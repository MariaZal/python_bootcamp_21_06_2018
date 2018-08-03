# Zadanie 1
# Zaimplementuj klasę Product przechowującą informację o cenie,
# nazwie oraz ID produktu. Zaimplementuj metodę wypisującą nazwę o produkcie na
# konsolę

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self. name = name
        self.price = price

    def print_info(self):
        print(f'Produkt "{self.name}" - id: {self.id}, cena: {self.price} PLN')

product = Product(1, 'woda', 10.99)
product.print_info()

def test_product():
    product = Product(1, 'woda', 10.99)
    assert product.id == 1
    assert product.name == 'woda'
    assert product.price == 10.99

# def test_product_print_info():
#     product = Product(1, 'woda', 10.99)