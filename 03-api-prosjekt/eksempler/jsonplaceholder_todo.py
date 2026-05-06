import json
import urllib.request

url = "https://jsonplaceholder.typicode.com/todos/1"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))

print("Tittel:", data.get("title"))
print("Fullført:", data.get("completed"))
