# Oppgave 3: Hent norske helligdager

API:
`https://date.nager.at/api/v3/PublicHolidays/2025/NO`

Målet er å hente norske helligdager og skrive ut dato og navn.

## Slik gjør du det

Lag en ny fil:

```bash
touch helligdager.py
code helligdager.py
```

Bruk `api_hjelper.py`, eller be ChatGPT lage en fil som:
- henter JSON fra URL-en over
- går gjennom listen
- skriver ut `date` og `localName`

## Eksempelprompt

```text
Lag et Python 3-program i én fil som henter norske helligdager for 2025 fra dette API-et:
https://date.nager.at/api/v3/PublicHolidays/2025/NO

Krav:
- Bruk bare Python standardbibliotek.
- Skriv ut dato og norsk navn på hver helligdag.
- Forklar hvordan jeg kjører programmet i Ubuntu/WSL.
```

## Ekstraoppgave

- La brukeren skrive inn årstall selv
