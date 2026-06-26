# Oppgave 3: Lineær regresjon

Lineær regresjon er den enkleste formen for maskinlæring. Den prøver å trekke en rett linje gjennom datapunktene dine.

## Hva er lineær regresjon?

Tenk deg at du vil forutsi billettpris basert på alder. Lineær regresjon finner en rett linje som passer best:

```
pris = a * alder + b
```

Her er:
- `a` (stigningstallet): hvor mye prisen endrer seg per år
- `b` (konstantleddet): startverdi når alder er 0

Modellen finner de beste verdiene for `a` og `b` ved å minimere feilen mellom sine gjetninger og de virkelige prisene.

## Hvordan lærer modellen?

1. Modellen starter med tilfeldige verdier for `a` og `b`
2. Den beregner hvor mye den bommer (feilen)
3. Den justerer `a` og `b` for å redusere feilen
4. Dette gjentas til feilen er så liten som mulig

Feilen måles ofte med **MSE** (Mean Squared Error) — gjennomsnittet av alle feilene i andre:

```
MSE = gjennomsnitt av (faktisk_verdi - gjettet_verdi)²
```

Jo lavere MSE, jo bedre er modellen.

## Steg 1: Forbered dataene

Opprett en fil som heter `regresjon.py`:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Last inn data
df = pd.read_csv("04-maskinlaering/data/titanic.csv")

# Vi bruker alder til å forutsi billettpris
# Først: fjern rader der alder mangler
df = df.dropna(subset=["Age", "Fare"])

# Velg feature (X) og target (y)
X = df[["Age"]]      # Feature: alder (må være i doble klammer for en tabell)
y = df["Fare"]       # Target: billettpris

print(f"Antall datapunkter: {len(X)}")
print(f"Feature: Age")
print(f"Target: Fare")
```

**Forklaring:**
- `dropna(subset=["Age", "Fare"])` fjerner rader der alder eller pris mangler
- `X = df[["Age"]]` — doble klammer gir en tabell (DataFrame), som sklearn krever
- `y = df["Fare"]` — enkle klammer gir en kolonne (Series)

## Steg 2: Del i trening og test

```python
# Del dataene: 80% trening, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nTreningssett: {len(X_train)} rader")
print(f"Testsett: {len(X_test)} rader")
```

**Forklaring:**
- `train_test_split` blander og deler dataene tilfeldig
- `test_size=0.2` betyr 20 % til testing
- `random_state=42` gjør at vi får samme resultat hver gang

## Steg 3: Tren modellen

```python
# Lag en lineær regresjonsmodell
modell = LinearRegression()

# Tren modellen på treningsdataene
modell.fit(X_train, y_train)

# Vis hva modellen lærte
print(f"\nStigningstall (a): {modell.coef_[0]:.2f}")
print(f"Konstantledd (b): {modell.intercept_:.2f}")
print(f"Formel: pris = {modell.coef_[0]:.2f} * alder + {modell.intercept_:.2f}")
```

**Forklaring:**
- `LinearRegression()` lager en tom modell
- `modell.fit(X_train, y_train)` trener modellen — den finner de beste `a` og `b`
- `modell.coef_` er stigningstallet
- `modell.intercept_` er konstantleddet

## Steg 4: Test modellen

```python
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
```

**Forklaring:**
- `modell.predict(X_test)` bruker formelen på nye data
- `mean_squared_error` beregner gjennomsnittlig feil
- RMSE (roten av MSE) er lettere å tolke — den er i samme enhet som prisen

## Steg 5: Visualiser resultatet

```python
import matplotlib.pyplot as plt

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
```

## Diskusjon

Lineær regresjon fungerer dårlig her. Hvorfor?

1. Sammenhengen mellom alder og pris er ikke en rett linje
2. Pris avhenger av mange ting (klasse, havn osv.), ikke bare alder
3. Det er mange variasjoner som en enkel linje ikke fanger opp

Det er OK! Vi har lært hvordan prosessen fungerer:
1. Forbered data
2. Del i trening/test
3. Tren modellen
4. Evaluer resultatet

Denne prosessen er den samme for alle modeller vi skal prøve.

## Oppgave

1. Kjør hele `regresjon.py` og se på resultatene.
2. Hva er RMSE? Er modellen god?
3. Prøv å endre feature til `Pclass` i stedet for `Age`. Blir modellen bedre?

## Neste steg

I neste oppgave skal vi prøve logistisk regresjon — en modell for klassifisering som kan forutsi om noen overlevde eller ikke.
