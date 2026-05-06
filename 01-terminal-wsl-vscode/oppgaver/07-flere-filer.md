# Oppgave 7: Et program med flere filer

Målet er å lære at et program kan bestå av flere filer, at Python kan importere kode fra en annen fil, og at terminalen må stå i riktig mappe.

## Slik gjør du det

1. Gå til `eksempler/flerfil`:

```bash
cd eksempler/flerfil
```

2. Se filene:

```bash
ls
```

3. Åpne mappen i VS Code:

```bash
code .
```

4. Se på `main.py` og `hilsen.py`.
5. Kjør:

```bash
python3 main.py
```

## Forklaring

- `main.py` er filen vi kjører
- `hilsen.py` inneholder en funksjon som `main.py` bruker
- Linjen `from hilsen import lag_hilsen` henter kode fra den andre filen

## Liten oppgave

- Endre teksten i `hilsen.py`
- Lagre filen
- Kjør `main.py` på nytt

## Frivillig feilsøkingsoppgave

Gå én mappe opp:

```bash
cd ..
```

Prøv å kjøre:

```bash
python3 main.py
```

Spørsmål:
- Hvorfor virker det ikke?

Gå tilbake:

```bash
cd flerfil
python3 main.py
```
