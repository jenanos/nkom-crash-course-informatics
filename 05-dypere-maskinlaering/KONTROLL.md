# Kontroll av kursmaterialet

Kontrollskriptet validerer notatbokformat, Python-syntaks og lokale lenker. Ved
kjøring starter hver notatbok med en ny Jupyter-kernel og kjøres i rekkefølge,
slik at gamle variabler ikke kan skjule en manglende celle. Originalnotatbøkene
beholdes uten utskrifter. Kontrollkjøringene lagres separat under `resultater/kontroll/`.

## Kjør kontrollene selv

Aktiver kursmiljøet og installer kontrollpakkene. PyTorch og Torchvision må allerede
være installert som forklart i oppsettet. Kjør fra kursdelens arbeidsmappe:

```bash
python -m pip install -r requirements-kontroll.txt
python startkode/kontroller_notatboker.py --bare-struktur
python startkode/kontroller_notatboker.py --kort
```

`--kort` bruker ekte datasett og samme modeller, men reduserer utvalg til høyst
256 eksempler, trening til to epoker og språkmodelltrening til 30 steg. Det endrer
bare en kopi i minnet. RL-episodene er uendret, siden de er raske og trengs for
å kontrollere at agenten lærer. En kort kjøring kontrollerer arbeidsflyten, ikke
kvaliteten etter full trening.

Uten eksterne datasett kan du kjøre 00, 01, 06, 07 og 08:

```bash
python startkode/kontroller_notatboker.py --uten-nedlasting
```

Vil du kontrollere alle standardinnstillingene, utelater du valgene:

```bash
python startkode/kontroller_notatboker.py
```

Ett kapittel kan kjøres med `--notatbok 04`. `--utmappe` velger en annen mappe for
kontrollresultatene. Kontrollen begrenser CPU til to tråder for små forsøk; den
endrer ikke originalnotatbøkenes trådvalg. Python-kernelen heter `python3` i
kontrollskriptet og kommer fra kontrollmiljøet, mens deltakeren velger
`Python (Nkom del 5)` i brukerflaten.

## Hva som kontrolleres

- Regresjonen lærer forventet stigning og startverdi innen en romslig toleranse.
- Bildeøvelsene bruker trenings- og valideringsindekser uten overlapp.
- Treningsfeilen i MLP-eksempelet går ned, og feilmålene er endelige tall.
- CNN-vekter gir samme output etter lagring og tilbakeinnlasting.
- ResNet har bare 5130 lærbare parametre, og basens BatchNorm-buffere er uendret.
- Attention-rader summerer til én, og maskerte forbindelser har vekt null.
- Endring av et framtidig tegn endrer ikke tidligere logits i transformeren.
- Språkmodellens valideringsfeil går ned, og meldingsdelene er adskilt.
- RL-miljøets kanter, hull og mål virker, og den lærte policyen slår tilfeldig handling.

Kontrollene er laget for å fange faglig viktige feil, ikke for å kreve identiske
treningsresultater på ulike maskiner. Ved en feil: les utskriften i den aktuelle
kontrollnotatboken og sjekk miljø, seed og kodeendringer før du justerer en kontroll.

## Testmiljø og praktiske grenser

Alle ni notatbøkene er kjørt fra start til slutt med standardinnstillingene på
CPU, og kontrollene over besto. Bildeøvelsene brukte ekte Fashion-MNIST- og
CIFAR-10-data, og overføringsøvelsen brukte de offisielle ResNet18-vektene.
Språkmodelløvelsen er også kjørt i hurtigmodus. Figurene for prediksjoner,
overtilpasning, CNN-aktiveringer, attention og forvirringsmatrise er sett over.
Installasjonssjekken besto på CPU og avviste som forventet kravet om GPU i et
miljø uten CUDA.

Materialet er kontrollert med Python 3.12.3, PyTorch 2.14.1 CPU, Torchvision 0.29.1,
Matplotlib 3.11.2 og Jupyter-kerneler via nbclient. Dette beskriver testmiljøet;
kravfilene tillater et versjonsintervall og er ikke en låst installasjon.

CPU-kjøringer dokumenterer at kode og læringsløp fungerer der. CUDA-utførelse,
VRAM-forbruk og treningstid på en RTX 3080 må kontrolleres på en faktisk GPU-maskin
med installasjonssjekken og benchmarken i notatbok 04.
