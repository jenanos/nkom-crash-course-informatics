# Oppgave 4: Logistisk regresjon (klassifisering)

Nå skal vi løse det egentlige Titanic-problemet: forutsi om en passasjer overlevde eller ikke. Dette er et **klassifiseringsproblem** fordi svaret er enten 0 (døde) eller 1 (overlevde).

## Hva er logistisk regresjon?

Til tross for navnet er logistisk regresjon brukt til **klassifisering**, ikke regresjon.

Den fungerer slik:
1. Først beregner den en vektet sum av features (som lineær regresjon)
2. Deretter presser den resultatet gjennom en **sigmoid-funksjon** som gir et tall mellom 0 og 1
3. Dette tallet tolkes som en **sannsynlighet**

```
sannsynlighet = sigmoid(a₁*alder + a₂*klasse + a₃*kjønn + ... + b)
```

Sigmoid-funksjonen ser ut som en S-kurve:
- Input nær -∞ → output nær 0
- Input nær +∞ → output nær 1
- Input = 0 → output = 0.5

Hvis sannsynligheten er over 0.5, sier modellen «overlevde». Ellers «døde».

## Nye begreper

- **Sigmoid:** en funksjon som «klemmer» tall inn mellom 0 og 1
- **Sannsynlighet:** modellens sikkerhet på svaret (0.9 = 90 % sikker)
- **Accuracy (nøyaktighet):** andelen riktige svar av totalt antall
- **Encoding:** å gjøre tekst om til tall (maskinen forstår bare tall)

## Steg 1: Forbered dataene

Opprett en fil som heter `klassifisering.py`:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Last inn data
df = pd.read_csv("04-maskinlaering/data/titanic.csv")

# Fjern rader med manglende verdier i kolonnene vi bruker
df = df.dropna(subset=["Age", "Fare", "Embarked"])

# Gjør kjønn om til tall (encoding)
# male = 0, female = 1
df["Sex_encoded"] = df["Sex"].map({"male": 0, "female": 1})

print("Slik ser encoded kjønn ut:")
print(df[["Sex", "Sex_encoded"]].head())
```

**Forklaring:**
Maskinen kan ikke lese tekst som «male» eller «female». Vi må gjøre det om til tall. Dette kalles **encoding**.

## Steg 2: Velg features og del data

```python
# Velg features (hva modellen ser) og target (hva den skal gjette)
features = ["Pclass", "Sex_encoded", "Age", "Fare"]
X = df[features]
y = df["Survived"]

# Del i trening og test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nFeatures: {features}")
print(f"Target: Survived")
print(f"Treningssett: {len(X_train)} rader")
print(f"Testsett: {len(X_test)} rader")
```

## Steg 3: Tren modellen

```python
# Lag og tren modellen
modell = LogisticRegression(max_iter=1000)
modell.fit(X_train, y_train)

# Vis vektene modellen lærte
print("\nHva modellen lærte (vekter per feature):")
for feature, vekt in zip(features, modell.coef_[0]):
    print(f"  {feature}: {vekt:.3f}")
```

**Forklaring:**
- `max_iter=1000` gir modellen nok tid til å lære
- Vektene viser hvor viktig hver feature er:
  - Positiv vekt → øker sjansen for å overleve
  - Negativ vekt → minsker sjansen for å overleve

## Steg 4: Evaluer modellen

```python
# Gjør prediksjoner på testdata
y_pred = modell.predict(X_test)

# Beregn nøyaktighet
accuracy = accuracy_score(y_test, y_pred)
print(f"\nNøyaktighet (accuracy): {accuracy:.1%}")
print(f"Det betyr at modellen gjetter riktig {accuracy:.1%} av gangene.")

# Confusion matrix (forvirringsmatrise)
cm = confusion_matrix(y_test, y_pred)
print(f"\nForvirringsmatrise:")
print(f"                  Gjettet: Døde  |  Gjettet: Overlevde")
print(f"  Faktisk døde:      {cm[0][0]:>4}        |      {cm[0][1]:>4}")
print(f"  Faktisk overlevde: {cm[1][0]:>4}        |      {cm[1][1]:>4}")
```

**Forklaring av forvirringsmatrisen:**
- Øverst til venstre: modellen sa «døde» og personen døde faktisk (riktig!)
- Øverst til høyre: modellen sa «overlevde» men personen døde (feil!)
- Nederst til venstre: modellen sa «døde» men personen overlevde (feil!)
- Nederst til høyre: modellen sa «overlevde» og personen overlevde (riktig!)

## Steg 5: Prøv med egne passasjerer

```python
import numpy as np

# Lag en «ny» passasjer og se hva modellen sier
# [Pclass, Sex_encoded, Age, Fare]
ny_passasjer = [[1, 1, 25, 70.0]]  # Kvinne, 25 år, 1. klasse, dyr billett
sannsynlighet = modell.predict_proba(ny_passasjer)[0]
prediksjon = modell.predict(ny_passasjer)[0]

print(f"\nNy passasjer: Kvinne, 25 år, 1. klasse, billett 70 kr")
print(f"Sannsynlighet for å dø: {sannsynlighet[0]:.1%}")
print(f"Sannsynlighet for å overleve: {sannsynlighet[1]:.1%}")
print(f"Modellens gjetning: {'Overlevde' if prediksjon == 1 else 'Døde'}")

# Prøv en annen passasjer
ny_passasjer2 = [[3, 0, 30, 8.0]]  # Mann, 30 år, 3. klasse, billig billett
sannsynlighet2 = modell.predict_proba(ny_passasjer2)[0]
prediksjon2 = modell.predict(ny_passasjer2)[0]

print(f"\nNy passasjer: Mann, 30 år, 3. klasse, billett 8 kr")
print(f"Sannsynlighet for å dø: {sannsynlighet2[0]:.1%}")
print(f"Sannsynlighet for å overleve: {sannsynlighet2[1]:.1%}")
print(f"Modellens gjetning: {'Overlevde' if prediksjon2 == 1 else 'Døde'}")
```

## Hva har vi lært?

- Forskjellen mellom regresjon og klassifisering
- Hva logistisk regresjon er og hvordan den bruker sigmoid
- Hvorfor vi må encode tekst til tall
- Hva accuracy og confusion matrix betyr
- Hvordan man kan gjøre prediksjoner på nye data

## Oppgave

1. Kjør `klassifisering.py` og se på resultatene.
2. Hvilken feature har størst påvirkning? (Hint: se på vektene)
3. Lag en tredje «ny passasjer» med dine egne verdier. Hva sier modellen?
4. Hva skjer med accuracy hvis du fjerner `Sex_encoded` fra features?

## Neste steg

Logistisk regresjon er bra, men den kan bare lære rette skillelinjer. I neste oppgave prøver vi beslutningstrær, som kan lære mer komplekse mønstre.
