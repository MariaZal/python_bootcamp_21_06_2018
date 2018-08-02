# #Zadanie 3
# Napisz program zliczający wystąpienia liczb dodatnich i ujemnych
# w zadanej liście liczb całkowitych



# lista = [1,2,3,4,5,6,7,8]
# for element in lista:
#     print(element)
#
# tupla = ('ala', 'ma', 3, 'koty', 'bla', 3, 5,)
# for el in tupla:
#     print(el)
#
# for x, zmienna in enumerate (tupla, start=1):
#     print(x, zmienna)
#
# for i in range(2,11,2):
#     print(i)
#
# print('--------------range(len(tupla)-----------')
# for i in range(0,len(tupla),2):
#     print(i, tupla[i])

#-----------------------------------------------------------------------------------
dodatnie=0
ujemne=0
zera=0

a=0
lista=[]

while True:
    a=input("Podaj liczbę: ")
    if a!="o":
        lista.append(int(a))
    else:
        print(lista)
        break

for x in lista:
    if x<0:
        ujemne=ujemne+1
    if x>0:
        dodatnie=dodatnie+1
    if x==0:
        zera=zera+1

print(f'dodatnie={dodatnie} ujemne={ujemne} zera={zera}')

#
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


