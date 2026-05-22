# Oppgave 3: If og kampresultater

Målet er å bruke `if`, `elif` og `else` for å ta enkle valg i programmet.

## Lag en ny fil

Kjør:

```bash
touch kampresultat.py
code kampresultat.py
```

## Lag et program for resultat

Du kan starte med variabler slik:

```python
hjemmelag = "Brann"
bortelag = "Viking"
hjemmemaal = 3
bortemaal = 1
```

En `if`-setning i Python skrives slik:

```python
if hjemmemaal > bortemaal:
    print("Hjemmeseier")
elif hjemmemaal < bortemaal:
    print("Borteseier")
else:
    print("Uavgjort")
```

Merk:
- kolon `:` kommer etter `if`, `elif` og `else`
- linjene inni blokken må stå litt innrykket
- du kan bruke `>` , `<` og `==` for å sammenligne verdier

Lag variabler for:
- hjemmelag
- bortelag
- hjemmemål
- bortemål

Programmet skal skrive ut:
- `Hjemmeseier` hvis hjemmelaget scorer mest
- `Borteseier` hvis bortelaget scorer mest
- `Uavgjort` hvis lagene scorer like mye

Legg også til en ekstra sjekk:
- hvis totalt antall mål er 5 eller mer, skriv ut `For en målfest!`

Tips: Du kan regne ut totalen i en egen variabel, for eksempel `totalt = hjemmemaal + bortemaal`.

Kjør:

```bash
python3 kampresultat.py
```

## Prøv selv

Test minst tre ulike resultater.

## Kontrollspørsmål

- Når brukes `elif`?
- Hva skjer hvis flere `if`-tester kan være sanne i samme program?
