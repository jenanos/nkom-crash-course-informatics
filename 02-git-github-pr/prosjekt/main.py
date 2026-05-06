from tekstverktoy import tell_linjer, tell_ord, tell_tegn

FILNAVN = "data/eksempeltekst.txt"

with open(FILNAVN, "r", encoding="utf-8") as fil:
    tekst = fil.read()

print("Tekstanalyse")
print("============")
print(f"Fil: {FILNAVN}")
print(f"Antall linjer: {tell_linjer(tekst)}")
print(f"Antall ord: {tell_ord(tekst)}")
print(f"Antall tegn: {tell_tegn(tekst)}")
