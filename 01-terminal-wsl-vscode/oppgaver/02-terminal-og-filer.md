# Oppgave 2: Terminal og filer

Målet i denne oppgaven er å lære noen enkle og nyttige terminalkommandoer.

## Del A: Hvor er jeg?

Kjør:

```bash
pwd
ls
ls -la
```

Forklaring:
- `pwd` viser hvilken mappe du står i
- `ls` viser vanlige filer og mapper
- `ls -la` viser mer detaljert liste, også skjulte filer

Forskjellen på `ls` og `ls -la` er altså at `ls -la` viser mer informasjon.

## Del B: Se mappestruktur

Installer `tree`:

```bash
sudo apt update
sudo apt install tree
```

Kjør deretter:

```bash
tree
```

Forklaring:
- `tree` viser mapper og filer som en visuell trestruktur

## Del C: Lag en tekstfil

Kjør:

```bash
echo "Hei, jeg lærer terminalen" > notat.txt
cat notat.txt
echo "Dette er linje 2" >> notat.txt
cat notat.txt
```

Forklaring:
- `echo` skriver tekst
- `>` skriver over filen eller lager filen hvis den ikke finnes
- `>>` legger til ny tekst nederst i filen
- `cat` viser innholdet i filen

## Del D: Kopier, flytt og slett

Kjør:

```bash
cp notat.txt kopi.txt
ls
mv kopi.txt nytt-navn.txt
ls
rm nytt-navn.txt
ls
```

Forklaring:
- `cp` kopierer en fil
- `mv` flytter eller gir nytt navn til en fil
- `rm` sletter en fil

## Del E: Søk i tekst

Kjør:

```bash
echo "banan eple appelsin banan" > frukt.txt
grep banan frukt.txt
wc frukt.txt
wc -w frukt.txt
```

Forklaring:
- `grep banan frukt.txt` finner linjer som inneholder ordet `banan`
- `wc frukt.txt` teller linjer, ord og tegn i filen
- `wc -w frukt.txt` teller bare ord

## Del F: Finn filer

Kjør:

```bash
find . -name "*.txt"
find . -name "*.py"
```

Forklaring:
- `find` leter etter filer
- punktum `.` betyr: mappen jeg står i nå
- `-name "*.txt"` betyr: finn filer som slutter på `.txt`
