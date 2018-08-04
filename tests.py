from kartkówka import Animal, Cat, Dog

def test_everything():
    animal = Animal("Strange something", 1000)
    assert animal.name == "Strange something"
    assert animal.age == 1000
    assert animal.s
