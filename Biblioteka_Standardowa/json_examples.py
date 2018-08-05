import json

# print(dir(json))
# print(help(json))

# dump - wrzucić cos dumps() - obsluguje stringi
# load - załadować

lista = [1, 2, 'a', 'd']
print(json.dumps(lista))

with open("first.json", 'w') as f:
    json.dump(lista, f)

slownik = {"Polska": "Warszawa", "Rosja": "Moskwa"}
with open("stolice.json", 'w') as f:
    json.dump(slownik, f)

with open("stolice2.json", encoding='utf8') as f:
    stolice = json.load(f)
    print(stolice['Francja'])
