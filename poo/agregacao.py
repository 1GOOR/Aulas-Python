from datetime import datetime
class ShoppingCart:

    def __init__(self, data=datetime.today(), cpf=None):

        self.cpf = cpf
        self.data = data
        self.__products = []

    @property
    def getProducts(self):
        return self.__products

    @getProducts.setter
    def setProducts(self, product):
        self.__products.append(product)


class Product:

    def __init__(self, descipt: str, value: [float, int] = 0):

        self.descript = descipt
        self.value = value


if __name__ == '__main__':

    p1 = Product("rice", 30.00)
    p2 = Product("beans", 7.50)
    p3 = Product("Meat", 35.00)

    cart_one = ShoppingCart(cpf="333.333.333-67")

    cart_one.setProducts = p1
    cart_one.setProducts = p2
    cart_one.setProducts = p3

    print(cart_one.getProducts[0].descript)


    """for i in cart_one.getProducts:
        print(i.descript, i.value)"""

