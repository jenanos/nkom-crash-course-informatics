import json
import urllib.request

url = "https://date.nager.at/api/v3/PublicHolidays/2025/NO"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))

for helligdag in data:
    print(helligdag.get("date"), "-", helligdag.get("localName"))
