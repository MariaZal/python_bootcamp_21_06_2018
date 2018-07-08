lista = [1,2,3,4,5]

kwadraty1 = []
for i in lista:
    kwadraty1.append(i**2)

kwadraty2 = [1**2 for i in lista]

kwadraty_t = [(i, i**2) for i in lista]

#Zadanie 13

zbior = {(i, i**2, i**3) for i in range(-10, 11)}
print(zbior)
lista = [(i, i**2, i**3) for i in range(-10, 11)]
print(lista)
slownik = {i:(i**2) for i in range (-10,11)}
print(slownik)

zbior = {"a", "bb", "ccc", "dddd"}

slownik = {i:len(i) for i in zbior}
print(slownik)

