import datetime

# Tratamento de e
"""
try:
    divisao = 2/0
    print(divisao)
    lista = [12, 34, 56]
    print(lista[3])
except Exception as variavel:
    print("mensagem de erro:", variavel)

for i in range(10):
    print(i)


###########################################

pessoas = []

def get():
    nome = input("Informe um nome: ")
    data_nasc = input(f"Informe a data de nascimeto de {nome}: ")
    print("")
    pessoa = [nome, data_nasc]
    pessoas.append(pessoa)


def idade (data_nasc:list):

    for i in data_nasc:

        print(i[0])
        try:
            data = int(datetime.datetime.today().year)
            idade = data - int(i[1])
            print(idade)
        except Exception as e:
            print("idade invalida")
        finally:
            print("-"*15)

def mensagen():
    print(f"Para cadastrar um pessoa digite -> 1")
    print(f"Para para mostrar todas as pessoa digite -> 2")


while True:
    mensagen()
    resposta = input(f"Resposta: ")
    print("")

    if resposta == "1":
        get()
    elif resposta == "2":
        idade(pessoas)
    else:
        print("respota invalida")

"""
##########################################################

alunos = list()

def cad_aluno():
    notas = list()
    nome = input("Qual o nome do aluno: ")

    for i in range(4):
        while True:
            try:
                nota = int(input(f"Informe a {i}º: "))
                notas.append(nota)
                break
            except Exception as e:
                print(f"{e} Nota invalida")

    aluno = [nome, notas]
    alunos.append(aluno)

def cal_media_um(alun:list):

    resp = input("qual o nome do aluno")
    for i in alun:
        if i.__contains__(resp):
            for x in i[1]:
                print(x)
        else:
            break

while True:
    cad_aluno()
    cal_media_um(alunos)