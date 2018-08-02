# # ZADANIE 3


def policz_znaki(napis, start, end):
    waga = 0
    ilosc = 0

    for i in napis:
        if i == start:
            waga += 1
        elif i == end:
            waga -= 1
        else:
            ilosc += waga
    print(ilosc)
    return ilosc


policz_znaki("dfd<<24<71>24>>789",'<', '>')
policz_znaki('ala [kota [a kot]] ma ale', '[', ']')
policz_znaki('a <a<a<a>>>', '<', '>')

# def test_czy_dobrze_liczysz_znaki_1():
#     assert policz_znaki('ala [kota [a kot]] ma ale','[',']') == 18
# def test_czy_dobrze_liczysz_znaki_2():
#     assert policz_znaki('a <a<a<a>>>') == 6
# def test_czy_dobrze_liczysz_znaki_3():
#     assert policz_znaki('ala ma <kota> a kot ma ale')==4












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
# def test_czy_dobrze_liczysz_znaki_1():
#     assert policz_znaki('<','>', "ala ma <kota> a kot ma ale") == 4
#
#
# def test_czy_dobrze_liczysz_znaki_2():
#     assert policz_znaki('[',']', "ala [kota [a kot]] ma [ale]") == 18
#
# def test_czy_dobrze_liczysz_znaki_3():
#     assert policz_znaki('<','>', "a <a<a<a>>>") == 6
