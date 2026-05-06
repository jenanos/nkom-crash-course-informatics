# Oppgave 1: Klone repoet

Forutsetning: GitHub CLI er installert, og du har en GitHub-bruker.

## Logg inn i GitHub CLI

Kjør:

```bash
gh auth login
```

Forklaring:
- `gh` er GitHub CLI
- `auth login` starter innlogging
- Følg instruksjonene som vises i terminalen

## Klon repoet

Kjør:

```bash
cd ~/crash-course
gh repo clone DIN-GITHUB-BRUKER/informatikk-crash-course
cd informatikk-crash-course
```

Viktig:
- `DIN-GITHUB-BRUKER` er en plassholder
- kursholder skal erstatte denne før repoet brukes i undervisning

## Kontroller at alt ser riktig ut

Kjør:

```bash
pwd
ls
git status
git remote -v
```

Forklaring:
- `pwd` viser hvor du står
- `ls` viser filer og mapper
- `git status` viser status i repoet
- `git remote -v` viser hvor repoet er koblet mot på GitHub
