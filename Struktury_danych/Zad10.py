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