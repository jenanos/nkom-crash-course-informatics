# Veiledning for den som holder kurset

Deltakerne har sett teori om nevrale nett, men har lite erfaring med kode. Gi plass
til å lese former, se mellomresultater og forklare for hverandre. Bruk ferdig kode
som lesestoff først, deretter små endringer. Det er ikke nødvendig å skrive en
transformer fra hukommelsen for å ha forstått noe viktig om den.

## Før dere møtes

Kjør installasjonssjekken på hver maskin, også på gaming-PC-ene som skal trene.
Avklar om alle kjører selv eller om noen gjør små forsøk og sammenligner med
større kjøringer fra en kollega. Last ned Fashion-MNIST, CIFAR-10 og ResNet-vekter
på forhånd. La hver deltaker bruke egen kopi av kursdelen, som i oppsettet.

## Et arbeidsmønster som kan gjentas

1. Les forklaringen og be deltakerne gjette utskrift, form eller kurve.
2. Kjør én celle og sammenlign med forventningen.
3. La en deltaker forklare hva den viktigste linjen gjør.
4. Endre ett valg, restart ved behov, og noter observasjonen.
5. Stopp når deltakerne kan svare på kontrollspørsmålet uten å lese fasiten.

Gå tilbake til en mindre tensor eller ett batch når forklaringen blir uklar.
Notatbok 07 kan med fordel deles i data, modell og trening over flere møter.

## Stoppunkter

| Etter notatbok | Be deltakeren vise og forklare |
| --- | --- |
| 00 | Batchaksen og hva en kernel husker |
| 01 | Hvor gradienten beregnes, og hvor vekten endres |
| 02 | Ett bilde gjennom hele løkken og hvorfor output har ti logits |
| 03 | Modellvalget før testen og hva overtilpasning ser ut som |
| 04 | Formen etter hvert lag og forskjellen på benchmark og epoketid |
| 05 | Hvilke parametre som trenes og hvorfor BatchNorm trenger egen omtanke |
| 06 | Én attention-rad og hvorfor første kausale rad bare ser seg selv |
| 07 | Ett input/mål-par, masken og generering ett tegn om gangen |
| 08 | Ett Q-mål, terminaltilstanden og forskjellen på utforsking og evaluering |

## Knytt tilbake til videoene

Vis gradienten til én vekt før dere går til tusenvis av parametre. Når dere møter
cross entropy, sammenlign to tenkte modeller som begge gjetter feil, men gir fasit
henholdsvis 0,4 og 0,001. Den siste straffes mer fordi den ga riktig svar svært lav
sannsynlighet. Ved attention kan deltakerne endre Q, K og V hver for seg før de
leser klassen i språkmodellen.

I del 4 ble backpropagation brukt om vekttilpasningen samlet. Presiser nå at
`backward()` beregner gradienter, mens optimizer oppdaterer vektene. Ikke krev at
deltakerne kan utlede alle formlene; krev at de kan følge regnestykket på ett lite eksempel.

## Typiske feiltolkninger

Høy treffandel på trening er ikke det samme som god generalisering. Et softmax-tall
på 90 % er ikke i seg selv dokumentasjon på kalibrert sikkerhet. En ferdigtrent
modell har allerede brukt et stort tidligere treningsbudsjett. Attention-kart
viser vekter, ikke en full årsaksforklaring. Språk som ligner treningsmeldingene
beviser ikke at modellen kjenner virkelige forhold. En høy belønning kan skyldes
at belønningsregelen tillater en uønsket strategi.

## Når dere vil gå dypere

For bildeoppgavene kan dere undersøke dataaugmentering, normalisering og
finjustering. For språkmodellen kan dere prøve ekte tekst med tydelig kilde og
rettigheter, og splitte dokumenter før vinduer. For reinforcement learning kan
neste trinn være et enkelt DQN-eksempel med replay-buffer og målnettverk.
Disse er nye eksperimenter; la forståelsen av grunnløkken avgjøre tempoet.
