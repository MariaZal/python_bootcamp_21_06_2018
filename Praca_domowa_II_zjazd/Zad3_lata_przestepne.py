# Zaimplementuj funkcję zwracającą listę lat przestępnych na podstawie zadanego zakresu.
# Podpowiedź: rok przestępny to taki który dzieli się przez 4,
# ale nie dzieli się przez 100 lub dzieli się przez 400
# Przykład użycia:
# >>>	lata_przestepne(1990,	2020)
# [1992,	1996,	2000,	2004,	2008,	2012,	2016,	2020]

def lata_przestepne(poczatek,koniec):
    lata = []
    for i in range(poczatek,koniec+1):
        if i%4==0 and i%100!=0 or i%400==0:
            lata.append(i)

    print(lata)

lata_przestepne(1980, 2020)

def test_rok_przestepny():
    assert lata_przestepne(1990, 2020)==[1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
