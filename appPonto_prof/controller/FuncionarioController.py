from appPonto_prof.model.funcionario import Funcionario

class FuncionarioController:

    def __init__(self, nome, cpf, data_nascimeto, cargo, id, senha, nivel):

        self.nome = nome
        self.cpf = cpf
        self.data_nascimeto = data_nascimeto
        self.cargo = cargo
        self.id = id
        self.senha = senha
        self.nivel = nivel

        self.funcionario = Funcionario(self.nome, self.data_nascimeto, self.cargo, self.id, self.senha, self.nivel)
        Funcionario.cpf = cpf
        self.criarTxtFuncionario(self.funcionario)

    def criarTxtFuncionario(self, funcionario):
        with open("tabela/funcionario.txt", "a") as file:

            file.write(funcionario.__str__())
            return f"Arquivo criado com sucesso | {file.name}"
