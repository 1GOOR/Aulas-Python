#funcao

import datetime

""""
ano_nasc: str

def idade(ano_nasc):
    if ano_nasc.isdigit() and len(ano_nasc) == 4
 """
# funcoes sem retorno sao chamadas de procedimentos

def mensagem(mensagem):
    print(mensagem)#esta printando o parametro da funcao


mensagem("Hello World!!")

print("""

Para imprimir na tela digite -> 1
Para salvar digite -> 2
Para sair digite  -> 3

""")


#terceira

def pessoa(nome, idade, rg):

    if len(nome) > 1 and nome.isalpha:

        if idade.isdigit() and len(idade):

            if int(idade) <= 120:

                if rg.isdigit():

                    if len(rg) >= 8 and len(rg) < 11:

                        return {"nome":nome, "idade":idade, "rg":idade}

                    else:
                        print("rg invalido:")
                else:
                    print("idade invalida")
        else:
            print("idade invalida")

    else:
        print("nome invalido")

pessoas = []

x = 0

while True:
    nome = input("Informe um nome: ")
    idade = input("informe a idade: ")
    rg = input("informe o rg: ")

    pessoa(nome, idade, rg)

    if isinstance(pessoa(nome, idade, rg), dict):
        pessoas.append(pessoa(nome, idade, rg))

    if x == 1:
        break
    x = x + 1

print(pessoas)