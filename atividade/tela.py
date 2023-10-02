import PySimpleGUI as sg

#Cadastro de Produtos

#produto -> Tipo, nome, preco, quantidade

class Produto:

    def __init__(self, tipo, nome, preco, quantidade):
        self.tipo = tipo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


def printTabela():
    with open("produtos.txt", "r+") as file:
        lista = []
        for linha in file:
            linha.replace("\n", "")
            arquivo = linha.split(" ")
            lista.append(arquivo)
        return lista


def telaCadastro():

    cabecalho = ["Tipo", "Nome", "Preço", "Quantidade"]
    tipos = ["Main-bord", "CPU", "RAM", "VGA"]

    layout = [

        [sg.Text("Produto", size=6), sg.Combo(tipos, size=13, default_value="Produto", key="-PRODUTO-"),
         sg.Text("Nome", size=6), sg.Input(key="-NOME-", size=19)],

        [sg.Text("Preço", size=6), sg.Input(key="-PRECO-", size=15),
         sg.Text("Quantidade", size=8), sg.Push(), sg.Input(key="-QUANTIDADE-", size=16)],

        [sg.Push(), sg.Button("Cadastrar", key="-CADASTRAR-"),
         sg.Push(), sg.Button("Busca", key="-BUSCA-"),sg.Push(), sg.Button("Total", key="-TOTAL-"), sg.Push(), sg.Input(size=15, key="-BSC-"), sg.Push()],

        [sg.HSep()],

        [sg.Table(headings=cabecalho, values=printTabela(), auto_size_columns=False, def_col_width=10, key="-TABELA-")]
    ]
    return sg.Window("tela", layout, finalize=True)

"""def valorPecas():
    with open("produtos.txt", "r+") as file:



        contador = 0
        for linha in file:
            if linha[1].__contains__(resposta):
                print("encontrou")"""



janela = telaCadastro()

while True:

    envents, values = janela.read()

    if envents == sg.WINDOW_CLOSED:
        break

    if envents == "-CADASTRAR-":

        produto = values["-PRODUTO-"]
        nome = values["-NOME-"]
        preco = values["-PRECO-"]
        quantidade = values["-QUANTIDADE-"]

        if (nome == "" or len(nome) < 3) or (preco == "") or (quantidade == ""):
            sg.Popup("Nao foi possivel cadastrar")
        else:
            with open("produtos.txt", "a+") as file:

                file.write(f"{produto} {nome} {preco} {quantidade}\n")

                sg.Popup("Cadastrado com sucesso!")
                janela["-PRODUTO-"].update(value="")
                janela["-NOME-"].update(value="")
                janela["-PRECO-"].update(value="")
                janela["-QUANTIDADE-"].update(value="")


            janela["-TABELA-"].update(values=printTabela())

    if envents == "-BUSCA-":
        
        with open("produtos.txt", "r+") as file:

            contador = 0
            resposta = values["-BSC-"]
            lista = []
            for linha in file:
                arquivo = linha.split(" ")
                lista.append(arquivo)

            for i in lista:
                if i[1] == resposta:
                    sg.Popup(f"Produto encontrado")
                elif len(lista) == contador+1:
                    contador = 0
                    sg.Popup(f"Produto nao encontrado")
                contador += 1


    if envents == "-TOTAL-":

        with open("produtos.txt", "r+") as file:
            contador = 0
            resposta = values["-BSC-"]
            lista = []
            for linha in file:
                arquivo = linha.split(" ")
                lista.append(arquivo)
            for i in lista:
                if i[1] == resposta:
                    valor = float(i[2])
                    qnt = float(i[3])
                    total = valor * qnt
                    sg.Popup(total)
                    break
                elif len(lista) == contador + 1:
                    contador = 0
                    sg.Popup(f"nao foi possivel calcular")
                    break
                contador += 1



