from api_hjelper import hent_json

url = "https://jsonplaceholder.typicode.com/todos/1"

statuskode, data = hent_json(url)

print("Statuskode:", statuskode)
print("Data fra API:")
print(data)
