"""
Startkode for del 4: Maskinlæring
Kjør dette programmet for å sjekke at alt er installert riktig.
"""

print("=== Del 4: Maskinlæring - Sjekk installasjon ===\n")

# Sjekk pandas
try:
    import pandas as pd
    print(f"✓ pandas versjon {pd.__version__} er installert")
except ImportError:
    print("✗ pandas mangler. Kjør: pip install pandas")

# Sjekk scikit-learn
try:
    import sklearn
    print(f"✓ scikit-learn versjon {sklearn.__version__} er installert")
except ImportError:
    print("✗ scikit-learn mangler. Kjør: pip install scikit-learn")

# Sjekk matplotlib
try:
    import matplotlib
    print(f"✓ matplotlib versjon {matplotlib.__version__} er installert")
except ImportError:
    print("✗ matplotlib mangler. Kjør: pip install matplotlib")

# Sjekk at datasettet finnes
import os

datasett_sti = os.path.join(os.path.dirname(__file__), "..", "data", "titanic.csv")
if os.path.exists(datasett_sti):
    df = pd.read_csv(datasett_sti)
    print(f"\n✓ Titanic-datasettet funnet ({len(df)} rader)")
    print(f"\nKolonner: {', '.join(df.columns)}")
    print(f"\nDe 3 første radene:")
    print(df.head(3).to_string(index=False))
else:
    print(f"\n✗ Fant ikke datasettet på: {datasett_sti}")

print("\n=== Alt klart! Du kan begynne med oppgavene. ===")
