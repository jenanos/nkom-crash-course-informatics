from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import PercentFormatter
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, confusion_matrix

# Last inn data
datasett_sti = Path(__file__).resolve().parent.parent / "data" / "titanic.csv"
df = pd.read_csv(datasett_sti)

# Fjern rader med manglende verdier i kolonnene vi bruker
df = df.dropna(subset=["Age", "Fare", "Embarked"])

# Gjør kjønn om til tall (encoding)
# male = 0, female = 1
df["Sex_encoded"] = df["Sex"].map({"male": 0, "female": 1})

print("Slik ser encoded kjønn ut:")
print(df[["Sex", "Sex_encoded"]].head())

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

# Lag og tren modellen
modell = LogisticRegression(max_iter=1000)
modell.fit(X_train, y_train)

# Vis vektene modellen lærte
print("\nHva modellen lærte (vekter per feature):")
for feature, vekt in zip(features, modell.coef_[0]):
    print(f"  {feature}: {vekt:.3f}")

# Gjør prediksjoner på testdata
y_pred = modell.predict(X_test)

# Beregn nøyaktighet
accuracy = accuracy_score(y_test, y_pred)
print(f"\nNøyaktighet (accuracy): {accuracy:.1%}")
print(f"Det betyr at modellen gjetter riktig {accuracy:.1%} av gangene.")

# Confusion matrix (forvirringsmatrise)
cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
print(f"\nForvirringsmatrise:")
print(f"                  Gjettet: Døde  |  Gjettet: Overlevde")
print(f"  Faktisk døde:      {cm[0][0]:>4}        |      {cm[0][1]:>4}")
print(f"  Faktisk overlevde: {cm[1][0]:>4}        |      {cm[1][1]:>4}")

# Lag nye passasjerer med de samme kolonnene som modellen ble trent på.
ny_passasjer = pd.DataFrame([
    {"Pclass": 1, "Sex_encoded": 1, "Age": 25, "Fare": 70.0}
])[features]
sannsynlighet = modell.predict_proba(ny_passasjer)[0]
prediksjon = modell.predict(ny_passasjer)[0]

print("\nNy passasjer: Kvinne, 25 år, 1. klasse, billett 70 kr")
print(f"Sannsynlighet for å dø: {sannsynlighet[0]:.1%}")
print(f"Sannsynlighet for å overleve: {sannsynlighet[1]:.1%}")
print(f"Modellens gjetning: {'Overlevde' if prediksjon == 1 else 'Døde'}")

ny_passasjer2 = pd.DataFrame([
    {"Pclass": 3, "Sex_encoded": 0, "Age": 30, "Fare": 8.0}
])[features]
sannsynlighet2 = modell.predict_proba(ny_passasjer2)[0]
prediksjon2 = modell.predict(ny_passasjer2)[0]

print("\nNy passasjer: Mann, 30 år, 3. klasse, billett 8 kr")
print(f"Sannsynlighet for å dø: {sannsynlighet2[0]:.1%}")
print(f"Sannsynlighet for å overleve: {sannsynlighet2[1]:.1%}")
print(f"Modellens gjetning: {'Overlevde' if prediksjon2 == 1 else 'Døde'}")

# Visualiser antall riktige og feil, og hvor nær hver prediksjon er grensen.
klassenavn = ["Døde", "Overlevde"]
fig, (matrise_akse, sannsynlighet_akse) = plt.subplots(
    1, 2, figsize=(11, 5), layout="constrained"
)
fig.suptitle(f"Logistisk regresjon på Titanic · {accuracy:.0%} riktige")

ConfusionMatrixDisplay(cm, display_labels=klassenavn).plot(
    ax=matrise_akse, cmap="Blues", colorbar=False
)
matrise_akse.set(title="Forvirringsmatrise", xlabel="Gjettet", ylabel="Faktisk")

# Klasse 1 betyr overlevde. Behold fasiten på samme rad som sannsynligheten.
overlevde_kolonne = list(modell.classes_).index(1)
testresultater = pd.DataFrame({
    "sannsynlighet": modell.predict_proba(X_test)[:, overlevde_kolonne],
    "fasit": y_test.to_numpy(),
}).sort_values("sannsynlighet", ignore_index=True)
testresultater.index += 1

for klasse, navn, farge in zip([0, 1], klassenavn, ["#a64018", "#176c9d"]):
    gruppe = testresultater[testresultater["fasit"] == klasse]
    sannsynlighet_akse.scatter(
        gruppe["sannsynlighet"], gruppe.index, color=farge, label=navn
    )

sannsynlighet_akse.axvline(0.5, color="0.35", linestyle="--", label="Grense på 50 %")
sannsynlighet_akse.set(
    title="Én prikk per passasjer i testsettet",
    xlabel="Modellens sannsynlighet for å overleve",
    ylabel="Passasjerer sortert etter sannsynlighet",
    xlim=(-0.03, 1.03),
    xticks=[0, 0.25, 0.5, 0.75, 1],
    yticks=[],
)
sannsynlighet_akse.xaxis.set_major_formatter(PercentFormatter(xmax=1))
sannsynlighet_akse.legend(title="Faktisk utfall og grense", loc="upper left")

# Agg kan tegne figuren til en fil når et grafikkvindu ikke er tilgjengelig.
if plt.get_backend().lower() == "agg":
    figur_sti = Path(__file__).resolve().with_name("klassifisering-resultater.png")
    fig.savefig(figur_sti, dpi=150)
    print(f"\nFiguren er lagret i {figur_sti}")
else:
    plt.show()
