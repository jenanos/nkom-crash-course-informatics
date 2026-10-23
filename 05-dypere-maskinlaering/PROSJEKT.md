# Et eget maskinlæringseksperiment

Velg ett spørsmål og bruk kurskoden som utgangspunkt. Arbeid gjerne to sammen,
med én som kjører og én som forklarer det som skjer. Bytt roller underveis.

## Velg et spor

1. **Bilder:** Hjelper et CNN mer enn et MLP på samme CIFAR-10-utvalg? Lag samme
   trenings- og valideringsindekser for begge. Logg også parametre og treningstid.
2. **Overføringslæring:** Hvordan endres resultatet med 500, 2000 og 10 000
   treningsbilder? Hold valideringen fast og diskuter tidligere ImageNet-læring.
3. **Språk:** Hva endres ved 100, 300 og 1000 treningssteg? Sammenlign tap på faste
   valideringsvinduer og tekster ved samme temperatur. Skill språkform fra fakta.
4. **Reinforcement learning:** Hvordan påvirker utforsking læringen? Tren nye
   tabeller med ulike ε-oppsett og flere seeds, og evaluer uten videre læring.

## Planlegg før du trener

Bruk forsøksloggen til å beskrive hypotese, baseline, data og hvilke valg som holdes
faste. Begynn med det lille oppsettet slik at du kan kontrollere hele arbeidsflyten.
For modellvalg bruker du validering. Bestem hvordan du vil gjøre sluttesten før
resultatet foreligger. I rutenettet måler du dessuten en fast policy uten utforsking
og forklarer at et nytt kart er en annen oppgave.

## Vis hva du lærte

Lever en notatbok som kan kjøres fra Restart Kernel and Run All, en graf, noen
konkrete feil eller eksempler og en kort forsøkslogg. Vis utskrift med faktisk enhet
og pakkeversjoner. Forklar ett kodeavsnitt til en kollega med egne ord.

Et vellykket prosjekt kan vise at hypotesen var feil. Det viktige er at oppsettet
undersøker spørsmålet, at resultatet kan spores til kjøringen, og at konklusjonen
holder seg til det som ble målt.
