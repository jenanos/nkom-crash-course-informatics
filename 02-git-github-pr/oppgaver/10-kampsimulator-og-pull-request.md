# Oppgave 10: Kampsimulator og pull request

Målet er å avslutte del 2 med et litt morsommere program og bruke branch, commit, push og pull request.

## Lag en ny branch

Stå i `fotballoppgaver` og kjør:

```bash
git switch -c kamp-simulator
```

## Lag et nytt program

Kjør:

```bash
touch kamp_simulator.py
code kamp_simulator.py
```

Lag et program som:
- importerer `random`
- velger tilfeldige mål for to lag med `random.randint(...)`
- bruker en funksjon til å skrive ut resultatet
- simulerer minst 3 kamper i en løkke

Du kan bruke lag du liker, for eksempel favorittlaget ditt mot andre lag.

## Lagre og push

Kjør:

```bash
git status
git add .
git commit -m "Legg til kampsimulator"
git push -u origin kamp-simulator
```

## Opprett pull request

Kjør:

```bash
gh pr create --base main --head kamp-simulator --title "Legg til kampsimulator" --body "Jeg har laget en enkel kampsimulator i Python."
```

Hvis GitHub CLI spør om valg, følger du instruksjonene.

## Åpne PR-en i nettleser

Kjør:

```bash
gh pr view --web
```

## Kontrollspørsmål

- Hvorfor lager vi en egen branch før vi gjør nye endringer?
- Hva er forskjellen på `push` og pull request?
