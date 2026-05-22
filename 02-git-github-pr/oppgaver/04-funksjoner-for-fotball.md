# Oppgave 4: Funksjoner for fotball

Målet er å lage funksjoner som kan brukes flere ganger.

## Lag en ny fil

Kjør:

```bash
touch fotballfunksjoner.py
code fotballfunksjoner.py
```

## Lag funksjonen `skriv_resultat`

En funksjon i Python skrives med `def`, navn på funksjonen og parenteser:

```python
def skriv_resultat(hjemmelag, bortelag, hjemmemaal, bortemaal):
    print(f"{hjemmelag} {hjemmemaal} - {bortemaal} {bortelag}")
```

Merk:
- `def` starter funksjonen
- navnet på funksjonen kommer etter `def`
- verdiene funksjonen tar imot skrives inne i parentesene
- kolon `:` kommer på slutten av første linje
- koden inni funksjonen må stå innrykket

Lag en funksjon som tar imot:
- hjemmelag
- bortelag
- hjemmemål
- bortemål

Funksjonen skal skrive ut kampresultatet på en pen måte.

Etterpå skal funksjonen også skrive ut:
- `Hjemmelaget vant`
- `Bortelaget vant`
- eller `Det ble uavgjort`

Tips: Bruk en `if`-setning inni funksjonen for å velge riktig tekst.

## Kall funksjonen flere ganger

Når du skal bruke funksjonen, skriver du navnet og sender inn verdier:

```python
skriv_resultat("Brann", "Viking", 2, 1)
skriv_resultat("Lyn", "Start", 0, 0)
```

Bruk funksjonen til å skrive ut minst tre ulike kamper.

Kjør:

```bash
python3 fotballfunksjoner.py
```

## Kontrollspørsmål

- Hvorfor er det nyttig å samle kode i en funksjon?
- Hva er forskjellen på verdiene inni funksjonen og verdiene du sender inn når du kaller den?
