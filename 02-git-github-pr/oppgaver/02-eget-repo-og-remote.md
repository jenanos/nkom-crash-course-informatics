# Oppgave 2: Lag ditt eget private repo

Målet er at du skal lage en egen privat kopi på GitHub og forstå forskjellen på kursholders repo og ditt eget repo.

## Stå i rotmappen til det klonede repoet

Kjør:

```bash
cd ~/crash-course/nkom-crash-course-informatics
```

## Sjekk dagens remote

Kjør:

```bash
git remote -v
```

Forklaring:
- Foreløpig peker `origin` til kursholders public repo.

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
gh repo create mitt-nkom-crash-course-informatics --private --source=. --remote=origin --push
```

Forklaring:
- `upstream` = kursholders repo
- `origin` = ditt eget repo
- `private` = bare du har tilgang, med mindre du inviterer andre
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
