#Zadanie 6
a=0
b = int(input('Ile elementow ma lista '))
lista = []
while a < b:
    lista.append(int(input('Wprowadż liczbe: ')))
    a += 1
print(f'lista: {lista}')

max = lista[0]
min = lista[0]

for i in range(len(lista)):
    if lista[i] > max:
        max = lista[i]
    elif lista[i] < min:
        min = lista[i]

x=lista.index(min)
y=lista.index(max)

lista[x] = max
lista[y] = min

print(f'zamieniona{lista}')