# Oppgave 1: Hva er maskinlæring?

## Hva betyr «maskinlæring»?

Vanlig programmering fungerer slik:

```
Data + Regler → Svar
```

Du skriver reglene selv. For eksempel: «Hvis alder > 18, gi tilgang.»

Maskinlæring snur dette på hodet:

```
Data + Svar → Regler (modell)
```

Du gir maskinen eksempler med riktige svar, og den finner reglene selv.

## Et konkret eksempel

Tenk deg at du vil forutsi om en Titanic-passasjer overlevde. Du har informasjon om 100 passasjerer: alder, kjønn, billetklasse, og om de faktisk overlevde.

Med vanlig programmering måtte du skrevet regler som:
- «Kvinner overlever oftere»
- «Førsteklassepassasjerer overlever oftere»
- «Barn overlever oftere»

Med maskinlæring gir du bare dataene til en algoritme, og den finner disse mønstrene selv.

## Viktige begreper

### Features (variabler)

Features er informasjonen du gir modellen. For Titanic kan det være:
- Alder
- Kjønn
- Billetklasse
- Pris på billetten

### Target (mål)

Target er det du vil forutsi. For Titanic er det: overlevde passasjeren? (1 = ja, 0 = nei)

### Trening og testing

Vi deler alltid dataene i to:
1. **Treningssett** (ca. 80 %): Modellen lærer fra disse
2. **Testsett** (ca. 20 %): Vi sjekker hvor god modellen er på data den aldri har sett

Hvorfor? Fordi vi vil vite om modellen har lært noe generelt, eller bare pugget svarene.

## Typer maskinlæring

### Regresjon
Forutsi et **tall**. Eksempler:
- Hva blir prisen på et hus?
- Hvor mange grader blir det i morgen?

### Klassifisering
Forutsi en **kategori**. Eksempler:
- Overlevde passasjeren? (ja/nei)
- Er e-posten spam? (ja/nei)
- Hva slags dyr er på bildet? (katt/hund/fugl)

I denne delen skal vi prøve begge deler.

## Oppgave

Før du går videre, tenk på disse spørsmålene:

1. Kan du komme på et eksempel fra din egen jobb der maskinlæring kunne vært nyttig?
2. Hva ville vært «features» og hva ville vært «target» i ditt eksempel?
3. Er det et regresjons- eller klassifiseringsproblem?

Skriv ned svarene i en fil som heter `mine-tanker.txt` i din egen mappe.

## Neste steg

I neste oppgave skal vi laste inn Titanic-datasettet og utforske det med Python.
