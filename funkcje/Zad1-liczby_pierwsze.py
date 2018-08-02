# Zadanie 1
# Napisz funkcję sprawdzającą czy dana liczba jest liczbą pierwszą.
# Przykłąd użycia:
# >>>czy_jest_pierwsza(10)
# False
# >>>czy_jest_pierwsza(7)
# True

# --------------------------------------------------------------------------------
# def czy_jest_parzysta(x):
#     print(x % 2 == 0)
#
# czy_jest_parzysta(44)
# czy_jest_parzysta(53)
#
# def test_czy_jest_parysta_dla_parzystej():
#     assert czy_jest_parzysta(2) == True
#
# def test_czy_jest_parzysta_dla_nieparzystej():
#     assert czy_jest_parzysta(3) == False

# --------------------------------------------------------------------------------

def czy_jest_pierwsza(x):
    for y in range(2, x):
        if (x % y)==0:
            return False
    return True
#
# czy_jest_pierwsza(90)

# def test_czy_jest_pierwsza_dla_pierwszej():
#     assert czy_jest_pierwsza(5)
# def test_czy_jest_pierwsza_dla_niepierwszej():
#     assert czy_jest_pierwsza(22)







for l in range(200, 300):
    if czy_jest_pierwsza(l):
      print(f'{l} {czy_jest_pierwsza(l)}')

#
# #Definiowanie testu
# def test_czy_jest_pierwsza_dla_liczby_pierwszej():
# #     assert czy_jest_pierwsza(11) == True

# def test_czy_jest_pierwsza_dla_liczby_niepierwszej():
#     assert czy_jest_pierwsza(4) == False