# Oppgave 1: Komme i gang med WSL og kursmappen

I denne oppgaven skal du åpne Ubuntu fra Windows og lage kursmappen du skal jobbe i.

## Før du starter: kopiere og lime inn i terminalen

I terminalen fungerer kopiering og liming litt annerledes enn i vanlige Windows-programmer.

For å lime inn tekst i Ubuntu/WSL-terminalen kan du vanligvis bruke:
- `Ctrl` + `Shift` + `V`
- eller høyreklikk i terminalen

For å kopiere tekst ut fra terminalen:
- marker teksten med musen
- trykk `Ctrl` + `Shift` + `C`
- eller høyreklikk og velg kopier

Hvis `Ctrl` + `C` nevnes senere i kurset, betyr det som regel ikke kopier. I terminalen brukes `Ctrl` + `C` ofte til å stoppe et program som kjører.

## Del 1: Lag kursmappen

Åpne **Ubuntu** eller **WSL** fra Start-menyen i Windows.

Skriv disse kommandoene i terminalen:

```bash
cd ~
mkdir crash-course
cd crash-course
pwd
```

Forklaring:
- `cd ~` betyr: gå til hjemmemappen din
- `mkdir crash-course` lager en mappe som heter `crash-course`
- `cd crash-course` går inn i mappen
- `pwd` viser hvor du står akkurat nå

Hvis alt gikk bra, skal du nå stå i mappen `~/crash-course`.

## Del 2: Hent ZIP-filen inn i WSL

1. Last ned ZIP-filen fra e-posten du har fått.
2. Sjekk at du fortsatt står i `~/crash-course`.
3. Kjør denne kommandoen:

```bash
explorer.exe .
```

Forklaring:
- `explorer.exe .` åpner Windows Utforsker i Ubuntu-mappen du står i nå
- Punktum `.` betyr: mappen jeg står i akkurat nå

Når vinduet åpner seg:
- finn ZIP-filen du lastet ned fra e-post
- dra ZIP-filen inn i dette vinduet

## Del 3: Se at filen er der

Kjør:

```bash
ls
```

Forklaring:
- `ls` viser filer og mapper i mappen du står i

Du skal nå se ZIP-filen i listen.

## Del 4: Pakk ut ZIP-filen

Kjør:

```bash
unzip 01-terminal-wsl-vscode.zip
```

Hvis du får beskjed om at `unzip` mangler, kjør først:

```bash
sudo apt update
sudo apt install unzip
```

Forklaring:
- `sudo apt update` oppdaterer listen over programmer som kan installeres
- `sudo apt install unzip` installerer programmet `unzip`

Når `unzip` er installert, kjører du unzip-kommandoen igjen.

## Del 5: Gå inn i kursmappen

Kjør:

```bash
ls
cd 01-terminal-wsl-vscode
ls
```

Forklaring:
- første `ls` viser at mappen ble pakket ut
- `cd 01-terminal-wsl-vscode` går inn i kursmappen
- siste `ls` viser innholdet i kursmappen

## Kontrollspørsmål

- Hvilken mappe står du i nå?
- Hva viser kommandoen `pwd`?
- Ser du mappene `oppgaver`, `filer`, `eksempler` og `prompts`?
