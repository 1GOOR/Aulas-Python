from cliente import Customer
class ShoppingCart:
    def __init__(self, customer: Customer):
        self.customer = customer
        self.listProducts = []
    def addProducts(self, products):
        self.listProducts.append(products)


