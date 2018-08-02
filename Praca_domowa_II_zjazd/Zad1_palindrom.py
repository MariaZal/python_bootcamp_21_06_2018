# Zaimplementuj funkcję, która sprawdzi czy podany napis jest palindromem (napis czytany tak samo od
# lewej, jak i od prawej).
# Podpowiedź: do odwrócenia napisu możemy wykorzystać mechanizm wycinania (ang. slicing).
# Przykład użycia:
# >>>	czy_palindrom('kajak')
# True
# >>>	czy_palindrom('python')
# False

def czy_palindrom(wyraz):
    wyraz_odw=wyraz[::-1]
    if wyraz_odw==wyraz:
        print(f'"{wyraz}" to jest palindrom')
        return True
    else:
        print(f'"{wyraz}" to nie jest palindrom')
        return False


czy_palindrom('ala')
czy_palindrom('magda')

def test_dla_palindromu():
    assert czy_palindrom('kajak')==True

def test_dla_niepalindromu():
    assert czy_palindrom('python')==False