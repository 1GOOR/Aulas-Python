
class Customer:
    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf

    def __str__(self):
        return f'Cliente:{self.name}'