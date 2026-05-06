import json
import urllib.request

url = "https://api.open-meteo.com/v1/forecast?latitude=59.91&longitude=10.75&current=temperature_2m,wind_speed_10m"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))

current = data.get("current", {})
print("Temperatur:", current.get("temperature_2m", "ukjent"))
print("Vindstyrke:", current.get("wind_speed_10m", "ukjent"))
