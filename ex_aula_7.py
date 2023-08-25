import  datetime as dt
#                as ->

#Praticando

print("Seja bem vindo ao sistema\n")

login:str = input("Qual o seu login:")
senha:str = input("Senha: ")

clientes = list()

if login in ["pedro", "maria", "santos"] and senha == "123":

    while True:

        print(f"Menu\nCadastra Cliente 1\nIdade do Cliente 2\nmostrar os clientes no sistema 3\npesquisa por nome 4\nSair do sistema 9")

        menu = int(input("Qual acao: "))

        if menu == 1:
            print("cadastrando cliente\n")
            nome: str = input(print("Qual o nome do Clinte:"))
            rg: str = input(print(f"informe rg de {nome}:"))
            cpf: str = input(print(f"informe cpf de {nome}:"))
            data_nas: int = int(input(print(f"informe a data de nascimeto de {nome}:")))
            cliete = [nome, rg, cpf, data_nas] #
            clientes.append(cliete) # append() adiona uma linha na nossa lista

        if menu == 2:
            for i in range(len(clientes)):
                idade = dt.date.today().year - clientes[i][3]

        if menu == 3:
            for i in range(len(clientes)):
                print(clientes[i])

        if menu == 4:
            pequisa = input("Qual o nome do clinte: ")
            if cliete.count(pequisa):
                print(pequisa, " foi entrada")
            else:
                print("nao foi encontrado")

        if menu == 9:
            break
else:
    print("Login ou senha incorretas")
