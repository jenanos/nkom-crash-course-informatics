# Oppgave 6: Kryptering og passord

Målet i denne oppgaven er å se at filer kan være låst med kryptering, og at et program kan be om flere passord før det slipper deg videre.

Du skal først dekryptere en ferdig kryptert fil. Inni filen ligger passordet du trenger for å kjøre programmet.

## Del A: Dekrypter filen

Stå i mappen `01-terminal-wsl-vscode`.

Installer `openssl` hvis det trengs:

```bash
sudo apt install openssl
```

Den krypterte filen ligger her:

```text
filer/hemmelig_passord.txt.enc
```

Den krypterte filen bruker AES-256-CBC. Da trenger vi både en AES-nøkkel og en IV.

AES-nøkkelen er 32 bytes. I OpenSSL skriver vi den som 64 heksadesimale tegn:

```text
9f1b8a4c6d3e2f10987a65b4c3d2e1f0aabbccddeeff00112233445566778899
```

IV-en er 16 bytes. I OpenSSL skriver vi den som 32 heksadesimale tegn:

```text
0f1e2d3c4b5a69788796a5b4c3d2e1f0
```

Kjør:

```bash
openssl enc -d -aes-256-cbc -K 9f1b8a4c6d3e2f10987a65b4c3d2e1f0aabbccddeeff00112233445566778899 -iv 0f1e2d3c4b5a69788796a5b4c3d2e1f0 -in filer/hemmelig_passord.txt.enc -out passord.txt
```

Forklaring:
- `enc -d` betyr at OpenSSL skal dekryptere
- `-aes-256-cbc` er krypteringsmetoden
- `-K` er AES-nøkkelen som heksadesimale tegn
- `-iv` er startverdien som trengs for CBC-modus
- `-in` er inputfilen
- `-out` er outputfilen

Les den dekrypterte filen:

```bash
cat passord.txt
```

## Del B: Bruk passordet i programmet

Kjør programmet:

```bash
python3 filer/innerste_rom.py
```

Programmet spør først etter et første passord. Der skal du bruke passordet du fant i den dekrypterte filen.

Deretter spør programmet etter et andre passord. Du kan trykke `Enter` for ikke noe passord.

Kom du inn? Dette er en film-referanse. Bruk ChatGPT om du trenger et hint og prøv eventuelt på nytt.

## Visste du at denne krypteringen er svært sikker?

AES-256 betyr at nøkkelen er 256 bits lang. Det gir enormt mange mulige nøkler: 2^256.

Det er så mange muligheter at det ikke er realistisk å prøve alle nøklene en etter en med dagens datamaskiner. Derfor brukes AES fortsatt i mange seriøse systemer.

Men sikker kryptering handler ikke bare om algoritmen. Nøkkelen må også holdes hemmelig. I denne oppgaven står nøkkelen i oppgaveteksten fordi du skal lære kommandoen. I et ekte system ville nøkkelen aldri ligget åpent i en kursfil.

## Refleksjon

- Hva var forskjellen på den krypterte filen og den dekrypterte filen?
- Hvorfor trengte du både en inputfil og en outputfil?
- Hva skjer hvis du skriver feil passord i programmet?
