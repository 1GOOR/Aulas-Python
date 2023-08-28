
usuarios = list()

while True:
    nome = input("Qual o seu nome: ")
    while not nome.isalpha():
        nome = input("Informe seu nome novamente: ")

    rg = input("infome seu RG: ")

    data_nasc = input("Qual a data do seu nascimeto")
    while not data_nasc.isdigit():
        data_nasc = input("informe a data de nascimento novamente")

    telefones = list()
    tel_1 = input("Informe o primeiro telefone")
    tel_2 = input("Informe o segundo telefone")
    while not tel_1.isnumeric() or not tel_2.isnumeric():
        if not tel_1.isnumeric():
            tel_1 = input("Informe o primeiro telefone novamete")
        if not tel_2.isnumeric():
            tel_2 = input("Informe o segundo telefone novamete")
    telefones.append(tel_1)
    telefones.append(tel_2)

    dicionario = {"nome": nome, "rg": rg, "data_nasc": data_nasc, "telefones": telefones}
    usuarios.append(dicionario)

    resposta = input("Sim ou Nao").strip()[0].lower()
    if resposta == "n":
        break

print(f"{usuarios}")


