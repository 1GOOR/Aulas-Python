"""try:
    pessoas = []


except FileExistsError as e:
    pass
"""
BD = open("atv_13_BD.txt", "a")

for i in range(5):
    nome = input(f"Informe {i+1}º nome: ")
    BD.write(f'{nome}\n')
