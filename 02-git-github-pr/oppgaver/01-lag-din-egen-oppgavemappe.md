# Oppgave 1: Lag din egen oppgavemappe

Målet er å lage et sted der du kan samle dine egne Python-oppgaver. Denne mappen blir senere ditt eget Git-repo.

## Lag mappen ved siden av kursrepoet

Kjør:

```bash
cd ~/crash-course
mkdir fotballoppgaver
cd fotballoppgaver
pwd
ls
```

Forklaring:
- Du lager en ny mappe for dine egne filer.
- Du står ikke inne i kursrepoet når du lager løsningene dine.

## Lag et virtuelt miljø

Kjør:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Hvis det feiler, prøv:

```bash
sudo apt install python3-venv
```

## Åpne mappen i VS Code

Kjør:

```bash
code .
```

Lag to tomme filer:
- `README.md`
- `spillerkort.py`

Skriv én linje i `README.md` som forklarer at dette er dine egne fotballoppgaver i Python.

## Kontrollspørsmål

- Hvorfor er det nyttig å ha en egen mappe for oppgavene?
- Hva betyr det når du ser `(.venv)` i terminalen?
