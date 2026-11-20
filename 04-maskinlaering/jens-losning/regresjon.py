from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Last inn data
datasett_sti = Path(__file__).resolve().parent.parent / "data" / "titanic.csv"
df = pd.read_csv(datasett_sti)

# Vi bruker alder til å forutsi billettpris
# Først: fjern rader der alder mangler
df = df.dropna(subset=["Age", "Fare"])

# Velg feature (X) og target (y)
X = df[["Age"]]      # Feature: alder (må være i doble klammer for en tabell)
y = df["Fare"]       # Target: billettpris

print(f"Antall datapunkter: {len(X)}")
print(f"Feature: Age")
print(f"Target: Fare")

# Del dataene: 80% trening, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nTreningssett: {len(X_train)} rader")
print(f"Testsett: {len(X_test)} rader")

# Lag en lineær regresjonsmodell
modell = LinearRegression()

# Tren modellen på treningsdataene
modell.fit(X_train, y_train)

# Vis hva modellen lærte
print(f"\nStigningstall (a): {modell.coef_[0]:.2f}")
print(f"Konstantledd (b): {modell.intercept_:.2f}")
print(f"Formel: pris = {modell.coef_[0]:.2f} * alder + {modell.intercept_:.2f}")

# Bruk modellen til å gjette priser på testdataene
y_pred = modell.predict(X_test)

# Beregn feilen
mse = mean_squared_error(y_test, y_pred)
print(f"\nMean Squared Error (MSE): {mse:.2f}")
print(f"Root MSE (RMSE): {mse**0.5:.2f}")

# Vis noen eksempler
print("\nEksempler (alder -> faktisk pris vs. gjettet pris):")
for i in range(5):
    print(f"  Alder {X_test.iloc[i, 0]:.0f}: "
          f"Faktisk {y_test.iloc[i]:.2f}, "
          f"Gjettet {y_pred[i]:.2f}")


plt.scatter(X_test, y_test, alpha=0.5, label="Faktiske priser")
plt.plot(X_test.sort_values("Age"), 
         modell.predict(X_test.sort_values("Age")), 
         color="red", linewidth=2, label="Modellens linje")
plt.xlabel("Alder")
plt.ylabel("Billettpris")
plt.title("Lineær regresjon: Alder vs. Pris")
plt.legend()
plt.savefig("regresjon_resultat.png")
plt.close()
print("\nGraf lagret som regresjon_resultat.png")