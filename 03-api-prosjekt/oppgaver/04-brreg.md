# Oppgave 4: Søk i Enhetsregisteret

API:
`https://data.brreg.no/enhetsregisteret/api/enheter?navn=arbeidstilsynet`

Målet er å hente virksomhetsdata fra Brønnøysundregistrene og skrive ut navn, organisasjonsnummer og organisasjonsform hvis data finnes.

## Slik gjør du det

Lag fil:

```bash
touch brreg.py
code brreg.py
```

## Prompt til ChatGPT

```text
Lag et Python 3-program i én fil som søker i Brønnøysundregistrenes Enhetsregister-API.

URL:
https://data.brreg.no/enhetsregisteret/api/enheter?navn=arbeidstilsynet

Krav:
- Bruk bare Python standardbibliotek.
- Hent JSON.
- Finn listen med enheter i svaret.
- Skriv ut de fem første treffene.
- For hvert treff, skriv ut navn, organisasjonsnummer og organisasjonsform hvis feltene finnes.
- Koden skal tåle at noen felter mangler.
- Forklar hvordan jeg kjører filen.
```

## Ekstraoppgave

- La brukeren skrive inn søkeord selv
- URL-enkode søkeordet riktig
