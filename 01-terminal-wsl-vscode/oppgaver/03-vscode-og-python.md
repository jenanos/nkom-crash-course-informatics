# Oppgave 3: VS Code og din første Python-fil

VS Code er en editor. Det betyr at du bruker den til å skrive og lagre kode. VS Code er ikke selve Python.

Python-koden ligger i en fil. Terminalen brukes til å kjøre filen.

## Åpne mappen i VS Code

Kjør:

```bash
code .
```

Forklaring:
- `code .` åpner mappen du står i, i VS Code

## Installer Python-utvidelsen i VS Code

1. Gå til **Extensions** i menyen til venstre.
2. Søk etter **Python**.
3. Installer utvidelsen fra **Microsoft**.

## Lag din første Python-fil

Kjør:

```bash
touch min_forste_pythonfil.py
```

Forklaring:
- `touch` lager en tom fil

Åpne filen:

```bash
code min_forste_pythonfil.py
```

Lim inn denne Python-koden i filen:

```python
print("Hello World, mitt navn er Jens")
```

Bytt ut `Jens` med ditt eget navn.

## Kjør filen

Kjør:

```bash
python3 min_forste_pythonfil.py
```

Forklaring:
- `python3` starter Python
- `min_forste_pythonfil.py` er filen Python skal kjøre

## Vanlige feil

- Hvis filen ikke finnes: sjekk at du står i riktig mappe med `pwd` og `ls`
- Hvis Python ikke finnes: prøv `python3 --version`
- Hvis programmet ikke skriver ut forventet tekst: sjekk at filen er lagret
