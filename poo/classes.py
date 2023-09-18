#trabalhando com classes
"""
O que é uma classe

Class é uma abestracao do mundo real na programaco

.medodos tem atributos e me

"""

class Pessoa1:
    nome: str
    data_nasc:str
    rg:str
    tel:str


class Pessoa:

    def __init__(self, nome, data_nasc, rg, tel):
        self.nome: str = nome
        self.data_nasc: str = data_nasc
        self.rg: str = rg
        self.tel: str = tel


pessoa_1 = Pessoa1() # Criando um objeto Pessoa e Atribuindo o nome de 'pessoa_1'

pessoa_1.nome = "igor"
pessoa_1.data_nasc = "23/06/2003"
pessoa_1.rg = "15.935.782-8"
pessoa_1.tel = "11 935861-7698"

print(pessoa_1.nome)

try:
    pessoa_2 = Pessoa1()
    print(pessoa_2.nome)

except Exception as e:
    print(e)

pessoa_3 = Pessoa("ze", "20/06/2000", "156852364", "11 4985444")

print(pessoa_3.nome)