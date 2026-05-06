import json
import urllib.request

url = "https://data.brreg.no/enhetsregisteret/api/enheter?navn=arbeidstilsynet"
headers = {"Accept": "application/json"}
request = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(request) as response:
    data = json.loads(response.read().decode("utf-8"))

enheter = data.get("_embedded", {}).get("enheter", [])

for enhet in enheter[:5]:
    organisasjonsform = enhet.get("organisasjonsform", {}).get("beskrivelse", "Ukjent")
    print("Navn:", enhet.get("navn", "Mangler navn"))
    print("Organisasjonsnummer:", enhet.get("organisasjonsnummer", "Mangler nummer"))
    print("Organisasjonsform:", organisasjonsform)
    print()
