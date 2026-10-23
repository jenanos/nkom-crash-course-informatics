# Del 5 Maskinlæring fra teori til egne eksperimenter

I del 4 brukte du små ferdige modelloppskrifter på Titanic-data. Her åpner vi
oppskriften og ser hvordan et nevralt nett faktisk lærer. Du får trene egne
bilde- og språkmodeller og undersøke hva som skjer når du endrer ett valg.
Vi bygger på begrepene fra PBS og 3Blue1Brown, men forklarer koden fra starten.

Kurset har ingen fast tidsramme. Ta én notatbok om gangen, og del den gjerne over
flere møter. Begynn med små forsøk; gå videre til større GPU-forsøk når du kan
forklare hva den lille kjøringen gjør. Det er helt normalt å måtte repetere.

## Start her

1. Følg [oppsettet for Windows og WSL2](OPPSETT.md), og kjør installasjonssjekken.
2. Åpne [notatbok 00](notatboker/00-notatbok-og-tensorer.ipynb) i VS Code eller JupyterLab.
3. Les teksten før hver kodecelle. Gjett hva som skjer, kjør og sammenlign.
4. Noter ett spørsmål og én observasjon i [forsøksloggen](FORSOKSLOGG.md).

Du skal jobbe i en **egen kopi** av denne kursdelen, som forklart i oppsettet.
Da beholder du egne endringer og resultater når kursrepoet oppdateres.

## Læringsløpet

| Notatbok | Hva du gjør | Kobling til teorien | Utstyr |
| --- | --- | --- | --- |
| [00 Notatbok og tensorer](notatboker/00-notatbok-og-tensorer.ipynb) | Kjører celler, leser former og flytter tall | Input, batch og matriser | CPU |
| [01 Gradienter og læring](notatboker/01-gradienter-og-laering.ipynb) | Ser en vekt bevege seg og lærer en linje | Gradient descent, backpropagation, optimizer | CPU |
| [02 Bilder og treningsløkke](notatboker/02-bilder-og-treningslokke.ipynb) | Gjenkjenner klær med Fashion-MNIST | MLP, logits, softmax, cross entropy | CPU eller GPU |
| [03 Overtilpasning](notatboker/03-overtilpasning-og-eksperimenter.ipynb) | Sammenligner kontrollerte forsøk | Baseline, dropout, validering og sluttest | CPU eller GPU |
| [04 CNN og GPU](notatboker/04-cnn-og-gpu.ipynb) | Trener på CIFAR-10 og måler hastighet | Konvolusjon, aktiveringer, batch og VRAM | GPU anbefalt |
| [05 Overføringslæring](notatboker/05-overforingslaering.ipynb) | Trener nytt utgangslag på ResNet18 | Ferdigtrente representasjoner og frosne lag | GPU anbefalt |
| [06 Attention med tall](notatboker/06-attention-med-synlige-tall.ipynb) | Regner og tegner attention-kart | Q, K, V, softmax og kausal maske | CPU |
| [07 Liten språkmodell](notatboker/07-tren-en-liten-sprakmodell.ipynb) | Trener en transformer fra tilfeldige vekter | Token, embedding, posisjon, attention og generering | GPU anbefalt |
| [08 Reinforcement learning](notatboker/08-reinforcement-learning.ipynb) | Lærer en rute med Q-learning | Policy, belønning, utforsking og framtidig verdi | CPU |

Notatbok 00–03 gir grunnlaget for resten. Ta 04–05 som bildespor og 06–07 som
språkspor. Notatbok 08 er en roligere, selvstendig fordypning i reinforcement
learning. Avslutt med [et lite prosjekt](PROSJEKT.md). [Lærerveiledningen](LAERERVEILEDNING.md)
har forslag til stoppunkter og spørsmål.

## Hvorfor notatbøker her

Når vi lærer maskinlæring, er det nyttig å se inputbildet, modellens gjetning og
grafen sammen med koden som skapte dem. Derfor bruker vi Jupyter-notatbøker til
utforsking. Fra notatbok 03 bruker vi også [en vanlig Python-fil](startkode/kursverktoy.py)
til den treningsløkken vi allerede har lest. Det viser hvordan et eksperiment
kan vokse fra arbeidsbok til gjenbrukbar kode.

Hver kodebolk har forklaring, og øvelsene har forventninger, analogier, grafer og
kontrollspørsmål. Du trenger ikke forstå alle lag ved første gjennomlesning.
Målet er å kunne forklare hva som går inn, hva som kommer ut, hva som endres ved
trening, og hva resultatet faktisk gir grunnlag for å si.

## Hva en gaming-PC gir oss

En RTX 3080 med 10 GB VRAM gir et godt utgangspunkt for disse små modellene.
Startinnstillingene er bevisst forsiktige. GPU-fordypningen øker bilder, epoker
eller treningssteg; den krever ikke flere GPU-er. Tilgjengelig minne og treningstid
må måles på den enkelte maskinen. Kurset inneholder ingen lovnad om en bestemt
hastighet eller treffandel. CPU-deltakere kan gjøre små forsøk og sammenligne med
en kollegas større kjøring.

## Videre hjelp

- [Begrepskart](BEGREPER.md) knytter ord fra videoene til konkret kode.
- [Feilsøking](FEILSOKING.md) hjelper med kernel, CUDA og data.
- [Kilder og datasett](KILDER.md) peker til offisiell dokumentasjon og originalarbeider.
- [Kontroll av kursmaterialet](KONTROLL.md) beskriver hvordan notatbøkene kjøres og sjekkes.
