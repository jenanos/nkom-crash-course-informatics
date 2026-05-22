# Oppgave 7: Enkel offside-sjekk

Målet er å kombinere funksjoner og `if` i et lite fotballprogram.

## Lag en ny fil

Kjør:

```bash
touch offside.py
code offside.py
```

## Lag en veldig enkel offside-funksjon

Lag en funksjon som heter `er_offside`.

Funksjonen skal ta imot tre tall:
- spillerens posisjon
- ballens posisjon
- posisjonen til nest siste forsvarer

Bruk denne enkle regelen i oppgaven:
- spilleren er offside hvis spilleren er nærmere mål enn både ballen og nest siste forsvarer

Funksjonen skal returnere `True` eller `False`.

## Skriv ut svaret

Test funksjonen med minst tre eksempler og skriv ut:
- `Offside`
- eller `Ikke offside`

Kjør:

```bash
python3 offside.py
```

## Kontrollspørsmål

- Hva betyr det at en funksjon returnerer en verdi?
- Hvorfor er denne offside-regelen enklere enn ekte fotballregler?
