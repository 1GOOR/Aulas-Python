#dict dentro de dicts

alunos = [

    {"nome": "igor", "idade": 20, "cpf": "123.456.789-12"},
    {"nome": "gui", "idade": 28, "cpf": "214.776.072-35"},
    {"nome": "ana", "idade": 14, "cpf": "897.326.745-32"}

]

print(alunos[0]["nome"])

for n,valor in enumerate(alunos.values()):
    print(n)