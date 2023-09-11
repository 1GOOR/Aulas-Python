# Criar uma função que cadastre uma lista de produtos, onde cada produto vai ter :
# Tipo
# Descrição
# Quantidade
# Você deve validar o campo quantidade para ser um int

def mensagem():
    print("   para cadastrar um produto digite -> 1 ")
    print("   para ver todos os produto digite -> 2 ")
    print("   para sair digite -> 3 ")

def produto(tipo, nome, quantidade):
    if tipo.isalpha():
        if nome.isalpha():
            if quantidade.isdigit():
                int(quantidade)
                return {"tipo": tipo, "nome": nome, "quatidade": quantidade}
            else:
                print("Quantidade invalida")
        else:
            print("nome invalido")
    else:
        print("Tipo invalido")


produtos = []

while True:

    mensagem()

    resposta = input("opcao: ")

    if resposta == "1":
        tipo = input("Qual o Tipo do produto: ")
        nome = input("Qual o nome do produto: ")
        quantidade = input("Qual a quantidade: ")

        produto(tipo, nome, quantidade)

        if isinstance(produto(tipo, nome, quantidade), dict):
            produtos.append(produto(tipo, nome, quantidade))
            print("Produto cadastrado")


    elif resposta == "2":

        for i in produtos:
            print(f"")

        #for posicao in produtos:
        #    #print(f"{posicao.values()}")

    elif resposta == "4":

        for i in produtos:
            num = int(i.get("quatidade"))
            print(num)

    elif resposta == "3":
        print(f"voce saiu do sistema\n\n\n")
        break

    else:
        print("Resposta invalida")

print(produtos)