# Oppgave 5: Lister og løkker

Målet er å lagre flere spillere i en liste og gå gjennom dem med en løkke.

## Lag en ny fil

Kjør:

```bash
touch tropp.py
code tropp.py
```

## Lag en enkel tropp

En liste i Python skrives med hakeparenteser:

```python
spillere = ["Ada", "Caroline", "Frida", "Guro", "Ingrid", "Tuva"]
```

En `for`-løkke som går gjennom listen kan skrives slik:

```python
for spiller in spillere:
    print(spiller)
```

Merk:
- `for` tar én verdi av gangen fra listen
- `spiller` er bare et navn du velger selv
- kolon `:` kommer på slutten av `for`-linjen
- koden inni løkken må stå innrykket

Lag en liste med minst 6 fotballspillere.

Programmet skal:
- skrive ut en overskrift
- gå gjennom listen med en `for`-løkke
- skrive ut ett navn per linje
- skrive ut hvor mange spillere som er i troppen med `len(...)`

Legg deretter til én ny spiller i listen og kjør programmet på nytt.

Tips: Du kan legge til en ny spiller med `spillere.append("Ny spiller")`.

Kjør:

```bash
python3 tropp.py
```

## Prøv selv

- Bytt ut én spiller i listen.
- Legg inn navnet på favorittspilleren din.

## Kontrollspørsmål

- Hva er en liste?
- Hva gjør en `for`-løkke i dette programmet?
