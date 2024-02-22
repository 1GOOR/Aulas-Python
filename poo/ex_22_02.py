from abc import ABC
class Pessoa(ABC):
    def __init__(self, nome):
        self.nome = nome
class Funcionario(Pessoa):
    def __init__(self, nome, registro):
        super().__init__(nome)
        self.registro = registro
class Cliente(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome)
        self.cpf = cpf
        self.livros = []
    def addLivro(self, livro):
        self.livros.append(livro)

    def ler(self, livro):
        return f"{self.nome} esta lendo o livro {livro.nome},que tem {livro.qntdPaginas} paginas"

    def __str__(self):
        return f"{self.nome} {self.cpf}"

    def verLivro(self):
        for i in self.livros:
            print(f"nome:{i.nome} | descriçao:{i.descricao} | paginas:{i.qntdPaginas}")


class Livro:
    def __init__(self,nome, descricao, qntdPaginas):
        self.nome = nome
        self.descricao = descricao
        self.qntdPaginas = qntdPaginas



if __name__ == '__main__':

    funcionario_1 = Funcionario(nome="fernando", registro="12")

    clinte_1 = Cliente("ze", "123.456.789-78")

    clinte_2 = Cliente("ana", "789.456.145-87")

    clinte_3 = Cliente(nome="gui", cpf="456.987.321-63")

    livro_1 = Livro("caminho das trevas", "descricao generica", "200")

    livro_2 = Livro("POO", "Progamaçao orientada a objeto", "600")

    livro_3 = Livro("turma do dudão", "apenas a turma do dudao", "26")

    livro_4 = Livro("one piece", "pirataria", "1500")

    clinte_1.addLivro(livro_1)

    clinte_1.addLivro(livro_2)


    clinte_3.addLivro(livro_3)

    clinte_3.addLivro(livro_4)

    clinte_3.addLivro(livro_2)

    clinte_3.addLivro(livro_1)

    print(clinte_3.verLivro())






