# Oppgave 8: Lese fra fil og rydde spillerliste

Målet er å lese navn fra fil, bruke en løkke og rydde i tekst som ikke ser lik ut.

## Kopier filen du trenger

Stå i `fotballoppgaver` og kjør:

```bash
cp ../nkom-crash-course-informatics/02-git-github-pr/ressurser/spillere_uryddig.txt .
ls
```

## Lag en ny fil

Kjør:

```bash
touch rydde_spillere.py
code rydde_spillere.py
```

## Les filen og rydd navnene

Programmet skal:
- åpne `spillere_uryddig.txt`
- lese én linje om gangen
- bruke `strip()` for å fjerne ekstra mellomrom
- bruke `title()` for å få penere store og små bokstaver
- hoppe over tomme linjer
- lagre de ryddede navnene i en ny liste

Skriv til slutt ut den ryddede listen.

## Lag en ny fil med ryddede navn

Utvid programmet slik at det også lager `spillere_ryddig.txt`.

Kjør:

```bash
python3 rydde_spillere.py
```

## Kontrollspørsmål

- Hvorfor er `strip()` nyttig når du leser fra fil?
- Hva gjør `title()` med teksten?
