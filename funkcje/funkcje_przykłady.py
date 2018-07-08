# def hello_world():
#     print("hello world")
#
# hello_world()
#
# def hello_name(name):
#     print(f"Hello {name}")
#
# hello_name('XX')
#
# Zadanie 1

# def czy_jest_parzysta(x):
#     print(x % 2 == 0)
#
#
# czy_jest_parzysta(2)

#
# def czy_jest_pierwsza(x):
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True
#
#
# for l in range(1, 30):
#     print(f'{l} {czy_jest_pierwsza(l)}')

#
# #Definiowanie testu
# def test_czy_jest_pierwsza_dla_liczby_pierwszej():
# #     assert czy_jest_pierwsza(11) == True

# def test_czy_jest_pierwsza_dla_liczby_niepierwszej():
#     assert czy_jest_pierwsza(4) == False


# # ZADANIE 2
#
#
# def wiecej_niz(tekst, ilosc):
#     zbior = set(tekst)
#     wiecej = set()
#     for i in zbior:
#         if tekst.count(i) > ilosc:
#             wiecej.add(i)
#         # print(f'{i} wystepuje {tekst.count(i)} razy')
#     return wiecej
#
#
# wiecej_niz("zzzzzxxxxcccdd", 2)
#
#
# def test_czy_znak_wystepuje_wiecej_niz_x_razy():
#     assert wiecej_niz('ala ma kota a kot ma ale', 3) == {' ', 'a'}
#
#
# def test_empty():
#     assert wiecej_niz('', 0) == set()

# # ZADANIE 3

# def policz_znaki(start, end, tekst):
#     poziom = 0
#     ilosc = 0
#     for i in tekst:
#         if i == start:
#             poziom += 1
#         elif i == end:
#             poziom -= 1
#         else:
#             ilosc +=poziom
#
#     return ilosc
#
# print(policz_znaki('<', '>',"dfd<<24<71>24>>789"))
#
# def test_czy_dobrze_liczysz_znaki_1():
#     assert policz_znaki('<','>', "ala ma <kota> a kot ma ale") == 4
#
#
# def test_czy_dobrze_liczysz_znaki_2():
#     assert policz_znaki('[',']', "ala [kota [a kot]] ma [ale]") == 18
#
# def test_czy_dobrze_liczysz_znaki_3():
#     assert policz_znaki('<','>', "a <a<a<a>>>") == 6


# ZADANIE 4

def formatuj(*args, **kwargs):
    print(args)
    print("kwargs")
    print(kwargs)
    for i in args:
        if i == '$':
            for j in kwargs:
                modul = i + j
                return modul


args = ('hofsd $d')
kwargs = dict(c=10)
wynik = formatuj(*args, **kwargs)
print(wynik)



def test_czy_dobrze_formatuje():
    assert formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=10) == 'koszt 10 PLN\nkwota 10 brutto'
