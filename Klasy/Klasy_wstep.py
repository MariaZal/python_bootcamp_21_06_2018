# ĆWICZENIE 1

# napis="Ala"
#
# print((napis.lower()))
#
class MojaPierwszaKlasa:
    def __init__(self,imie):
        self.imie=imie
    def witaj(self):
        print(f'Hello {self.imie}')

moja_instancja = MojaPierwszaKlasa('Maria')
print(f'moja instancja: {moja_instancja}')
print(f'type: {type(moja_instancja)}')
print(f'moja instancja {moja_instancja.imie}')
moja_instancja.witaj()
#
# alicja = MojaPierwszaKlasa('Alicja')
#
# MojaPierwszaKlasa.witaj(alicja)
# alicja.witaj()


# ----------------------- ĆWICZENIE 2 -----------------------------------------

# class Przyklad:
#     def __init__(self,x):
#         print(f'Teraz jestem w srodku metody init dla przykladu {x}')
#         self.x = x
#     def metoda(self):
#         print('nie robie nic')
#
# przyklad = Przyklad('a')
# przyklad2 = Przyklad('b')
#
# print('instancja zostala utworzona')
# print(f'zmienna x instancji przyklad ma wartosc: {przyklad.x}')
# print(f'zmienna x instancji przyklad2 ma wartosc: {przyklad2.x}')
#
# print('to mozna zmienic')
#
# przyklad2.x = 4
#
# print(f'zmienna x instancji przyklad ma wartosc: {przyklad.x}')
# print(f'zmienna x instancji przyklad2 ma wartosc: {przyklad2.x}')

# # ----------------------- ĆWICZENIE 3 ---------------------------------------
# class Example:
#     def __init__(self, var1, var2):
#         self.first_var = var1
#         self.sceond_var = var2
#
#     def print_variables(self):
#         print(f'{self.first_var} {self.sceond_var}')
#
#
# e = Example('s', 2)
# e.print_variables()
#
# e2 = Example(123, 'abc')
# e2.print_variables()
#
# print(e)
#
# print(e2)


# ----------------------- ĆWICZENIE 4 ---------------------------------------
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         # return f'Person: {self.name}'
#         return 'Person: {}'.format(self.name)
#
# jack = Person('Jack', 82)
#
# str(jack)
# print(jack)

# ----------------------- PRZYKŁAD 4 ---------------------------------------
# class Example:
#     # These class has variables
#     name = 'Example class'
#     description = 'Just an example of a simple class'
#
#     def __init__(self, var1):
#         # This is an instance variable
#         self.instance_variable = var1
#
#     def show_info(self):
#         info = 'instance_variable: {}, name: "{}", description: {}'.format(self.instance_variable, Example.name,
#                                                                        Example.description)
#         print(info)
#
# inst1 = Example('foo')
# inst2 = Example('bar')
#
# inst1.show_info()
# inst2.show_info()
#
# Example.name = "Modified name"
#
# inst1.show_info()
# inst2.show_info()

# ----------------------- PRZYKŁAD 5 ---------------------------------------
# class Licznik:
#     counter = 0
#
#     def __init__(self, state):
#         Licznik.counter += 1
#         self.state = state
#
# ob1 = Licznik('active')
#
# ob2 = Licznik('deleted')
# print(ob2.counter)
# print(ob2.state)
# print(ob1.counter)
# print(ob1.state)

# ----------------------- PRZYKŁAD 6 ---------------------------------------
class Animal:
    """fco
    fcsd;lvfmds
    nvsd;nfvopsdfn
    f;nsdlfnhsdlfbnsldkf
    Dokumentacja klasy """
    def greet(self):
        print("Hello, I am an animal")

    @property
    def favorite_food(self):
        return 'beef'

    def walk(self):
        print("I am walking")
        self.greet()

class Dog(Animal):
    def greet(self):
        print('wof wof')

class Cat(Animal):
    def greet(self):
        print("miau miau")

    @property
    def favorite_food(self):
        print('fish')

animal = Animal()
animal.greet()
animal.walk()
print(f'{animal.favorite_food}')

dog = Dog()

dog.greet()
dog.favorite_food
dog.walk()

cat = Cat()
cat.greet()
cat.favorite_food
cat.walk()

help(Animal)
