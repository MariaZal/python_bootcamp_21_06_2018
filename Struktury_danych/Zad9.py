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
