# przygotowanie danych przed petla
#jak dlugo ma sie wykonywac (naglowek, ile iteracji)
# co petla ma faktycznie robic (cialo petli)

# #Zadanie 12
# a = 1
# while a <= 100:
#     print(a**2)
#     a += 1

# #Zadanie 13
# a = 0
# suma = 0
# while a < 7:
#     suma  += int(input(f'Podaj temperature {a+1} dnia: '))
#     a += 1
# print(f' Srednia: {suma/a:.2f}')


# #Zadanie 14
# d = input('podaj kolejna liczbe lub zakoncz ')
# max = d
# min = d
#
# while d != 'stop':
#     d = int(d)
#     if int(d) > int(max):
#         max = d
#     if int(d) < int(min):
#         min = d
#     d = input('podaj kolejna liczbe lub zakoncz ')
#
# if min != 'stop':
#     print(f'max={max}, min={min}')
# else:
#     print('Koniec')

#Zadanie 14 - lepiej
# # 1 obsluga wyjatkow - (wyjatkowych sytuacji)
# komunikat = 'podaj kolejna liczbe lub zakoncz '
# d = input(komunikat)
#
# if d == 'stop':
#     exit ('Nie podales zadnych liczb')
#
# d = int(d)
# min = d
# max = d
#
#
# while True:
#     d = input(komunikat)
#     if d == 'stop':
#         break
#     d = int(d)
#     if d > max:
#         max = d
#     if d < min:
#         min = d
#
# print(f'max={max}, min={min}')

#Zadanie 15

import random

gracz_x = random.randrange(1, 11)
gracz_y = random.randrange(1, 11)


#print(f'debug: gracz {gracz_x}, {gracz_y}, skarb {skarb_x}, {skarb_y}')

while  True:

    a = 0
    skarb_x = random.randrange(1, 11)
    skarb_y = random.randrange(1, 11)

    while a < 3:
        podp = random.randrange(1,6)
        print(f'Twoja pozycja to {gracz_x}, {gracz_y}')
        if gracz_x > 10 or gracz_y > 10 or gracz_x < 1 or gracz_y < 1:
            exit('Wyszedles poza plansze - przegrales')
            break

        if gracz_x == skarb_x and gracz_y == skarb_y:
            exit('Wygrales')
            break

        odl_x = abs(gracz_x - skarb_x)
        odl_y = abs(gracz_y - skarb_y)

        krok = input('''Podaj w ktora strone chcesz isc 
        [l] lewo
        [p] prawo
        [g] gora
        [d] dol
        ''')

        if krok == 'l':
            gracz_x -= 1
            if podp > 1:
                if abs(gracz_x - skarb_x)<odl_x:
                    print('zblizasz sie')
                else:
                    print('oddalasz sie')
            else:
                print('brak podpowiedzi')

        elif krok == 'p':
            gracz_x += + 1
            if podp > 1:
                if abs(gracz_x - skarb_x)<odl_x:
                    print('zblizasz sie')
                else:
                    print('oddalasz sie')
            else:
                print('brak podpowiedzi')

        elif krok == 'g':
            gracz_y -= 1
            if podp > 1:
                if abs(gracz_y - skarb_y)<odl_y:
                    print('zblizasz sie')
                else:
                    print('oddalasz sie')
            else:
                print('brak podpowiedzi')
        elif krok == 'd':
            gracz_y += 1
            if podp > 1:
                if abs(gracz_y - skarb_y)<odl_y:
                    print('zblizasz sie')
                else:
                    print('oddalasz sie')
            else:
                print('brak podpowiedzi')

        print(f'debug: gracz {gracz_x}, {gracz_y}, skarb {skarb_x}, {skarb_y}')

        a += 1

    print('spozniles sie, smok zmienil miejsce')