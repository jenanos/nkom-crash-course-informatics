# Oppgave 4: Opprett en Pull Request

Målet er å opprette en PR på GitHub og forstå at PR brukes for å foreslå og diskutere endringer.

## Lag PR fra terminalen

Stå i rotmappen i repoet og kjør:

```bash
gh pr create --base main --head min-forste-branch --title "Min første PR" --body "Dette er min første pull request."
```

Hvis GitHub CLI åpner nettleser eller spør om valg, følger du instruksjonene.

## Åpne PR-en i nettleser

Kjør:

```bash
gh pr view --web
```

Forklaring:
- `base` er branchen du vil inn i
- `head` er branchen med endringene dine
- en PR er en forespørsel om å slå endringer sammen

## Frivillig

- Be en kollega se på PR-en
- Skriv en kommentar i PR-en
- Merge PR-en hvis kursholder ønsker det
