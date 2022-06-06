

"""This module is a collection of product classes which will allow easy creation and editing of items with their associated prices"""


## Imports




## Classes 

class Product:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

## Method
    def multiple(self):
        amount = int(input())
        self.price *= amount    
    
class Sandwich(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)

class Soft_drinks(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)
        

class Snacks(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)

class Adult_drinks(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)

class Confec(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)


