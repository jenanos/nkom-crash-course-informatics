import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, confusion_matrix

# Last inn og forbered data
datasett_sti = Path(__file__).resolve().parent.parent / "data" / "titanic.csv"
df = pd.read_csv(datasett_sti)
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

# Lag et beslutningstre med maks dybde 3
# (maks 3 spørsmål i rekke)
modell = DecisionTreeClassifier(max_depth=3, random_state=42)
modell.fit(X_train, y_train)

# Vis treet som tekst
print("Beslutningstreet:")
print(export_text(modell, feature_names=features))

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

# Hvor viktig er hver feature?
print("\nFeature importance (hvor viktig er hver feature?):")
for feature, importance in zip(features, modell.feature_importances_):
    bar = "█" * int(importance * 30)
    print(f"  {feature:15s}: {importance:.3f} {bar}")

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