from datetime import datetime


def verificarValor(valor):
    valor = valor.strip()
    if valor.isdigit() or str.isdigit(valor.replace(".", "")) or str.isdigit(valor.replace(",", "")):
        valor = valor.replace(",", ".")
        return float(valor)


def receita(descricao, valor, data, categoria):
    descricao = descricao.strip()
    categoria = categoria.strip()
    # eu vou criar uma função para validar meu valor
    if isinstance(verificarValor(valor), float):
        return {"descricao": descricao, "data": data, "categoria": categoria, "valor": verificarValor(valor)}

    else:
        print("Valor digitado errado")


receitas = list()

while True:
    descricao = input("Digite a descrição da receita: ")
    valor = input("Digite o valor da receita:  ")
    data = datetime.today().date()
    categoria = input("Digite a categoria da receita:  ")
    if isinstance(receita(descricao, valor, data, categoria), dict):
        receitas.append(receita(descricao, valor, data, categoria))
    else:
        print("Não foi possivel cadastrar")

    resp = input("Deseja sair sim ou não").strip()[0].upper()

    if resp == "S":
        break


for i in receitas:
    print(f"{i.get('descricao'.title())}\n{i.get('categoria'.title())}\n{i.get('valor')}\n{i.get('data')}")
    print("-"*14)
