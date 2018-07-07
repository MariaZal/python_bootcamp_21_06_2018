# imie = input('wpisz swoje imie: ')
# wiek = int (input('ile masz lat? '))
# print(f'''witaj, {imie} za dwa lata bedziesz mial {wiek+2} lat''')
# if wiek>=18:
#     print("chodź na piwo")
# else:
#     print ("idz do domu")
# print('koniec programu')

# #Zadanie 5
# miasto1 = input('Z jakiego miasta wyruszasz? ')
# miasto2 = input('Do jakiego miasta jedzisz? ')
# dystans = float(input('Jaki pokonasz dystans? '))
# cena = float(input("Jaka jest cena paliwa? "))
# spalanie = float (input('Jakie spalanie ma Twoj samochod? '))
#
# print(f'''{"Miasto A:":<20} {miasto1:>30}
# {"Miasto B:":<20} {miasto2:>30}
# {"Dystans" + miasto1 + "-" + miasto2:<20} {dystans:>30}
# {"Cena paliwa:":<20} {cena:>30}
# {"Spalanie ba 100 km:":<20} {spalanie:>30}
#
# Koszt przejazdu Warszawa- Gdańsk to {int(dystans/100*spalanie*cena):>20} PLN''')

# # Zadanie 6
#
# liczba = float(input("Podaj liczbe: "))
# print(f'''Wieksza od 10:{liczba>10}
# Mniejsza rowna 15: {liczba<=15}
# Podzielna przez 2: {liczba%2==0}''')

# Zadanie 7
# zmienna = int(input("Podaj liczbę: "))
# print(f'''Liczba jest podzielna przez 2, podzielna przez 3 i większa od 10 lub jest to liczba 7:
# {zmienna == 7 or zmienna % 2 == 0 and zmienna % 3 == 0 and zmienna > 10}''')

# # Zadanie 8
#
# x = int(input("podaj wysokosc: "))
# y = int(input("podaj podaj szerokosc: "))
# z = int(input("podaj podaj dlugosc: "))
# print(f'Podane naczynie zmiesci jeden litr: {x*y*z>=1000}')

# Zadanie 9
# rok = int(input("Podaj rok urodzenia: "))
# import datetime
# data = datetime.date.today()
# rok1 = data.year
# if rok1-rok>18:
#     print("Jestes pelnoletni!")
# elif rok1-rok==18:
#     print("Gratulacje! w tym roku uzyskasz pełnoletniosc")
# else:
#     print("Jestes niepelnoletni!")

#
# # Zadanie 10
# x = int(input("Podaj pierwszą liczbe: "))
# y = int(input("Podaj drugą liczbe: "))
# znak = input("jakie działanie mam wykonać?: ")
#
# if znak == '+':
#     print(f'wynik: {x+y}')
# elif znak == '-':
#     print(f'wynik: {x-y}')
# elif znak == '*':
#     print(f'wynik: {x*y}')
# elif znak == '/':
#     if y == 0:
#         exit("Nie dzielimy przez 0")
#     else:
#         print(f'wynik: {x/y}')
#
# elif znak == '%':
#     print(f'wynik: {x%y}')
# else:
#     exit("nie dziala")

#
# # #Zadanie 11
#
# x = int(input("Podaj pozycje x: "))
# y = int(input("Podaj pozycje x: "))
#
# if x>100 or y>100:
#     print("Gracz znajduje sie poza plansza")
# elif x<=10 and y<=10:
#     print("Gracz jest w lewym gornym rogu")
# elif 90>x>10 and y<=10:
#     print("Gracz jest na gornej krawedzi")
# elif x>=90 and y<=10:
#     print("Gracz jest w prawym gornym rogu")
# elif x<=10 and 90>y>10:
#     print("Gracz jest na lewej krawedzi")
# elif x>=90 and 90>y>10:
#     print("Gracz jest na prawej krawedzi")
# elif x<=10 and y>90:
#     print("Gracz jest w lewym dolnym rogu")
# elif 90>x>10 and y>90:
#     print("Gracz jest na dolnej krawedzi")
# elif x>90 and y>90:
#     print("Gracz jest w prawym dolnym rogu")
# else:
#     print("Gracz jest w okolicy centrum")
#

x = int(input("Podaj pozycje x: "))
y = int(input("Podaj pozycje y: "))

if x <= 10:
    pos_x = 'left'
elif x >= 90:
    pos_x = 'right'
else:
    pos_x = ''

if y <= 10:
    pos_y = 'top'
elif y >= 90:
    pos_y = 'bottom'
else:
    pos_y = ''

if pos_x and pos_y:
    print(pos_x, pos_y, 'corner')
elif pos_x or pos_y:
    print(pos_x, pos_y, 'edge')
else:
    print ('center')