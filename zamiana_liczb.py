lista = [0, 1, 2, 3, 4, 8, 9, 5, 11]

g = lista.index(max(lista))
d = lista.index(min(lista))

x = max(lista)
y = min(lista)

lista[g] = y
lista[d] = x

print(lista)