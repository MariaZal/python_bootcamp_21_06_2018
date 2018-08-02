# Zaimplementuj funkcję, która na podstawie podanej listy stworzy nową listę zawierającą tylko elementy
# oryginalnej kolekcji z podanego zakresu.
# Funkcja powinna przyjmować trzy parametry:
# listę
# początek zakresu
# koniec zakresu
# Przykład użycia:
# >>>	filtruj([-2,	10,	0,	5,	1,	16,	9],	5,	15)
# [10,	5,	9]

def filtruj(lista, poczatek, koniec):
    kolekcja = []
    zbior = set(lista)

    for i in zbior:
        if i >= poczatek and i <= koniec:
            kolekcja.append(i)

    print(kolekcja)


filtruj([-1, -1, 0, 0, 10, 100], -1, 10)
filtruj([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 11, 14, 18, 0], 0, 10)


def test_filtruj1():
    assert filtruj([1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 7, 7, 8], 1, 2) == [1, 2]


def test_filtruj2():
    assert filtruj([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 11, 14, 18, 0], 0, 10) == [0, 1, 2, 3, 4, 5]
