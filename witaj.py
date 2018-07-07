# print('Hello world!')
#
# b = 3
# a = 1
#
# c=a/b
#
# print(c)
#
# print(c*3)
#
# print(1/2.)
# print(0.5)
#
# print(0.1 + 0.2)
#
# napis1 = "bla"
# napis2 = "bla"
# print(napis1)
# print(napis2)
# print(napis1 == napis2)
#
# a="bbabb"
#
# if a:
#     print ('prawda')
# else:
#     print('falsz')
#
# print(a+ 'fhosf')


# #Zadanie 1/2
# a = 10
# h = 5
# t = a * h / 2
#
# pi = 3.14
# r = 7
# k = pi * r**2
#
# a = 3
# b = 9
# h = 6.5
# tr = (a+b) * h/2
#
# r= 7/8
# kul = 4/3 * pi * r**3
#
# print('trojkat=', t)
# print('kolo=', k)
# print('trapez=', tr)
# print('kula=', kul)
#
#
# #Zadanie 3
# imie = 'Maria'
# wzrost = 173
#
# print('Imię: ', imie)
# print('Wzrost: ', wzrost)
# print(f'Imię: {imie} \nWzrost: {wzrost}')


#Zadanie 4

cena = 10.0
waga = 2.5
koszt = cena * waga

# <10 wyrównaj do lewej (w obrębie 10 znakow)
# ^10 wyrownaj do srodka
# >10 wyrownaj do prawej
# .2f - wyrównaj do dwóch miejsc po przecinku

print(f'''{"Cena za kg:":<10}{cena:>10.2f}{"zł":>5}
{"Waga:":<10} {waga:>10.2f}{"kg":>5}
{"Nalezność:":<10} {cena * waga :>10.2f}{"zł":>5}''')

#dygresja xor na bitach:
#print(7^1)