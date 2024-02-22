from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    @abstractmethod
    def punchTheClock(self, hour):
        pass

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, registro):
        super().__init__(nome, cpf)
        self.registro = registro
        self.hora = None

class Gerente(Funcionario):
    def __init__(self, nome, cpf, registro, setor):
        super().__init__(nome, cpf, registro)
        self.setor = setor

    def punchTheClock(self, hour):
        self.hora = hour

    def __str__(self):
        return f"{self.hora} {self.registro}"

if __name__ == '__main__':

    g1 = Gerente("fabio", "123456", registro="123", setor="vendas")

    print(g1)