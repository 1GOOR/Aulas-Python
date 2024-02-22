
class Produto:
    def __init__(self, descript, price, brand):
        self.descript = descript
        self.price = price
        self.brand = brand

    def __str__(self):
        return f'descript:{self.descript} R${self.price} brand:{self.brand}'

