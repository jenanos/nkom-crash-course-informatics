# Oppgave 2: Utforsk dataene

Før vi bygger en modell, må vi forstå dataene våre. Dette er alltid første steg i maskinlæring.

## Hva er i Titanic-datasettet?

Datasettet er en CSV-fil (Comma-Separated Values) med informasjon om passasjerer på Titanic:

| Kolonne      | Beskrivelse                                    |
|--------------|------------------------------------------------|
| PassengerId  | Unikt nummer for hver passasjer                |
| Survived     | 0 = døde, 1 = overlevde                       |
| Pclass       | Billetklasse: 1, 2 eller 3                    |
| Name         | Navn                                           |
| Sex          | Kjønn: male eller female                       |
| Age          | Alder i år                                     |
| SibSp        | Antall søsken/ektefelle om bord               |
| Parch        | Antall foreldre/barn om bord                   |
| Fare         | Billettpris                                    |
| Embarked     | Havn de gikk om bord: S, C eller Q            |

## Steg 1: Last inn dataene

Opprett en fil som heter `utforsk.py` i din egen mappe og skriv:

```python
import pandas as pd

# Les CSV-filen inn i en DataFrame (en tabell)
df = pd.read_csv("04-maskinlaering/data/titanic.csv")

# Vis de 5 første radene
print(df.head())
```

**Forklaring:**
- `import pandas as pd` — importerer pandas-biblioteket og gir det kallenavnet `pd`
- `pd.read_csv(...)` — leser en CSV-fil og lager en tabell (DataFrame)
- `df.head()` — viser de 5 første radene

Kjør programmet:

```bash
python3 utforsk.py
```

## Steg 2: Grunnleggende statistikk

Legg til dette i `utforsk.py`:

```python
# Hvor mange rader og kolonner?
print(f"\nAntall rader: {df.shape[0]}")
print(f"Antall kolonner: {df.shape[1]}")

# Statistikk for tallkolonner
print("\nStatistikk:")
print(df.describe())
```

**Forklaring:**
- `df.shape` gir deg (antall rader, antall kolonner)
- `df.describe()` gir gjennomsnitt, min, max osv. for alle tallkolonner

## Steg 3: Sjekk manglende data

```python
# Hvor mange verdier mangler i hver kolonne?
print("\nManglende verdier:")
print(df.isnull().sum())
```

**Forklaring:**
- `df.isnull()` sjekker om hver celle er tom
- `.sum()` teller antall tomme celler per kolonne

Manglende data er vanlig i virkeligheten. Senere skal vi lære å håndtere det.

## Steg 4: Hvem overlevde?

```python
# Hvor mange overlevde?
print("\nOverlevelse:")
print(df["Survived"].value_counts())

# Overlevelse fordelt på kjønn
print("\nOverlevelse per kjønn:")
print(df.groupby("Sex")["Survived"].mean())

# Overlevelse fordelt på klasse
print("\nOverlevelse per klasse:")
print(df.groupby("Pclass")["Survived"].mean())
```

**Forklaring:**
- `value_counts()` teller hvor mange av hver verdi
- `groupby("Sex")` grupperer radene etter kjønn
- `.mean()` gir gjennomsnittet — her betyr det andelen som overlevde (fordi 0 = nei, 1 = ja)

## Steg 5: Lag en enkel graf

```python
import matplotlib.pyplot as plt

# Overlevelse per klasse som søylediagram
df.groupby("Pclass")["Survived"].mean().plot(kind="bar")
plt.title("Andel som overlevde per klasse")
plt.xlabel("Klasse")
plt.ylabel("Andel overlevde")
plt.savefig("overlevelse_per_klasse.png")
plt.close()
print("\nGraf lagret som overlevelse_per_klasse.png")
```

**Forklaring:**
- `.plot(kind="bar")` lager et søylediagram
- `plt.savefig(...)` lagrer grafen som en bildefil
- `plt.close()` lukker figuren så den ikke tar opp minne

## Oppgave

1. Kjør hele `utforsk.py` og se på resultatene.
2. Hva er gjennomsnittsalderen i datasettet?
3. Hvilken klasse hadde høyest overlevelsesrate?
4. Overlevde kvinner eller menn oftere?

## Hva har vi lært?

- Hvordan laste inn en CSV-fil med pandas
- Hvordan se på de første radene i et datasett
- Hvordan finne grunnleggende statistikk
- Hvordan sjekke for manglende data
- Hvordan gruppere data og lage enkle grafer

## Neste steg

Nå som vi kjenner dataene, er vi klare til å bygge vår første modell: lineær regresjon.
