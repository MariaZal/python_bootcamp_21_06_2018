# # ZADANIE 2
#
# Napisz funkcję zwracającą zbiór wszystkich znaków występujących w napisie
# więcej niż zadana liczba razy
#
# Przykłąd użycia:
# >>>wiecej_niz('ala ma kota a kot ma ale',3)


def wiecej_niz(tekst, ilosc):
    zbior = set(tekst)
    wiecej = set()

    for i in zbior:
        if tekst.count(i) > ilosc:
            wiecej.add(i)
            print(f'{i} wystepuje wiecej niż {ilosc} razy: {tekst.count(i)}')
    return (wiecej)
    print(wiecej)

wiecej_niz('ggggghhhhhiupoiw',2)
wiecej_niz('ala ma kota a kot ma ale',3)

def test_wiecej_niz_prawda():
    assert wiecej_niz('ala ma kota kot ma ale',3)=={'a',' '}

def test_pusty():
    assert wiecej_niz('fsfsd',3)=={'f'}



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
