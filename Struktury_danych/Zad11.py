# ZADANIE 11

lista = []
while True:
    komenda = input('Wprowadź liczbę lub "K"')
    if komenda == "K":
        break
    else:
        lista.append(komenda)

# Inny sposob na rzutowanie
# zbior = set()
# for l in text:
#     zbior.add(int(l))

# rzutowanie
zbior = set((map(int, lista)))

# ilosc unikalnych liczb w tekscie = ilosc elementow w zbiorze 'zbior'
ilosc = zbior.__len__()
print(f'Wprowadziłeś {ilosc} unikalnych liczb')

# generowanie zbioru liczb partzystych od 0 - 100
parzyste = set(range(0, 101, 2))

# lista iloczynu zbiorow
parzyste_zbior = zbior & parzyste

print(f'W tym liczb parzystych jest {len(parzyste_zbior)}')
