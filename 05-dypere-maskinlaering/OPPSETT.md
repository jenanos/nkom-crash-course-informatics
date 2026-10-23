# Oppsett på Windows og WSL2

Vi bruker Python i WSL2 og lar Windows-driveren gi tilgang til NVIDIA-GPU-en.
Gjør installasjonen på maskinen som faktisk skal trene. En kurslaptop kan bruke
CPU, mens en gaming-PC kjører de større forsøkene med sin egen kopi av filene.

## Kontroller WSL og GPU

Åpne **PowerShell i Windows**, og skriv:

```powershell
wsl --list --verbose
wsl --update
```

Ubuntu-distribusjonen skal stå med versjon **2**. Del 1 viser grunnoppsettet for WSL.
Installer eller oppdater NVIDIA-driveren i **Windows** hvis gaming-PC-en trenger det.
Åpne deretter **Ubuntu-terminalen i WSL**, og skriv:

```bash
nvidia-smi
python3 --version
```

På GPU-maskinen skal `nvidia-smi` vise skjermkort og driver. CPU-maskinen trenger
ikke denne kommandoen. Vi bruker Python 3.12 som utgangspunkt; sjekk støttede
Python-versjoner i PyTorchs installasjonsvelger hvis du bruker noe annet.

Installer ikke en Linux-skjermdriver inne i WSL. NVIDIA sier uttrykkelig at
Windows-driveren gjør GPU-en tilgjengelig der. Vanlige ferdigbygde PyTorch-pakker
krever heller ikke at vi kompilerer et eget CUDA Toolkit for disse øvelsene.
Se [NVIDIAs WSL-veiledning](https://docs.nvidia.com/cuda/wsl-user-guide/index.html).

## Lag en egen arbeidsmappe

Følgende er **terminalkommandoer i Ubuntu/WSL**, ikke Python-kode.
Her antar vi at kursrepoet er klonet i hjemmemappen. Tilpass kildestien hvis du
har lagt repoet et annet sted. Velg et annet mappenavn hvis `nkom-del5` allerede finnes.

```bash
mkdir ~/nkom-del5
cp -r ~/nkom-crash-course-informatics/05-dypere-maskinlaering/. ~/nkom-del5/
cd ~/nkom-del5
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

`mkdir` lager arbeidsmappen. `cp -r` kopierer kursdelen med undermapper.
`.venv` er et eget Python-miljø for kurset. `source` aktiverer det i denne terminalen.
`python -m pip` sørger for at pakkene installeres til denne Python-tolkeren.
Hvis `venv` mangler, installer `python3-venv` i Ubuntu som i del 1 og prøv igjen.

## Installer PyTorch til riktig maskin

Åpne [PyTorchs installasjonsvelger](https://pytorch.org/get-started/locally/).
Velg **Stable**, **Linux**, **Pip** og **Python**. Vi velger Linux fordi Python
kjører i WSL, selv om selve PC-en har Windows.

På NVIDIA-maskinen velger du et CUDA-alternativ som støttes av driveren din.
Kopier kommandoen velgeren gir, og kjør den i den aktiverte WSL-terminalen.
Bytt eventuelt innledende `pip3` med `python -m pip`, og behold pakker og
`--index-url` fra velgeren. Installer `torch` og `torchvision` sammen fra samme
valg slik at de passer sammen. På CPU-maskinen velger du **CPU**.

`CUDA Version` i `nvidia-smi` beskriver driverens CUDA-støtte, ikke hvilken
PyTorch-pakke som er installert. Derfor har vi en egen kjørbar kontroll nedenfor.
Hvis en nyere CUDA-pakke krever nyere driver, kan du oppdatere Windows-driveren
eller velge en støttet pakke fra PyTorchs offisielle installasjonsoversikt.

Installer deretter resten i samme WSL-terminal:

```bash
python -m pip install -r requirements.txt
python startkode/sjekk_installasjon.py
```

På GPU-maskinen krever du også en vellykket GPU-sjekk:

```bash
python startkode/sjekk_installasjon.py --krev-gpu
```

Programmet skriver ut Python-sti og pakkeversjoner, prøver en liten beregning og
avslutter med feilstatus hvis nødvendige sjekker feiler. `--krev-gpu` hindrer at
en GPU-maskin stille fortsetter på CPU. CPU-deltakere bruker første kommando.

## Åpne notatbøkene

Registrer miljøet som en Jupyter-kernel:

```bash
python -m ipykernel install --user --name nkom-del5 --display-name "Python (Nkom del 5)"
code .
```

I VS Code skal vinduet være koblet til **WSL**. Installer utvidelsene **Python** og
**Jupyter** i WSL når VS Code tilbyr det. Åpne `notatboker/00-notatbok-og-tensorer.ipynb`.
Velg **Select Kernel → Python (Nkom del 5)**. Hvis navnet ikke vises, velg Python-miljøet
med sti som slutter på `nkom-del5/.venv/bin/python`.

Et alternativ er JupyterLab i nettleseren. Start dette i den aktiverte WSL-terminalen:

```bash
python -m jupyterlab
```

Åpne den lokale lenken som terminalen viser, og velg samme kernel. Python kjører
fortsatt i WSL på din egen maskin; nettleseren er bare brukerflaten. Stopp serveren
med Ctrl+C i terminalen når du er ferdig.

## Første kjøring og lagring

En kodecelle kjøres med **Shift+Enter**. Stjernen eller kjøreindikatoren betyr at
Python arbeider. Bruk **Interrupt Kernel** for å avbryte, og **Restart Kernel and
Run All** for et nytt, sammenhengende forsøk. Lagre notatboken med Ctrl+S.

Ved ny terminal må du aktivere miljøet igjen:

```bash
cd ~/nkom-del5
source .venv/bin/activate
```

Datasett lastes ned til `data/` ved første bruk. ResNet-vekter lagres i PyTorchs
vanlige cache, normalt `~/.cache/torch/hub/checkpoints/`. Last gjerne ned før
kursøkten. Sett av noen GB diskplass til pakker, data og resultater; CUDA-pakker
kan være store. Hold prosjektet i WSL-hjemmemappen for enkel filtilgang under trening.

For å registrere det fungerende miljøet kan du lagre pakkeversjonene:

```bash
python -m pip freeze > pakkeversjoner.txt
```

Noter også installasjonskommandoen fra PyTorch-velgeren og driverversjonen.
En versjonsliste alene beskriver ikke GPU-driveren eller hvilket pakkeindeksvalg du brukte.
