
# OOP - Programowanie obiektowe

class DummyProduct:
    pass

product = DummyProduct()
print(type(product))

class Product:

    def __init__(self, id, name, price, descr=""):
        self._id = id # niby - protected
        self._name = name # niby - protected
        self._price = price # niby - protected
        self._descr = descr

    def get_info(self):
        return f"{self._id} - {self._name} - {self._price} - {self._descr}"
    
    def __str__(self):
        return f"{self._id} - {self._name} - {self._price} - {self._descr}"

    def set_price(self, new_price):
        self._price = new_price

product = Product(1, "Mleko", 2.99, "Opis mleka")
#product._id = 1
#product._name = "Mleko"
#product._price = 2.99
#product._Product__descr = "Opis mleka"
print(product.get_info())
product.set_price(3.14)
print(product.get_info())
print(product)
