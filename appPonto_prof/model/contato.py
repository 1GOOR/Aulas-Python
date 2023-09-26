import appPonto_prof.util.verificador as verifica

class Contato():

    def __init__(self, email, telefone, rua, numero, bairro, cep, cidade, estado):

        self.__email = email
        self.__telefone = telefone
        self.__rua = rua
        self.__bairro = bairro
        self.__numero = numero
        self.__cep = cep
        self.__cidade = cidade
        self.__estado = estado

    #EMAIL
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    #TELEFONE
    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):

        if verifica.validarTelefone(telefone) != None:
            self.__telefone = verifica.validarTelefone(telefone)
        else:
            print("Telefone invalido")

#RUA
    @property
    def rua(self):
        return self.rua

    @rua.setter
    def rua(self, rua):
        self.__rua = rua

#BAIRRO
    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

#NUMERO
    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

#CEP
    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, cep):
        self.__cep = cep

#CIDADE
    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

#ESTADO
    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado


    def __str__(self) -> str:
        return f"{self.__email} {self.__telefone} {self.__rua} {self.__numero} {self.__bairro} {self.__cep} {self.__cidade} {self.__estado}"
