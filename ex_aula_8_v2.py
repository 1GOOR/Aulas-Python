import datetime

#versao 2

usuarios = list()

print(f"Seja bem Vidndo!!")

while True:  #loop para

    print("-"*13, "Menu", "-"*13)
    print("""
    Para cadastrar digite -> 1 
    Para listar os usuarios degite -> 2
    Para sair do sistema digite -> 3 
     
    """)

    btn = input("digite a opção desejado: ")

    if btn == "1": #Botao para cadastrar usuarios

        nome: str = input(f"Nome:")
        rg: str = input(f"RG: ")

        ano_nasc: str = input("Ano de nascimeto: ")
        #Tranformar

        tel_1: str = input("Digite o seu telefone: ")
        tel_2: str = input("Digite o seu telefone: ")

        telefone = [tel_1, tel_2] #add telefone na lista de telefone

        #despesa
        despesas = list()

        #loop para cadastrar varios despesas

        print("-"*8, "Cadastro de Despesas", "-"*8)
        while True:

            descricao: str = input("descrição da Despesa: ")

            #tratar o valor
            valor: str = input("Qual o valor: R$ ")

            data_despesa = datetime.date.today() #pegando a data do sistema para cadastrar as despesas

            despesa = {"descricao": descricao, "valor": valor, "data_despesa": data_despesa}

            despesas.append(despesa) #add despesa dentro da despesas(s)

            resposta = input("Deseja continuar cadastrando: ").strip()[0].upper()

            if resposta == 'N':
                break

        usuario = {"nome": nome, "rg": rg, "data_nascimeto": ano_nasc, "telefones": telefone, "despesas": despesas}

        usuarios.append(usuario)

    elif btn == "2": #botao para listar os usuarios

        print("-" * 10, "Lista de usuarios", "-" * 10)
        if len(usuarios) <= 0:
            print("nenhum usuario cadastrado.")
        else:
            for index in usuarios:
                #este for percorre os usuarios
                #pegando os valores individualmete de usuarios e atribuindo a index e printado ele

                print(f"Nome: {index['nome']}")
                print(f"RG: {index['rg']}")
                print(f"Idade:{datetime.date.today().year - int(index['data_nascimeto'])}")
                print("="*8, "dados de contato", "="*8)
                print(f"Telefone 1 {index['telefones'][0]} | Telefone 2 {index['telefones'][1]}")

                print("-"*10, " despesas ", "-"*10)

                #percorrer as despesas de usuario

                for index in usuario['despesas']: #atribuindo os valores de usuario despesas para varial index

                    #pegando os itens de index no caso: descricao e valor

                    #descricao|valor
                    for chave, valor in index.items():

                        if chave == "valor":
                            print(f"{chave}: R$ {float(valor)}")
                        else:
                            print(f"{chave}: {valor}")

                        print("------------------")

    elif btn == "3":
        break
