# # zmienna = (1,2,3,4)
# # print(zmienna)
# a = ('ala', 'ma', 'kota')
# b = ('ala', 'ma', 3.5, 'koty', 5, 6, 7, 8)
#
# # print(a)
# # print(b)
# # print(len(a))
# # print(len(b))
# # print(a[1])
#
## Zadanie 1
# x = 0
# while x < len(b):
#     print(b[x])
#     x+=1
#
# print('--------------')
#
# print(b[1:])
# print(b[:3])
# print(b[1:6:2])
# print(b[::2])
# print(b[1:-1])
# print(b[::-1])

#
# t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(t)
# print(t[1])
# print(t[-2])
# print(t[2:7])
# print(t[::3])
# print(t[::-2])
# # print(t[::-2])
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
#
# #Zadanie 2
#
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

# #Zadanie 3
#
# b = int(input('Ile liczb wpiszesz '))
#
# dodatnie = 0
# ujemne = 0
# zera = 0
# lista = []
# for a in range(b):
#     lista.append(int(input('Wprowadż liczbe: ')))
#     a += 1
# print(f'liczby: {lista}')
#
# for c in lista:
#     if c<0:
#         ujemne += 1
#
#     elif c>0:
#         dodatnie += 1
#     else:
#         zera += 1
#
# print(f'dodatnich: {dodatnie}, ujemnych: {ujemne}, zer: {zera}')


# #Zadanie 4
# trzy = 0
# piec = 0
# trojki = []
# piatki = []
#
#
# for i in range(100):
#     if i%3==0:
#         trzy += 1
#         trojki.append(i)
#
#     elif i%5==0:
#         piec += 1
#         piatki.append(i)
#
# print(f'Liczby podzielne przez 3 lub 5 {trojki} {piatki}')
# print(f'W przedziale 0-100 jest {trzy} liczb podzielnych przez 3 i {piec} podzielnych przez 5')

# # Zadanie 4 raz jeszcze
#
# liczby = 0
#
# print('Liczby podzielne przez 3 lub przez 5')
#
# for i in range(101):
#     if i%3==0 or i%5==0 :
#         liczby += 1
#         print(i)
#
#
# print(f'W przedziale 0-100 jest {liczby} liczb podzielnych przez 3 lub 5')

# #Zadanie 5
#
# print('    ', end='')
# for x in range(10):
#     print(f'{x:<3}', end=' ')
#
# print()
#
#
# for y in range(10):
#     print()
#     print(f'{y}', end='   ')
#     for x in range (10):
#         print(f'{x*y:<3}', end=' ')

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