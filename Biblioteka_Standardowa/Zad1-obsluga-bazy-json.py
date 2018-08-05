import json

action = input("Co chcesz zrobić? [d-dodaj, w -wypisz]")

try:
    with open('pracownik.json') as f:
        lista_pracownikow = json.load(f)
except FileNotFoundError:
    lista_pracownikow = []

pracownik = {}

if action == 'd':
    pracownik = {'imie': input("Imie: "), 'nazwisko': input("Nazwisko: "), 'rok': int(input("Rok urodzenia: ")),
                 'pensja': float(input("Pensja: "))}
    lista_pracownikow.append(pracownik)

    with open("pracownik.json", 'w') as f:
        json.dump(lista_pracownikow, f)

elif action == 'w':
        for c, a in enumerate(lista_pracownikow):
            print(c+1, a['imie'], a['nazwisko'], '- rok:', a['rok'], ', pensja:', a['pensja'])

