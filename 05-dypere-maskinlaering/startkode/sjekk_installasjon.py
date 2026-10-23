"""Kjør fra terminalen før notatbøkene: python startkode/sjekk_installasjon.py."""
import argparse
import importlib
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--krev-gpu", action="store_true")
    args = parser.parse_args()
    print("Python:", sys.version.split()[0], sys.executable)
    feil = []
    moduler = {}
    for navn in ("torch", "torchvision", "matplotlib", "ipykernel", "jupyterlab"):
        try:
            modul = importlib.import_module(navn)
            moduler[navn] = modul
            print(navn, getattr(modul, "__version__", "importert"))
        except Exception as exc:
            feil.append(f"{navn}: {exc}")
    if "torch" in moduler:
        torch = moduler["torch"]
        print("PyTorch CUDA-runtime:", torch.version.cuda)
        print("CUDA tilgjengelig:", torch.cuda.is_available())
        try:
            sted = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            x = torch.ones(2, 2, device=sted, requires_grad=True)
            (x @ x).sum().backward()
            assert torch.allclose(x.grad, torch.full_like(x, 4.0))
            if sted.type == "cuda":
                torch.cuda.synchronize()
                print("GPU:", torch.cuda.get_device_name(0))
                print("Totalt VRAM:", round(torch.cuda.get_device_properties(0).total_memory / 2**30, 1), "GiB")
            print("Beregning og gradienter virker på", sted)
        except Exception as exc:
            feil.append(f"Beregning feilet: {exc}")
        if args.krev_gpu and not torch.cuda.is_available():
            feil.append("GPU var påkrevd, men CUDA er ikke tilgjengelig.")
    if feil:
        for melding in feil:
            print("FEIL:", melding)
        print("Se OPPSETT.md og FEILSOKING.md.")
        return 1
    print("Installasjonssjekken besto. Start med notatbok 00.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
