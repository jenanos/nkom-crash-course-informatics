# Oppgave 2: Variabler og utskrift

Målet er å bli trygg på å lagre verdier i variabler og skrive dem ut med Python.

## Åpne filen

Stå i `fotballoppgaver` og åpne:

```bash
code spillerkort.py
```

## Lag et enkelt spillerkort

En variabel lager du ved å skrive navn, så `=`, og så verdien:

```python
navn = "Ada Hegerberg"
lag = "Lyon"
draktnummer = 14
maal = 12
```

Du kan skrive ut tekst med `print(...)`:

```python
print("Spillerkort")
print(navn)
print(f"{navn} spiller for {lag}")
```

Skriv et lite program som lager variabler for:
- spillerens navn
- lag
- draktnummer
- antall mål denne sesongen

Programmet skal skrive ut informasjonen som et lite spillerkort.

Tips:
- tekst skrives med anførselstegn, for eksempel `"Brann"`
- tall skrives uten anførselstegn, for eksempel `7`
- `f` foran en streng gjør at du kan sette inn variabler med `{...}`

Forslag til utskrift:
- en overskrift
- én linje per opplysning
- minst én linje med en `f`-streng

## Prøv selv

- Bytt ut verdiene med en annen spiller.
- Kjør filen flere ganger etter små endringer.

Kjør:

```bash
python3 spillerkort.py
```

## Kontrollspørsmål

- Hva er en variabel?
- Hva er forskjellen på teksten inne i filen og utskriften i terminalen?
