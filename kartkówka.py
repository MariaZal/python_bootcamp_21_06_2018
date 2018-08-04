class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        return 'knock knock'

    def __lt__(self, other):
        return self.age < other.age

animal = Animal("Strange something", 1000)


class Dog(Animal):
    def sound(self):
        return 'how how'


class Cat(Animal):
    def sound(self):
        return "...(sorry - that's cat!)"


cat = Cat("Albert", 7)
dog = Dog("Nina", 6)
assert (animal.sound())
print(dog.sound())
print(cat.sound())

cat > dog

print(bool(cat < dog))


def test_everything():
    animal = Animal("Strange something", 1000)
    assert animal.name == "Strange something"
    assert animal.age == 1000

