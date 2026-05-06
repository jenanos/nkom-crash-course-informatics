# Oppgave 5: Feilsøking med ChatGPT

Målet i denne oppgaven er å lære at feilmeldinger er informasjon. Du skal også øve på å lime inn kommando, feilmelding og kode i ChatGPT.

## Slik gjør du det

1. Gå til rotmappen for del 1.
2. Kjør:

```bash
python3 filer/feil_program.py
```

3. Programmet skal feile.
4. Kopier hele feilmeldingen.
5. Åpne filen `prompts/feilsoking.txt`.
6. Lim inn kommando, feilmelding og kode i prompten.
7. Be ChatGPT forklare og rette feilen.
8. Lag en ny fil:

```bash
cp filer/feil_program.py filer/feil_program_rettet.py
code filer/feil_program_rettet.py
```

9. Lim inn rettet kode.
10. Kjør:

```bash
python3 filer/feil_program_rettet.py
```

## Refleksjon

- Hva var feilen?
- Hvor i feilmeldingen sto filnavn og linjenummer?
- Hva endret ChatGPT?
