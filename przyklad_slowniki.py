# slownik = dict()
# slownik = {}
#
# slownik["klucz"] = "wartosc"
# slownik[1] = "jeden"
# slownik[2] = "dwa"
# x = list(slownik.keys())
#
# print(x)

# ZADANIE 9
# cennik = {'ziemniaki': 0.99, 'pomidory': 1.90, 'maslo': 9.99, 'pomarancze': 3.50, 'czeresnie': 5.00}
# magazyn = {'ziemniaki': 100, 'pomidory': 90, 'maslo': 80, 'pomarancze': 30, 'czeresnie': 500}
#
# for produkt in cennik:
#     print(produkt)
#
# print()
#
# while True:
#     produkt = input(f'jaki produkt Cie interesuje ')
#     if produkt == "KONIEC":
#         break
#     waga = float(input(f'ile kg {produkt} chcesz kupić?: '))
#     if waga >= magazyn[produkt]:
#         print(f"W magazynie mamy jedynie {magazyn[produkt]} kg {produkt} ")
#         continue
#     else:
#         print(f'cena za {produkt} to: {round(float(cennik[produkt])*float(waga),2) } zl')

# ZADANIE 10
napis = input("Podaj napis: ")

klucz = []
slownik = {}
slownik2 = {}

for i in napis:
    if i in klucz:
        continue
    else:
        klucz.append(i)

for k in klucz:
            slownik[k] = 0

for i in napis:
        slownik[i] = slownik[i] + 1

print(slownik)



for l in napis:
    slownik2[l] = slownik2.get(l,0)+1

print(slownik2)
