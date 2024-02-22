
class Contato:

    def __init__(self, telefone=None, email=None):
        self.__telefone = telefone
        self.__email = email
    @property
    def getTelefone(self):
        return self.__telefone
    @property
    def getEmail(self):
        return self.__email
    def addContato(self,telefone,email):
        self.__email = email
        self.__telefone = telefone
class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.contato = Contato()

    @property
    def getNome(self):
        return self.__nome
    @property
    def getCPF(self):
        return self.__cpf
    @getNome.setter
    def setNome(self, nome):
        self.__nome = nome
    @getCPF.setter
    def setCPF(self, cpf):
        self.__cpf = cpf


if __name__ == '__main__':

    a = Pessoa("ze",cpf="1211211")

    print(a.contato.getEmail)

    a.contato.addContato(telefone="11 995948", email="ze@gmail.com")


    print(a.contato.getEmail)