# Oppgave 5: Beslutningstrær

Et beslutningstre er en modell som tar avgjørelser steg for steg, som et flytskjema.

## Hva er et beslutningstre?

Tenk deg at du spiller «20 spørsmål»:
- Er passasjeren en kvinne? → Ja: trolig overlevde
- Er passasjeren i 1. eller 2. klasse? → Ja: trolig overlevde
- Er passasjeren under 10 år? → Ja: trolig overlevde

Et beslutningstre gjør akkurat dette. Det stiller ja/nei-spørsmål om features og følger grenene ned til et svar.

```
                Er det en kvinne?
               /                \
             Ja                  Nei
            /                      \
    Overlevde (77%)          Er det 1. klasse?
                              /            \
                            Ja              Nei
                           /                  \
                    Overlevde (37%)      Døde (83%)
```

## Hvordan lærer treet?

Modellen velger automatisk:
1. **Hvilke spørsmål** den skal stille (hvilken feature og hvilken verdi)
2. **I hvilken rekkefølge** (de viktigste spørsmålene først)

Den velger spørsmål som best deler dataene i grupper med like svar. Denne prosessen kalles å bygge treet.

## Nye begreper

- **Node:** et punkt i treet der et spørsmål stilles
- **Rot-node:** det aller første spørsmålet øverst
- **Blad:** et endepunkt der modellen gir sitt svar
- **Dybde:** hvor mange spørsmål treet stiller (flere = mer komplekst)
- **Overfitting:** når modellen pugger treningsdataene i stedet for å lære generelle mønstre

## Steg 1: Bygg et beslutningstre

Opprett en fil som heter `beslutningstre.py`:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
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

## Steg 2: Tren treet

```python
# Lag et beslutningstre med maks dybde 3
# (maks 3 spørsmål i rekke)
modell = DecisionTreeClassifier(max_depth=3, random_state=42)
modell.fit(X_train, y_train)

# Vis treet som tekst
print("Beslutningstreet:")
print(export_text(modell, feature_names=features))
```

**Forklaring:**
- `max_depth=3` begrenser treet til 3 nivåer med spørsmål
- `export_text` viser treet i tekstformat, slik at du kan lese det

## Steg 3: Evaluer

```python
# Prediksjoner og nøyaktighet
y_pred = modell.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\nNøyaktighet: {accuracy:.1%}")

# Forvirringsmatrise
cm = confusion_matrix(y_test, y_pred)
print(f"\nForvirringsmatrise:")
print(f"                  Gjettet: Døde  |  Gjettet: Overlevde")
print(f"  Faktisk døde:      {cm[0][0]:>4}        |      {cm[0][1]:>4}")
print(f"  Faktisk overlevde: {cm[1][0]:>4}        |      {cm[1][1]:>4}")
```

## Steg 4: Feature importance (hvor viktig er hver feature?)

```python
# Hvor viktig er hver feature?
print("\nFeature importance (hvor viktig er hver feature?):")
for feature, importance in zip(features, modell.feature_importances_):
    bar = "█" * int(importance * 30)
    print(f"  {feature:15s}: {importance:.3f} {bar}")
```

**Forklaring:**
Feature importance viser hvor mye hver feature bidrar til modellens avgjørelser. Tallene summerer til 1.0 (100 %).

## Steg 5: Overfitting — hva skjer uten dybdegrense?

```python
# Lag et tre UTEN dybdegrense
modell_dyp = DecisionTreeClassifier(random_state=42)  # Ingen max_depth!
modell_dyp.fit(X_train, y_train)

# Sjekk accuracy på trening vs. test
train_acc = accuracy_score(y_train, modell_dyp.predict(X_train))
test_acc = accuracy_score(y_test, modell_dyp.predict(X_test))

print(f"\n--- Overfitting-demonstrasjon ---")
print(f"Tre UTEN dybdegrense:")
print(f"  Accuracy på treningsdata: {train_acc:.1%}")
print(f"  Accuracy på testdata:     {test_acc:.1%}")
print(f"\nTre MED max_depth=3:")
print(f"  Accuracy på testdata:     {accuracy:.1%}")

if train_acc > test_acc + 0.1:
    print(f"\n⚠️  Stor forskjell mellom trening og test!")
    print(f"    Det betyr at modellen har OVERFITTET.")
    print(f"    Den har pugget treningsdataene i stedet for å lære generelle mønstre.")
```

**Forklaring av overfitting:**
- Hvis modellen er 100 % riktig på trening men mye dårligere på test, har den «pugget»
- Det er som å lære seg svarene på en prøve uten å forstå stoffet
- `max_depth` begrenser kompleksiteten og hindrer overfitting

## Hva har vi lært?

- Hvordan et beslutningstre tar avgjørelser (som et flytskjema)
- At treet automatisk finner de viktigste spørsmålene
- Hva overfitting er og hvorfor det er et problem
- Hvordan `max_depth` kan hindre overfitting
- Hva feature importance er

## Oppgave

1. Kjør `beslutningstre.py` og les treet. Hva er det første spørsmålet?
2. Hvilken feature er viktigst ifølge feature importance?
3. Prøv å endre `max_depth` til 5. Blir modellen bedre eller verre på testdata?
4. Hva skjer med overfitting når du øker dybden?

## Neste steg

I neste oppgave tar vi steget opp til nevrale nett — modeller inspirert av hjernen som kan lære enda mer komplekse mønstre.
