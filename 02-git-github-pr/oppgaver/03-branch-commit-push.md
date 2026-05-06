# Oppgave 3: Branch, commit og push

Målet er å endre kode, lagre endringen i Git og pushe den til GitHub.

## Gå til prosjektet og kjør det

Kjør:

```bash
cd 02-git-github-pr/prosjekt
python3 main.py
```

## Gå tilbake til rotmappen i repoet

Kjør:

```bash
cd ../..
```

## Lag en ny branch

Kjør:

```bash
git switch -c min-forste-branch
```

Forklaring:
- en branch er et eget arbeidsområde for endringer

## Åpne prosjektet i VS Code

Kjør:

```bash
code 02-git-github-pr/prosjekt
```

Gjør én liten endring:
- enten i `data/eksempeltekst.txt`
- eller i `main.py`

## Sjekk status og lagre endringen i Git

Kjør:

```bash
git status
git add 02-git-github-pr/prosjekt
git commit -m "Endre tekstverktoy"
```

Forklaring:
- `git status` viser hvilke filer som er endret
- `git add` gjør endringene klare for commit
- `git commit` lager et lagret punkt i historikken

## Push branchen til GitHub

Kjør:

```bash
git push -u origin min-forste-branch
```

Forklaring:
- `push` sender endringen til GitHub
- `-u` kobler lokal branch til branch på GitHub
