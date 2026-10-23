# Feilsøking

Les siste del av feilmeldingen først. Kontroller hvilken celle som feilet, hvilken
kernel som kjører, og om du har endret en tidligere celle uten å kjøre den på nytt.

## Feil Python eller manglende pakke

Ved `ModuleNotFoundError` kjører notatboken ofte med feil miljø. I en kodecelle:

```python
import sys
print(sys.executable)
```

Dette skal vise `.venv/bin/python` i din arbeidsmappe. Velg riktig kernel.
Installer pakker fra den aktiverte WSL-terminalen med `python -m pip`, og restart
kernel etter installasjon. Ved feil ved import av `torchvision`, kontroller at
`torch` og `torchvision` ble installert sammen fra samme PyTorch-valg.

## Navn mangler eller gamle resultater vises

`NameError` betyr ofte at en nødvendig celle ikke er kjørt. En notatbok lagrer
utskrifter, men den lagrer ikke nødvendigvis levende Python-variabler.
Velg Restart Kernel and Run All. Når du sammenligner modeller, må både modell og
optimizer lages på nytt. Å kjøre treningscellen igjen fortsetter ellers treningen.

## CUDA er ikke tilgjengelig

Kjør `nvidia-smi` i WSL og installasjonssjekken med `--krev-gpu`. Hvis `nvidia-smi`
virker, men `torch.version.cuda` er `None`, har du sannsynligvis CPU-utgaven av
PyTorch. Kontroller også kernel-stien. Installer paret `torch`/`torchvision` med
riktig CUDA-valg fra den offisielle velgeren. Hvis heller ikke `nvidia-smi` virker,
kontroller Windows-driver og WSL2-oppsett. Ved behov kan du kjøre `wsl --shutdown`
i PowerShell og starte WSL igjen; det stopper pågående WSL-prosesser, så lagre først.

## For lite GPU-minne

Ved `CUDA out of memory`, reduser batch, for eksempel 64 → 32 → 16. I språkmodellen
kan du også redusere kontekstlengde, men da må du bygge modellen på nytt. Restart
kernel for å fjerne gamle modeller og tensorer, og lukk andre programmer som bruker
GPU. `nvidia-smi` kan vise annen bruk, mens PyTorchs minnetall gjelder tensorallokering.

Ikke prøv å løse et minneproblem bare med flere epoker. Antall epoker styrer varighet;
batch, modell og aktiveringer avgjør mye av minnebehovet. `empty_cache()` frigjør
cache som ikke brukes, men kan ikke fjerne tensorer som Python fortsatt refererer til.

## Modell og data ligger ulike steder

En feil om `cpu` og `cuda` sammen betyr ofte at bare modellen eller bare dataene
er flyttet. Bruk `.to(enhet)` på både modellen, input og fasit. Matplotlib trenger
som regel `.cpu()` for å tegne GPU-tall; ved tensorer med gradienthistorikk bruker
du `.detach().cpu()` utenfor `no_grad()`.

## Feil form eller type

`mat1 and mat2 shapes cannot be multiplied` betyr ofte at antall verdier etter
utflating ikke stemmer med `Linear`. Skriv ut `.shape` før og etter hvert lag.
`CrossEntropyLoss` i bildeoppgavene venter desimaltallslogits `[batch, 10]` og
heltallsfasit `[batch]`. I språkmodellen flater vi batch og tid før feilmålet.

## Feilen blir NaN eller læringen stopper

Start med standardinnstillingene og nytt seed/modell/optimizer. En for høy
læringsrate kan gi ustabilitet. Kontroller også input, fasit og at du ikke legger
softmax før CrossEntropyLoss. Prøv ett lite batch og sjekk at feilen kan synke ved
å øve på akkurat det batchet. Det viser om modellen og løkken kan tilpasse seg,
men sier ingenting alene om generalisering.

## Nedlasting feiler

Fashion-MNIST, CIFAR-10 og ferdigtrente vekter trenger nett ved første kjøring.
Les URL-en og feilen: nettverk/proxy, full disk og en utilgjengelig kilde er ulike
problemer. Prøv samme celle igjen når nettverket fungerer. Hvis en nedlasting er
avbrutt og kontrollsummen feiler, fjern bare den aktuelle ufullstendige datafilen
og last ned igjen. Notatbok 00, 01, 06, 07 og 08 trenger ingen eksterne datasett.

## Treningen virker treg eller GPU er lite brukt

Små modeller kan være raskere på CPU fordi overhead dominerer. Dataforbehandling
kan dessuten bli en flaskehals, særlig ved oppskalering i ResNet-forsøket. Start med
benchmarken i notatbok 04 og sammenlign med full epoketid. Endre ett valg om gangen.
Vi bruker `num_workers=0` for et enkelt utgangspunkt; flere datalasterprosesser er
en videre optimalisering som også må måles.

## Be om hjelp med kontekst

Del feilmeldingen, koden i den aktuelle cellen, Python-stien og utskriften fra
installasjonssjekken. Be om en forklaring før du godtar en større omskriving.
Et nyttig spørsmål til ChatGPT er: «Forklar feilen på nybegynnernivå. Hvilket tall,
navn eller hvilken form forventet koden, og hva fikk den? Foreslå minste endring.»
