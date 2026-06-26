# Oppgave 6: Nevrale nett

Nå tar vi steget opp til nevrale nett. Dette er modellene som ligger bak mye av det vi kaller «kunstig intelligens» i dag.

## Hva er et nevralt nett?

Et nevralt nett er inspirert av hjernen. Det består av:
- **Nevroner:** små enheter som tar imot tall, gjør en beregning, og sender resultatet videre
- **Lag:** nevroner organisert i lag som kommer etter hverandre
- **Vekter:** tall som bestemmer hvor viktig hver forbindelse er

Strukturen ser slik ut:

```
Input-lag        Skjult lag       Output-lag
(features)       (beregning)      (svar)

  Alder ──┐
           ├──→ [Nevron 1] ──┐
  Kjønn ──┤                   ├──→ [Overlevde?]
           ├──→ [Nevron 2] ──┘
  Klasse ──┤
           ├──→ [Nevron 3]
  Pris  ──┘
```

### Hvordan lærer det?

1. Data sendes inn i input-laget (features)
2. Hvert nevron ganger inputen med vekter, summerer, og bruker en aktiveringsfunksjon
3. Resultatet sendes videre til neste lag
4. Til slutt gir output-laget et svar
5. Feilen beregnes (hvor mye bommet det?)
6. Vektene justeres litt for å redusere feilen (**backpropagation**)
7. Steg 1–6 gjentas mange ganger (**epoker**)

### Aktiveringsfunksjon

Uten aktiveringsfunksjoner ville et nevralt nett bare vært lineær regresjon med ekstra steg. Aktiveringsfunksjonen gjør at nettverket kan lære **ikke-lineære** mønstre.

Den vanligste heter **ReLU** og gjør noe veldig enkelt:
- Hvis input > 0: send input videre
- Hvis input ≤ 0: send 0

## Nye begreper

- **Epoke:** én runde gjennom alle treningsdataene
- **Backpropagation:** prosessen der nettverket justerer vektene basert på feilen
- **Læringsrate:** hvor store steg modellen tar når den justerer vektene
- **Skjult lag:** lag mellom input og output som gjør beregninger
- **Aktiveringsfunksjon:** funksjon som gjør at nettverket kan lære komplekse mønstre

## Steg 1: Forbered data med skalering

Opprett en fil som heter `nevralt_nett.py`:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

# Last inn og forbered data
df = pd.read_csv("04-maskinlaering/data/titanic.csv")
df = df.dropna(subset=["Age", "Fare", "Embarked"])
df["Sex_encoded"] = df["Sex"].map({"male": 0, "female": 1})

# Features og target
features = ["Pclass", "Sex_encoded", "Age", "Fare"]
X = df[features]
y = df["Survived"]

# Del i trening og test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

### Viktig: Skalering!

Nevrale nett fungerer best når alle features har lignende størrelse. Alder (0–80) og billettpris (0–500) har veldig forskjellig skala. Vi bruker **StandardScaler** for å fikse dette:

```python
# Skaler features til gjennomsnitt 0 og standardavvik 1
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Før skalering (første rad):")
print(f"  {X_train.iloc[0].values}")
print("Etter skalering (første rad):")
print(f"  {X_train_scaled[0]}")
```

**Forklaring:**
- `fit_transform` beregner gjennomsnitt/standardavvik fra trening og skalerer
- `transform` bruker SAMME skalering på testdata (viktig: aldri fit på testdata!)

## Steg 2: Bygg og tren nettverket

```python
# Lag et nevralt nett
# - hidden_layer_sizes=(8, 4) betyr: 2 skjulte lag med 8 og 4 nevroner
# - max_iter=500 betyr: maks 500 epoker
# - random_state=42 gir samme resultat hver gang
modell = MLPClassifier(
    hidden_layer_sizes=(8, 4),
    max_iter=500,
    random_state=42,
    activation="relu"
)

# Tren nettverket
modell.fit(X_train_scaled, y_train)

print(f"\nNettverkstruktur:")
print(f"  Input-lag: {len(features)} nevroner (en per feature)")
print(f"  Skjult lag 1: 8 nevroner")
print(f"  Skjult lag 2: 4 nevroner")
print(f"  Output-lag: 1 nevron (overlevde ja/nei)")
print(f"  Antall epoker brukt: {modell.n_iter_}")
```

**Forklaring:**
- `MLPClassifier` = Multi-Layer Perceptron, et standard nevralt nett
- `hidden_layer_sizes=(8, 4)` definerer arkitekturen
- `activation="relu"` bruker ReLU aktiveringsfunksjon
- Modellen kjører på CPU og trener på sekunder med dette lille datasettet

## Steg 3: Evaluer

```python
# Prediksjoner
y_pred = modell.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print(f"\nNøyaktighet: {accuracy:.1%}")

# Forvirringsmatrise
cm = confusion_matrix(y_test, y_pred)
print(f"\nForvirringsmatrise:")
print(f"                  Gjettet: Døde  |  Gjettet: Overlevde")
print(f"  Faktisk døde:      {cm[0][0]:>4}        |      {cm[0][1]:>4}")
print(f"  Faktisk overlevde: {cm[1][0]:>4}        |      {cm[1][1]:>4}")
```

## Steg 4: Eksperimenter med arkitekturen

```python
# Prøv forskjellige nettverksstørrelser
print("\n--- Eksperiment: forskjellige nettverksstørrelser ---")

arkitekturer = [
    (4,),          # 1 skjult lag med 4 nevroner
    (8, 4),        # 2 skjulte lag
    (16, 8, 4),   # 3 skjulte lag
]

for arkitektur in arkitekturer:
    m = MLPClassifier(
        hidden_layer_sizes=arkitektur,
        max_iter=500,
        random_state=42
    )
    m.fit(X_train_scaled, y_train)
    acc = accuracy_score(y_test, m.predict(X_test_scaled))
    lag_tekst = " → ".join([str(n) for n in arkitektur])
    print(f"  Lag [{lag_tekst}]: accuracy = {acc:.1%}")
```

## Steg 5: Se på treningsprosessen

```python
import matplotlib.pyplot as plt

# Tren en ny modell og spor feilen over tid
modell2 = MLPClassifier(
    hidden_layer_sizes=(8, 4),
    max_iter=1,          # Bare 1 epoke om gangen
    warm_start=True,     # Fortsett der vi slapp
    random_state=42
)

feil_over_tid = []
for i in range(200):
    modell2.fit(X_train_scaled, y_train)
    feil_over_tid.append(modell2.loss_)

plt.plot(feil_over_tid)
plt.xlabel("Epoke")
plt.ylabel("Feil (loss)")
plt.title("Hvordan nettverket lærer over tid")
plt.savefig("laering_over_tid.png")
plt.close()
print("\nGraf lagret som laering_over_tid.png")
print("Du kan se at feilen synker over tid — nettverket lærer!")
```

## Hva har vi lært?

- Hva et nevralt nett er (lag av nevroner med vekter)
- Hvorfor skalering er viktig
- Hva aktiveringsfunksjoner gjør
- Hva epoker og backpropagation betyr
- At nettverksstørrelse påvirker resultatet
- At et nevralt nett kan gi bedre resultater enn enklere modeller

## Oppgave

1. Kjør `nevralt_nett.py` og se på resultatene.
2. Hvilken arkitektur ga best accuracy?
3. Se på grafen `laering_over_tid.png`. Når slutter nettverket å forbedre seg?
4. Prøv å legge til flere features (f.eks. SibSp, Parch). Blir modellen bedre?

## Neste steg

I siste oppgave skal vi sammenligne alle modellene vi har bygget og lære hvordan man velger den beste.
