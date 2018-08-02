# Zaimplementuj funkcję zliczającą liczbę wystąpień poszczególnych słów w zadanym napisie.
# Podpowiedź: do podzielenia napisu na słowa użyj metody split() .
# Przykład użycia:
# >>>	policz_slowa('ala	ma	kota	i	kota	ma	ala')
# {'ala':	2,	'i':	1,	'kota':	2,	'ma':	2}


def policz_slowa(napis):
    napis_podzielony = napis.split(" ")
    wyrazy = set(napis_podzielony)
    slownik = {}

    for i in wyrazy:
        slownik[i] = napis_podzielony.count(i)

    print(slownik)


policz_slowa('ala ala ala nie nie nie lubi zupy zupy')


def test_policz_slowa():
    policz_slowa('ala ma kota i kota ma ala') == {'ma': 2, 'i': 1, 'kota': 2, 'ala': 2}
