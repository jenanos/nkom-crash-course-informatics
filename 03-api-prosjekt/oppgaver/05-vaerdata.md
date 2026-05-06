# Oppgave 5: Hent værdata

Målet er å hente værdata fra et åpent API og skrive ut noen få verdier på en ryddig måte.

I denne oppgaven kan du bruke Open-Meteo. API-et krever ikke API-nøkkel.

Eksempel-URL:
`https://api.open-meteo.com/v1/forecast?latitude=59.91&longitude=10.75&current=temperature_2m,wind_speed_10m`

## Slik gjør du det

1. Lag en ny fil:

```bash
touch vaer.py
code vaer.py
```

2. Be ChatGPT lage et program som:
- henter JSON fra URL-en
- finner delen som heter `current`
- skriver ut temperatur og vindstyrke

## Eksempelprompt

```text
Lag et Python 3-program i én fil som henter værdata fra Open-Meteo.

URL:
https://api.open-meteo.com/v1/forecast?latitude=59.91&longitude=10.75&current=temperature_2m,wind_speed_10m

Krav:
- Bruk bare Python standardbibliotek.
- Hent JSON fra URL-en.
- Skriv ut temperatur og vindstyrke på en ryddig måte.
- Koden skal tåle at et felt mangler.
- Forklar hvordan jeg kjører filen i Ubuntu/WSL.
```

## Ekstraoppgave

- Bytt koordinater til et annet sted
- La brukeren skrive inn breddegrad og lengdegrad selv
