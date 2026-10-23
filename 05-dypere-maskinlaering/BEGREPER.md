# Begreper fra video til kode

| Begrep | Betydning i kurset | Hvor du ser det |
| --- | --- | --- |
| Tensor | Tall med en form, som en tabell med flere akser | `bilder.shape` |
| Parameter | Et tall modellen kan lære, som en vekt eller bias | `modell.parameters()` |
| Hyperparameter | Et valg vi gjør utenfor vanlig vektlæring | Læringsrate, batch, arkitektur |
| Forward pass | Beregn en prediksjon med dagens vekter | `logits = modell(x)` |
| Loss | Ett tall som måler avvik etter en bestemt regel | `feilmaal(logits, fasit)` |
| Gradient | Lokal endring i loss ved liten parameterendring | `parameter.grad` |
| Backpropagation | Beregn gradienter bakover med kjederegelen | `feil.backward()` |
| Optimizer | Bruk gradientene til å oppdatere parametre | `optimizer.step()` |
| Læringsrate | Størrelsen på oppdateringene, sammen med optimizerens regel | `lr=0.001` |
| Batch | En pakke med eksempler | `DataLoader(..., batch_size=64)` |
| Epoke | En gjennomgang av hele det valgte treningsutvalget | Ytre løkke i bildeoppgavene |
| Steg | Én oppdatering etter ett batch | Indre løkke; språkmodellen teller steg |
| Logit | Rå poengsum før normalisering | Siste Linear-lag |
| Softmax | Gjør en liste skårer til positive tall som summerer til én | `logits.softmax(-1)` |
| Cross entropy | Straffer lav modellvekt på riktig kategori; ved én fasit er tapet −log(p for fasit) | `CrossEntropyLoss` tar logits direkte |
| Trening | Data som påvirker vektene gjennom gradienter | `trening_laster` |
| Validering | Data som brukes til modellvalg | `val_laster` |
| Test | Data som brukes etter at modellvalgene er tatt | Sluttesten i notatbok 03 |
| Overtilpasning | Modellen tilpasser treningsdata bedre enn nye data | Treningsfeil faller mens validering forverres |
| Dropout | Slå av tilfeldige aktiveringer i trening | `nn.Dropout(0.4)` |
| CNN | Nett med konvolusjonsfiltre som deles over romlige posisjoner | `nn.Conv2d` |
| Embedding | Lærbar tabell fra tokennummer til en vektor | `nn.Embedding` |
| Attention | Bland value-vektorer ut fra query/key-skårer | `softmax(QKᵀ / √d) V` |
| Kausal maske | Hindrer tilgang til senere posisjoner | Masken over diagonalen |
| Residual | Legg lagets endring til eksisterende representasjon | `x + blanding` |
| Policy | Regel for valg av handling | ε-greedy under Q-trening |
| Belønning | Tall miljøet gir etter en handling | `belonning` fra `flytt` |
| Q-verdi | Anslag for framtidig diskontert samlet belønning | `Q[tilstand, handling]` |
| Inferens | Bruk en modell uten å oppdatere vekter | `eval()` og `no_grad()` |
| Checkpoint | Lagrede vekter og eventuelt metadata/tilstand | `torch.save(...)` |

`eval()` er en lagmodus, ikke en egen målemetode. `no_grad()` hindrer sporing av
gradienter. Du trenger vanligvis begge ved evaluering. En seed gjør tilfeldighet
mer kontrollerbar, men garanterer ikke identiske resultater på tvers av maskiner.
