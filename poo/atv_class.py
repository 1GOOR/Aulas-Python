import datetime

class Usuario:

    def __init__(self, nome, rg, data_nasc, vigor=5): #pode se definir um valor padro para atributos,para serem usados quando na criacao do objeto nao forem passados os parametros
        self.nome: str = nome
        self.rg: str = rg
        self.data_nasc: str = data_nasc
        self.vigor: int = vigor


    def correr(self):
        self.vigor -= 1


    def calcularIdade(self):

        try:
            idade = int(datetime.datetime.today().year) - int(self.data_nasc)
            return idade

        except Exception as e:
            print("Erro")


user_1 = Usuario("ze", "1245679", "2000", 9)

print(user_1.vigor)
print(user_1.data_nasc)
print(user_1.calcularIdade())
