import datetime

import appPonto_prof.util.verificador as verifica

class Funcionario:

    def __init__(self, nome, data_nasc, cargo, contato, senha, nivel):

        #usa o '__' para privar os atributos da instancia

        self.__nome = nome
        self.__cpf = None
        self.__data_nasc = data_nasc
        self.__cargo = cargo
        self.__contato = contato
        self.__senha = senha
        self.__nivel = nivel

   #Decoreitor
    @property # -> getter usado para pegar valores
    def nome(self):
        return self.__nome

    @nome.setter # setter usado para alter o valor de um atributo
    def nome(self, nome):
        self.__nome = nome
    ##############################################################
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if verifica.validarCpf(cpf) != None:
            self.__cpf = verifica.validarCpf(cpf)
        else:
            print("CPF invalido")
    ##############################################################
    @property
    def data_nasc(self):
        return self.__data_nasc

    @data_nasc.setter
    def data_nasc(self, data_nac):
        self.__data_nasc = data_nac
    ##############################################################
    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo
    ##############################################################
    @property
    def contato(self):
        return self.__contato

    @contato.setter
    def contato(self, contato):
        self.__contato = contato
    ##############################################################
    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha
    ##############################################################
    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, nivel):
        self.__nivel = nivel


    def __str__(self):
        return f"{self.nome} {self.cpf} {self.data_nasc} {self.cargo} {self.contato} {self.senha} {self.nivel}"


    def idade(self):
        anoAtual = int(datetime.datetime.today().year)
        return anoAtual - int(str(self.data_nasc).split("/")[2])


"""nome = "ze"
cpf = "1211324"
data_nasc = "20/01/2000"
cargo = "adm"
contato = 1
senha = "123"
nivel = "adm"

f1 = Funcionario(nome, cpf, data_nasc, cargo, senha, nivel)

print(f1.idade())"""