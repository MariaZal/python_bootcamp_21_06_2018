# #Zadanie 2
# Napisz program obliczający średnią wartość z podanych przez użytkownika liczb
# Do przechowywania liczb użyj listy.
# Pozwól na wprowadzenie maksymalnie 10 liczb.
# Skorzystaj z funkcji wbudowanej sum()
#
# lista = [1,2,3,4,5,6,7]
#
# print(len(lista))
# print(lista[0])
# print(lista[-1])
# print(lista[::2])
# lista.append('ala')
# print(lista)
#
# lista.insert(-1, 'kot')
# print(lista)
# print(len(lista))
# lista[3:7] = 'tu byl element4'
# print(lista.count('kot'))
# print(lista)
# print(len(lista))
# --------------------------------------------------------------------------------

lista = []
b=1
while b<=10:
    a = input(f'Podaj {b} liczbę lub oblicz średnią: ')
    if a != 's':
        lista.append(int(a))
        b = b + 1
    else:
        break

print(f'średnia={sum(lista)/len(lista)}')


print(lista)

# a = 0
# b = int(input('Sume ilu liczb chcesz obliczyc? '))
# lista = []
# while a < b:
#     lista.append(int(input('Wprowadż liczbe: ')))
#     a += 1
# print(f'liczby: {lista}')
#
# print(f'srednia = {(sum(lista))/(len(lista))}')

# lista = [1,2,3,4,5,6,7,8]
# for element in lista:
#     print(element)
#
# tupla = ('ala', 'ma', 3, 'koty', 'bla', 3, 5,)
# for el in tupla:
#     print(el)
#
# for nr, zmienna in enumerate (tupla, start=1):
#     print(nr, zmienna)
#
# for i in range(10):
#     print(i)
#
# print('--------------range(len(tupla)-----------')
# for i in range(1,len(tupla),2):
#     print(i, tupla[i])