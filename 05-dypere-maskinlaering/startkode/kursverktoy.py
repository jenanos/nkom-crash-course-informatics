"""Gjenbruk etter at treningsløkken er forklart i notatbok 02. Ingen skjult trening."""
import random
from time import perf_counter
import torch
from torch import nn
from torch.utils.data import DataLoader


def sett_seed(seed=42):
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def velg_enhet():
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def lag_lastere(trening, validering, batch=64):
    # Én prosess gir et enkelt utgangspunkt i Windows/WSL og notatbøker.
    # Egen generator gjør at dropout ikke endrer neste epokes stokkerekkefølge.
    generator = torch.Generator().manual_seed(42)
    return (DataLoader(trening, batch_size=batch, shuffle=True, num_workers=0, generator=generator),
            DataLoader(validering, batch_size=batch, shuffle=False, num_workers=0))


def maal(modell, laster, enhet):
    """Gjennomsnitt per eksempel, også når siste batch er mindre."""
    modell.eval()
    sum_feil, riktige, antall = 0.0, 0, 0
    with torch.no_grad():
        for bilder, fasit in laster:
            bilder, fasit = bilder.to(enhet), fasit.to(enhet)
            logits = modell(bilder)
            feil = nn.functional.cross_entropy(logits, fasit)
            sum_feil += feil.item() * len(fasit)
            riktige += (logits.argmax(1) == fasit).sum().item()
            antall += len(fasit)
    return sum_feil / antall, riktige / antall


def tren(modell, trening, validering, enhet, epoker=3, lr=0.001, frys_basen=False):
    """Ny optimizer per forsøk. Best valideringstilstand lagres på CPU."""
    optimizer = torch.optim.Adam(
        (p for p in modell.parameters() if p.requires_grad), lr=lr)
    historikk, beste, beste_feil = [], None, float("inf")
    for epoke in range(epoker):
        modell.train()
        if frys_basen:
            # ResNet har BatchNorm: eval hindrer at også statistikken endres.
            modell.eval()
            modell.fc.train()
        sum_feil, antall = 0.0, 0
        if enhet.type == "cuda":
            torch.cuda.synchronize()
        start = perf_counter()
        for bilder, fasit in trening:
            bilder, fasit = bilder.to(enhet), fasit.to(enhet)
            optimizer.zero_grad()
            logits = modell(bilder)
            feil = nn.functional.cross_entropy(logits, fasit)
            feil.backward()
            optimizer.step()
            sum_feil += feil.item() * len(fasit)
            antall += len(fasit)
        if enhet.type == "cuda":
            torch.cuda.synchronize()
        sekunder = perf_counter() - start
        val_feil, val_treff = maal(modell, validering, enhet)
        rad = {"epoke": epoke + 1, "treningsfeil": sum_feil / antall,
               "valideringsfeil": val_feil, "valideringstreff": val_treff,
               "trening_sekunder": sekunder}
        historikk.append(rad)
        print(f"Epoke {epoke + 1}: trening={rad['treningsfeil']:.3f}, "
              f"validering={val_feil:.3f}, treff={val_treff:.1%}, trening={sekunder:.1f}s")
        if val_feil < beste_feil:
            beste_feil = val_feil
            beste = {k: v.detach().cpu().clone() for k, v in modell.state_dict().items()}
    if beste is not None:
        modell.load_state_dict(beste)
    return historikk
