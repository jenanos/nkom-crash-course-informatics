# Oppgave 10: Klone hele kursrepoet

Målet i denne oppgaven er at du skal hente hele kursrepoet fra GitHub. Dette gir deg tilgang til del 2 og del 3.

Kort forklart:
- Å klone et repo betyr å kopiere et repo fra GitHub ned til maskinen din.

Dokumentasjon:
- <https://cli.github.com/manual/gh_repo_clone>

## Viktig før du starter

Frem til nå har du jobbet i ZIP-versjonen av del 1.

Nå skal du hente hele repoet fra GitHub.

Etter kloning finnes det derfor to kopier:

- ZIP-kopien av del 1
- Det komplette GitHub-repoet med del 1, del 2 og del 3

Dette er forventet og ikke feil.

## Stå i hovedmappen for kurset

Skriv:

```bash
cd ~/crash-course
pwd
ls
```

## Klon repoet

Du kan finne riktig kommando på GitHub:

1. Gå til repoet på GitHub:

   <https://github.com/jenanos/nkom-crash-course-informatics>

2. Trykk på den grønne knappen `Code`.
3. Velg fanen `GitHub CLI`.
4. Kopier kommandoen som starter med `gh repo clone`.
5. Lim kommandoen inn i terminalen.

Kommandoen skal være:

```bash
gh repo clone jenanos/nkom-crash-course-informatics
```

Viktig:
- `jenanos` er Jens GitHub-bruker for kursrepoet.

## Gå inn i repoet

Skriv:

```bash
cd nkom-crash-course-informatics
```

## Kontroller at alle tre delene finnes

Skriv:

```bash
ls
```

Du skal se omtrent:

```text
01-terminal-wsl-vscode
02-git-github-pr
03-api-prosjekt
README.md
```

## Kontroller Git-status

Skriv:

```bash
git status
```

Forklaring:
- `git status` viser status for repoet.

## Kontroller remote

Skriv:

```bash
git remote -v
```

Forklaring:
- `git remote -v` viser hvor repoet er koblet til på GitHub.
- Foreløpig peker `origin` til kursholders public repo.
- I del 2 skal du lage ditt eget private repo og bytte remote-oppsett.

## Rydd i den gamle ZIP-kopien

Før du klonet repoet, jobbet du i en ZIP-kopi av del 1.

Etter kloning kan du derfor se `01-terminal-wsl-vscode` to steder:

- `~/crash-course/01-terminal-wsl-vscode`
- `~/crash-course/nkom-crash-course-informatics/01-terminal-wsl-vscode`

Fra nå av skal du bruke mappen som ligger inne i det klonede repoet:

```text
~/crash-course/nkom-crash-course-informatics/01-terminal-wsl-vscode
```

For å unngå forvirring kan du gi den gamle ZIP-kopien et nytt navn.

Gå først tilbake til hovedmappen:

```bash
cd ~/crash-course
```

Gi så den gamle ZIP-kopien et tydelig navn:

```bash
mv 01-terminal-wsl-vscode 01-terminal-wsl-vscode-zip-kopi
```

Sjekk at du fortsatt har det klonede repoet:

```bash
ls
```

Du skal fortsatt se:

```text
nkom-crash-course-informatics
```

## Videre arbeid

Du er nå ferdig med ZIP-delen av kurset. Fra nå av skal vi jobbe i den klonede mappen:

```text
~/crash-course/nkom-crash-course-informatics
```

## Vanlige problemer

- Hvis `gh` ikke finnes, gå tilbake til oppgave 9.
- Hvis du ikke er logget inn, kjør `gh auth login`.
- Hvis repoet ikke finnes, sjekk at GitHub-brukernavn og repo-navn er riktig.
- Hvis mappen allerede finnes, kan det være fordi du har klonet repoet tidligere.

## Kontrollspørsmål

- Hva betyr det å klone et repo?
- Hvor ligger den klonede mappen?
- Hvilke tre hovedmapper ser du?
- Hva viser `git remote -v`?
