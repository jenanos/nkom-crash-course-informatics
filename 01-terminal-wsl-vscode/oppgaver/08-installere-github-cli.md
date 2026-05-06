# Oppgave 8: Installere GitHub CLI

Målet i denne oppgaven er at du skal installere GitHub CLI. GitHub CLI er GitHubs kommandolinjeverktøy. Vi trenger det for å logge inn på GitHub fra terminalen og hente resten av kursrepoet.

Kort forklart:
- **GitHub** er en tjeneste for lagring og samarbeid om kode.
- **git** er verktøyet som holder orden på versjonene.
- **GitHub CLI**, kommandoen `gh`, gjør at vi kan bruke GitHub fra terminalen.

Dokumentasjon:
- GitHub CLI quickstart: <https://docs.github.com/en/github-cli/github-cli/quickstart>
- GitHub CLI installasjon for Linux: <https://github.com/cli/cli/blob/trunk/docs/install_linux.md>

## Sjekk først om `gh` allerede er installert

Dette skal du skrive i Ubuntu/WSL-terminalen.

```bash
gh --version
```

Forklaring:
- Hvis dette viser en versjon, er GitHub CLI allerede installert.
- Hvis terminalen sier at kommandoen ikke finnes, må du installere GitHub CLI.

## Installer GitHub CLI hvis det trengs

Skriv dette i Ubuntu/WSL-terminalen:

```bash
sudo apt update
sudo apt install gh
```

Når installasjonen er ferdig, sjekk igjen:

```bash
gh --version
```

Merknad:

Hvis dette ikke fungerer, bruk den offisielle installasjonsdokumentasjonen for Linux. Kursholder hjelper deg i rommet.

## Logg inn i GitHub

Når `gh` er installert, logger du inn med:

```bash
gh auth login
```

Når du får spørsmål i terminalen, kan du normalt velge:

- `GitHub.com`
- `HTTPS`
- `Yes, authenticate Git with your GitHub credentials`
- `Login with a web browser`

Forklaring:
- Terminalen kan vise en kode og be deg åpne nettleseren.
- Følg instruksjonene på skjermen steg for steg.
- Hvis du blir sendt til en nettside, logger du inn der og skriver inn koden hvis GitHub ber om det.

Dokumentasjon for innlogging:
- <https://cli.github.com/manual/gh_auth_login>

## Sjekk at du er logget inn

Skriv:

```bash
gh auth status
```

Forklaring:
- Denne kommandoen viser om GitHub CLI er logget inn.
- Hvis du ser informasjon om brukeren din og GitHub, er innloggingen som regel i orden.

## Vanlige problemer

- Hvis nettleseren ikke åpner seg, kopier lenken manuelt.
- Hvis du ikke har GitHub-bruker, må du opprette en på <https://github.com/>.
- Hvis du får spørsmål om passord eller kode, følg instruksjonene fra GitHub.
- Hvis du bruker jobb-PC, kan sikkerhetsinnstillinger påvirke innloggingen.

## Kontrollspørsmål

- Hva er forskjellen på `git` og `gh`?
- Hva viser `gh --version`?
- Hva viser `gh auth status`?
