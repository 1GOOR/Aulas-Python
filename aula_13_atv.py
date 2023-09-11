"""try:
    pessoas = []


except FileExistsError as e:
    pass
"""
BD = open("atv_13_BD", "a")
while True:
    nome = input("Informe um nome: ")
    #idade = input(f"informe a idade de {nome}: ")
    BD.write(nome)
