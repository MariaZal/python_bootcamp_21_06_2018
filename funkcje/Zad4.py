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
