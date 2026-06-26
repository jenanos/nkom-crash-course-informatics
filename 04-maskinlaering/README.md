# Del 4: Maskinlæring

Denne delen handler om maskinlæring. Du skal lære hva maskinlæring er, hvordan det fungerer, og prøve det selv med små modeller som kjører på din egen maskin.

Vi bruker et kjent datasett: passasjerlisten fra Titanic. Målet er å bygge modeller som kan forutsi hvem som overlevde forliset, basert på informasjon som alder, kjønn og billetklasse.

## Hva du trenger

Alt kjøres lokalt på din laptop. Du trenger:

- Python 3 (som du allerede har fra del 1)
- Noen Python-pakker som vi installerer underveis

## Begreper

- **Maskinlæring:** en måte å la datamaskinen finne mønstre i data, uten at vi skriver eksplisitte regler
- **Modell:** et program som har lært fra data og kan gjøre forutsigelser
- **Trening:** prosessen der modellen lærer fra data
- **Prediksjon:** når modellen gjetter et svar på nye data
- **Feature (variabel):** en egenskap vi gir modellen, for eksempel alder eller kjønn
- **Target (mål):** det vi vil at modellen skal forutsi, for eksempel om noen overlevde
- **Regresjon:** forutsi et tall (for eksempel en pris)
- **Klassifisering:** forutsi en kategori (for eksempel ja/nei, overlevde/ikke)
- **Treningssett:** data modellen lærer fra
- **Testsett:** data vi tester modellen på etterpå, som den ikke har sett før
- **Nevralt nett:** en modell inspirert av hjernen, med lag av «nevroner»

## Installere pakker

Kjør dette i terminalen for å installere det du trenger:

```bash
pip install pandas scikit-learn matplotlib
```

Disse pakkene gjør:
- **pandas:** lese og jobbe med tabelldata (som CSV-filer)
- **scikit-learn:** bygge maskinlæringsmodeller
- **matplotlib:** lage grafer og visualiseringer

## Anbefalt rekkefølge

1. `oppgaver/01-hva-er-maskinlaering.md`
2. `oppgaver/02-utforsk-data.md`
3. `oppgaver/03-lineaer-regresjon.md`
4. `oppgaver/04-logistisk-regresjon.md`
5. `oppgaver/05-beslutningstraer.md`
6. `oppgaver/06-nevralt-nett.md`
7. `oppgaver/07-sammenlign-modeller.md`

## Tips

- Ikke vær redd for feilmeldinger. Les dem og spør ChatGPT om hjelp.
- Du trenger ikke forstå all matematikken. Fokuser på hva modellen gjør og hvorfor.
- Alt kjøres på CPU, så det går raskt nok med disse små datasettene.
