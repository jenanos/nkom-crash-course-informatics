# Oppgave 7: pip og virtuelt miljø

Målet i denne oppgaven er å forstå at pakker er ferdig kode andre har skrevet, at `pip` installerer Python-pakker, og at et virtuelt miljø holder pakker adskilt fra resten av maskinen.

Veldig enkelt forklart:
- En pakke er ferdig kode vi kan bruke.
- `pip` er et verktøy for å installere Python-pakker.
- Et virtuelt miljø er en liten lokal Python-installasjon for prosjektet.

## Slik gjør du det

1. Stå i mappen `01-terminal-wsl-vscode`.
2. Lag virtuelt miljø:

```bash
python3 -m venv .venv
```

Hvis dette feiler, skriv:

```bash
sudo apt install python3-venv
```

3. Aktiver miljøet:

```bash
source .venv/bin/activate
```

Forklaring:
- Etter aktivering skal du se `(.venv)` først i terminalen
- Det betyr at du jobber inne i det virtuelle miljøet

4. Installer `pyfiglet`:

```bash
pip install pyfiglet
```

5. Lag fil:

```bash
touch banner.py
code banner.py
```

6. Lim inn denne Python-koden i filen:

```python
import pyfiglet

tekst = input("Skriv noe: ")
print(pyfiglet.figlet_format(tekst))
```

7. Kjør:

```bash
python3 banner.py
```

8. Avslutt virtuelt miljø:

```bash
deactivate
```

## Kontrollspørsmål

- Hva betyr `(.venv)`?
- Hva gjorde `pip install pyfiglet`?
- Hvorfor måtte vi installere pakken før `import pyfiglet` virket?
