# Oppgave 2: Lag ditt eget private repo

Målet er at du skal lage en egen privat kopi på GitHub og forstå forskjellen på kursholders repo og ditt eget repo.

## Sjekk dagens remote

Kjør:

```bash
git remote -v
```

## Gi kursholders repo navnet upstream

Kjør:

```bash
git remote rename origin upstream
```

Sjekk igjen:

```bash
git remote -v
```

## Opprett eget privat repo fra lokal mappe

Kjør:

```bash
gh repo create mitt-informatikk-crash-course --private --source=. --remote=origin --push
```

Forklaring:
- `gh repo create` lager et nytt repo på GitHub
- `--private` gjør repoet privat
- `--source=.` betyr: bruk mappen jeg står i nå
- `--remote=origin` setter det nye repoet som `origin`
- `--push` sender innholdet opp med en gang

## Sjekk remote på nytt

Kjør:

```bash
git remote -v
```

Forventet resultat:
- `origin` skal peke til ditt eget repo
- `upstream` skal peke til kursholders repo

## Kontrollspørsmål

- Hva er forskjellen på `origin` og `upstream`?
- Hvorfor er eget repo privat?
