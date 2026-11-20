from pathlib import Path

import pandas as pd

# Les CSV-filen inn i en DataFrame (en tabell)
datasett_sti = Path(__file__).resolve().parent.parent / "data" / "titanic.csv"
df = pd.read_csv(datasett_sti)

# Vis de 5 første radene
print(df.head())

# Hvor mange rader og kolonner?
print(f"\nAntall rader: {df.shape[0]}")
print(f"Antall kolonner: {df.shape[1]}")

# Statistikk for tallkolonner
print("\nStatistikk:")
print(df.describe())

# Hvor mange verdier mangler i hver kolonne?
print("\nManglende verdier:")
print(df.isnull().sum())

# Hvor mange overlevde?
print("\nOverlevelse:")
print(df["Survived"].value_counts())

# Overlevelse fordelt på kjønn
print("\nOverlevelse per kjønn:")
print(df.groupby("Sex")["Survived"].mean())

# Overlevelse fordelt på klasse
print("\nOverlevelse per klasse:")
print(df.groupby("Pclass")["Survived"].mean())

# Overlevelse fordelt på alder
print("\nOverlevelse per alder:")
print(df.groupby("Age")["Survived"].mean())

import matplotlib.pyplot as plt

# Overlevelse per klasse som søylediagram
df.groupby("Pclass")["Survived"].mean().plot(kind="bar")
plt.title("Andel som overlevde per klasse")
plt.xlabel("Klasse")
plt.ylabel("Andel overlevde")
plt.savefig("overlevelse_per_klasse.png")
plt.close()
print("\nGraf lagret som overlevelse_per_klasse.png")