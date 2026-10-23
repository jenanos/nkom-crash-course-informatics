"""Kjør hver notatbok i en ny Jupyter-kernel og lagre kontrollkjøringene separat."""
import argparse
import ast
from pathlib import Path
import re
import sys

import nbformat
from nbclient import NotebookClient

KURSMAPPE = Path(__file__).resolve().parents[1]


class KortKjoring(ast.NodeTransformer):
    """Reduser trening og utvalg i en minnekopi, aldri i originalnotatboken."""

    def visit_Assign(self, node):
        self.generic_visit(node)
        if any(isinstance(t, ast.Name) and t.id == "steg_antall" for t in node.targets):
            node.value = ast.Constant(30)
        if any(isinstance(t, ast.Name) and t.id == "epoker" for t in node.targets):
            node.value = ast.Constant(2)
        if any(isinstance(t, ast.Tuple) and [getattr(e, "id", "") for e in t.elts]
               == ["antall_trening", "antall_validering"] for t in node.targets):
            node.value = ast.Tuple(elts=[ast.Constant(256), ast.Constant(128)], ctx=ast.Load())
        return node

    def visit_Call(self, node):
        self.generic_visit(node)
        for kw in node.keywords:
            if kw.arg == "epoker" and isinstance(kw.value, ast.Constant):
                kw.value = ast.Constant(min(2, kw.value.value))
        # Bare utvalgsstørrelser i Subset, ikke RL-episoder eller train/val-skillet.
        if isinstance(node.func, ast.Name) and node.func.id == "Subset" and len(node.args) == 2:
            valg = node.args[1]
            if (isinstance(valg, ast.Call) and isinstance(valg.func, ast.Name)
                    and valg.func.id == "range" and len(valg.args) == 1
                    and isinstance(valg.args[0], ast.Constant)):
                valg.args[0] = ast.Constant(min(256, valg.args[0].value))
        return node


KONTROLLER = {
    "01": '''
assert abs(modell.weight.item() - 2) < 0.2
assert abs(modell.bias.item() - 1) < 0.2
''',
    "02": '''
assert set(trening.dataset.indices[i] for i in trening.indices).isdisjoint(
    validering.dataset.indices[i] for i in validering.indices)
assert len(historikk) == epoker
assert torch.isfinite(torch.tensor(historikk)).all()
assert historikk[-1][0] < historikk[0][0]
''',
    "03": '''
assert len(resultater) == 3
assert set(trening.dataset.indices[i] for i in trening.indices).isdisjoint(
    validering.dataset.indices[i] for i in validering.indices)
assert 0 <= test_treff <= 1
''',
    "04": '''
modell.eval()
kopi.eval()
with torch.no_grad():
    x = torch.randn(2, 3, 32, 32, device=enhet)
    assert torch.allclose(modell(x), kopi(x), atol=1e-6)
''',
    "05": '''
assert all(not p.requires_grad for navn, p in modell.named_parameters() if not navn.startswith("fc."))
assert sum(p.numel() for p in modell.parameters() if p.requires_grad) == 5130
# Basens BatchNorm-statistikk skal være uendret fra ferdigtrente vekter.
referanse = models.resnet18(weights=vekttype)
for navn, buffer in modell.named_buffers():
    assert torch.equal(buffer.cpu(), dict(referanse.named_buffers())[navn]), navn
''',
    "06": '''
assert torch.allclose(vekter.sum(-1), torch.ones(3))
assert torch.equal(kausale_vekter[0], torch.tensor([1., 0., 0.]))
assert torch.all(kausale_vekter[maske] == 0)
''',
    "07": '''
assert set(meldinger[:int(n*0.8)]).isdisjoint(meldinger[int(n*0.8):])
assert all(torch.isfinite(v).all() for v in modell.state_dict().values())
assert logg[-1][2] < logg[0][2]
# Endring av et framtidig tegn må ikke endre logits på tidligere posisjoner.
modell.eval()
probe = kod("i oslo ").unsqueeze(0).to(enhet)
endret = probe.clone()
endret[0, -1] = (endret[0, -1] + 1) % len(alfabet)
with torch.no_grad():
    assert torch.allclose(modell(probe)[:, :-1], modell(endret)[:, :-1], atol=1e-5)
''',
    "08": '''
assert flytt(0, 0) == (0, -0.01, False)
assert flytt(1, 2) == (5, -1.0, True)
assert flytt(14, 1) == (15, 1.0, True)
assert evaluer(False) > 0.9
assert evaluer(False) > evaluer(True)
''',
}


def kontroller_struktur(path, doc):
    nbformat.validate(doc)
    for indeks, celle in enumerate(doc.cells):
        if celle.cell_type == "code":
            ast.parse(celle.source, filename=f"{path.name}:celle {indeks}")
            if celle.outputs or celle.execution_count is not None:
                raise ValueError(f"{path.name}: originalfilen har lagrede kjøreresultater")
        else:
            for maal in re.findall(r"\]\(([^)]+)\)", celle.source):
                if "://" not in maal and not (path.parent / maal.split("#")[0]).exists():
                    raise ValueError(f"Ugyldig lokal lenke i {path.name}: {maal}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kort", action="store_true", help="Mindre utvalg, 2 epoker, 30 språkmodellsteg")
    parser.add_argument("--uten-nedlasting", action="store_true", help="Kjør bare 00, 01, 06, 07 og 08")
    parser.add_argument("--bare-struktur", action="store_true", help="Valider format, Python-syntaks og lokale lenker")
    parser.add_argument("--notatbok", choices=[f"{i:02d}" for i in range(9)],
                        help="Kjør bare ett prefiks, for eksempel 04")
    parser.add_argument("--utmappe", type=Path, default=KURSMAPPE / "resultater" / "kontroll")
    args = parser.parse_args()
    for path in sorted((KURSMAPPE / "notatboker").glob("*.ipynb")):
        doc = nbformat.read(path, as_version=4)
        kontroller_struktur(path, doc)
        prefiks = path.name[:2]
        if args.bare_struktur:
            print("Struktur OK:", path.name, flush=True)
            continue
        if args.notatbok and prefiks != args.notatbok:
            continue
        if args.uten_nedlasting and prefiks in {"02", "03", "04", "05"}:
            continue
        if args.kort:
            for celle in doc.cells:
                if celle.cell_type == "code":
                    tre = KortKjoring().visit(ast.parse(celle.source))
                    celle.source = ast.unparse(ast.fix_missing_locations(tre))
        # Begrens CPU-tråder for små kjøringer, ikke kursdeltakernes originalkode.
        doc.cells.insert(0, nbformat.v4.new_code_cell("import torch\ntorch.set_num_threads(2)"))
        if prefiks in KONTROLLER:
            doc.cells.append(nbformat.v4.new_code_cell(KONTROLLER[prefiks]))
        print("Kjører:", path.name, "(kort)" if args.kort else "(standard)", flush=True)
        client = NotebookClient(doc, timeout=1800, kernel_name="python3",
                                resources={"metadata": {"path": str(path.parent)}})
        client.execute()
        args.utmappe.mkdir(parents=True, exist_ok=True)
        nbformat.write(doc, args.utmappe / path.name)
        for celle in doc.cells:
            for output in celle.get("outputs", []):
                if output.output_type == "stream" and output.name == "stdout":
                    # Utelat nedlastingsprogresjon, men vis måleresultatene.
                    linjer = output.text.strip().splitlines()
                    print("\n".join(linjer[-6:]), flush=True)
        print("Kjøring og faglige kontroller OK:", path.name, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
