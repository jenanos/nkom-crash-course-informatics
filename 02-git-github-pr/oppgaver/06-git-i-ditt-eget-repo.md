# Oppgave 6: Gjør mappen om til ditt eget repo

Målet er å ta Python-filene du har laget så langt og legge dem i ditt eget private repo på GitHub.

## Sjekk at du står i riktig mappe

Kjør:

```bash
cd ~/crash-course/fotballoppgaver
pwd
ls
```

Du skal stå i mappen med dine egne oppgaver.

## Lag `.gitignore`

Lag filen `.gitignore` og legg inn:

```text
.venv/
__pycache__/
```

Forklaring:
- `.venv/` skal ikke pushes til GitHub
- `__pycache__/` er midlertidige Python-filer

## Start Git lokalt

Kjør:

```bash
git init -b main
git status
```

## Lagre første versjon

Kjør:

```bash
git add .
git commit -m "Legg til første fotballoppgaver"
```

## Opprett privat repo på GitHub

Kjør:

```bash
gh repo create fotballoppgaver --private --source=. --remote=origin --push
```

## Sjekk at alt er koblet riktig

Kjør:

```bash
git remote -v
git status
```

## Kontrollspørsmål

- Hvorfor legger vi `.venv/` i `.gitignore`?
- Hva er forskjellen på lokal mappe, Git og GitHub?
