# Oppgave 7: Sammenlign modellene

Nå har vi bygget tre forskjellige modeller for det samme problemet. I denne oppgaven setter vi dem opp mot hverandre og lærer hvordan man velger den beste.

## Hvordan velger man modell?

Det finnes ingen «beste modell» for alle problemer. Valget avhenger av:

1. **Nøyaktighet:** Hvor ofte gjetter modellen riktig?
2. **Enkelhet:** Er modellen lett å forstå og forklare?
3. **Hastighet:** Hvor lang tid tar trening og prediksjon?
4. **Overfitting:** Generaliserer modellen godt til nye data?

## Steg 1: Bygg alle modeller

Opprett en fil som heter `sammenlign.py`:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import time

# Last inn og forbered data
df = pd.read_csv("04-maskinlaering/data/titanic.csv")
df = df.dropna(subset=["Age", "Fare", "Embarked"])
df["Sex_encoded"] = df["Sex"].map({"male": 0, "female": 1})

features = ["Pclass", "Sex_encoded", "Age", "Fare"]
X = df[features]
y = df["Survived"]

# Del i trening og test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Skaler for nevrale nett
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

## Steg 2: Tren og mål alle modeller

```python
# Definer modellene
modeller = {
    "Logistisk regresjon": LogisticRegression(max_iter=1000),
    "Beslutningstre (depth=3)": DecisionTreeClassifier(max_depth=3, random_state=42),
    "Beslutningstre (depth=5)": DecisionTreeClassifier(max_depth=5, random_state=42),
    "Nevralt nett (8,4)": MLPClassifier(hidden_layer_sizes=(8, 4), max_iter=500, random_state=42),
    "Nevralt nett (16,8,4)": MLPClassifier(hidden_layer_sizes=(16, 8, 4), max_iter=500, random_state=42),
}

print("=" * 60)
print("SAMMENLIGNING AV MODELLER")
print("=" * 60)

resultater = []

for navn, modell in modeller.items():
    # Bruk skalerte data for nevrale nett, vanlige for andre
    if "Nevralt" in navn:
        X_tr, X_te = X_train_scaled, X_test_scaled
    else:
        X_tr, X_te = X_train, X_test
    
    # Mål treningstid
    start = time.time()
    modell.fit(X_tr, y_train)
    treningstid = time.time() - start
    
    # Mål prediksjon
    y_pred = modell.predict(X_te)
    accuracy = accuracy_score(y_test, y_pred)
    
    # Lagre resultater
    resultater.append({
        "Modell": navn,
        "Accuracy": accuracy,
        "Tid (sek)": treningstid
    })
    
    print(f"\n{'─' * 40}")
    print(f"  {navn}")
    print(f"  Accuracy: {accuracy:.1%}")
    print(f"  Treningstid: {treningstid:.4f} sekunder")
```

## Steg 3: Vis resultater i en tabell

```python
# Lag en pen oppsummeringstabell
print(f"\n{'=' * 60}")
print(f"OPPSUMMERING")
print(f"{'=' * 60}")
print(f"{'Modell':<30} {'Accuracy':<12} {'Tid':<10}")
print(f"{'─' * 52}")

for r in sorted(resultater, key=lambda x: x["Accuracy"], reverse=True):
    print(f"{r['Modell']:<30} {r['Accuracy']:<12.1%} {r['Tid (sek)']:<10.4f}")

beste = max(resultater, key=lambda x: x["Accuracy"])
print(f"\n🏆 Beste modell: {beste['Modell']} ({beste['Accuracy']:.1%})")
```

## Steg 4: Detaljert rapport for beste modell

```python
# Classification report for beste modell
print(f"\n{'=' * 60}")
print(f"DETALJERT RAPPORT: {beste['Modell']}")
print(f"{'=' * 60}")

# Finn og kjør beste modell på nytt for rapport
for navn, modell in modeller.items():
    if navn == beste["Modell"]:
        if "Nevralt" in navn:
            y_pred_best = modell.predict(X_test_scaled)
        else:
            y_pred_best = modell.predict(X_test)
        break

print(classification_report(
    y_test, y_pred_best,
    target_names=["Døde", "Overlevde"]
))
```

**Forklaring av classification_report:**
- **Precision:** Av alle modellen sa «overlevde», hvor mange overlevde faktisk?
- **Recall:** Av alle som faktisk overlevde, hvor mange fant modellen?
- **F1-score:** Et balansert mål som kombinerer precision og recall

## Steg 5: Visualiser sammenligningen

```python
import matplotlib.pyplot as plt

# Søylediagram over accuracy
navn_list = [r["Modell"] for r in resultater]
acc_list = [r["Accuracy"] for r in resultater]

plt.figure(figsize=(10, 5))
plt.barh(navn_list, acc_list, color="steelblue")
plt.xlabel("Accuracy")
plt.title("Sammenligning av modeller")
plt.xlim(0, 1)
for i, acc in enumerate(acc_list):
    plt.text(acc + 0.01, i, f"{acc:.1%}", va="center")
plt.tight_layout()
plt.savefig("modell_sammenligning.png")
plt.close()
print("\nGraf lagret som modell_sammenligning.png")
```

## Diskusjon: Hvilken modell bør du velge?

| Situasjon | Anbefalt modell |
|-----------|-----------------|
| Du må forklare modellen til noen | Beslutningstre |
| Du vil ha best mulig accuracy | Nevralt nett (eller prøv flere) |
| Du har veldig lite data | Logistisk regresjon |
| Du trenger rask trening og prediksjon | Logistisk regresjon |
| Data har komplekse, ikke-lineære mønstre | Nevralt nett |

## Hva har vi lært i hele del 4?

La oss oppsummere hele reisen:

1. **Hva maskinlæring er:** La maskinen finne mønstre i data
2. **Utforsking av data:** Forstå dataene før du bygger modeller
3. **Lineær regresjon:** Den enkleste modellen — en rett linje
4. **Logistisk regresjon:** Klassifisering med sannsynligheter
5. **Beslutningstrær:** Ja/nei-spørsmål i sekvens, feature importance, overfitting
6. **Nevrale nett:** Lag av nevroner, skalering, epoker
7. **Modellvalg:** Sammenligne og velge rett modell for problemet

## Bonusoppgave

Hvis du vil utfordre deg selv:

1. Legg til flere features (SibSp, Parch) og se om resultatene endres
2. Prøv å lage en encoding av «Embarked» (S=0, C=1, Q=2) og bruk den
3. Kan du finne en kombinasjon av features og modell som gir over 85 % accuracy?

## Gratulerer! 🎉

Du har nå lært grunnleggende maskinlæring. Du kan:
- Forberede data for maskinlæring
- Bygge og trene modeller
- Evaluere og sammenligne modeller
- Forstå forskjellen mellom regresjon og klassifisering
- Forklare hva et nevralt nett er

Dette er et solid fundament for å forstå hvordan maskinlæring brukes i virkeligheten — enten du skal vurdere AI-løsninger, snakke med utviklere, eller eksperimentere videre på egen hånd.
