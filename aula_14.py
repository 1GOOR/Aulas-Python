def criarArquivoPessoa():
    try:
        arquivo = open("pessoas.txt", "+r")
        arquivo.close()
        return True
    except Exception as e:
        print("O arquivo ja foi criado")
        return False


def addPessoas(nome, rg, ano_nasc):
    pessoa = f'{nome},{rg},{ano_nasc}'

    try:
        arquivo = open("pessoas.txt", "a")
        arquivo.write(pessoa)
        arquivo.close()
    except Exception as e:
        print("nao foi possivel add esta pessoa | Nome do erro ", e)


def listarPessoa():

    pessoas = list()

    try:
        arquivo = open("pessoas.txt", "r")
        for linha in arquivo.readlines():
            lista = linha.split(",")
            pessoa = {"nome":lista[0],"rg":lista[1],"data_nasc":lista[2]}
            pessoas.append(pessoa)
        return pessoas

    except Exception as e:
        print("nao foi possivel ler o arquivo | Nome do erro> ", e)


########################################################################

valor = criarArquivoPessoa()

while True:

    if valor:
        print("MENU".center(40, "-"))
        print("""
        opção 1 -> Cadastrar
        opção 2 -> Listar
        opção 3 -> Sair do sistema

        """)

        pergunta = input("Qual a opção que deseja: ")

        if pergunta == "1":
            print("Cadastrar".center(40, "="))
            nome = input("Nome: ")
            rg = input("Rg: ")

            try:
                ano_nasc = int(input("Data de nascinto: "))
                addPessoas(nome=nome, rg=rg, ano_nasc=ano_nasc)

            except Exception as e:
                print("Nao foi possivel Criar uma Pessoa | Nome do erro> ", e)

        elif pergunta == "2":
            for linha in listarPessoa():
                print(f"Nome: {linha['nome']}")
                print(f"RG:   {linha['rg']}")
                print(f"Ano:  {linha['data_nasc']}")
                print("#" * 20)

        elif pergunta == "3":
            break

        else:
            print("opcao invalida")

    else:
        break
