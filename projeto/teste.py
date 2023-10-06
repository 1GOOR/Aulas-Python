import PySimpleGUI as sg

class Evento:

    lista = []

    def __int__(self, nome, detalhe, data):

        self.__nome = nome
        self.__detalhe = detalhe
        self.__data = data

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def detalhe(self):
        return self.__detalhe

    @detalhe.setter
    def detalhe(self, detalhe):
        self.__detalhe = detalhe

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


    def cadastrar(self):

        key = self.nome

        layout = [
            sg.Button(button_text=self.nome, size=10, key=key)
        ]
        Evento.lista.append(layout)


class Botao():

    botoes = []

    def __init__(self, evento):
        self.evento = evento
        botao = [sg.Button(button_text=self.evento.nome)]
        Botao.botoes.append(botao)


def criarEvento(nome: str, detalhe: str, data: str):

    evento = Evento

    evento.nome = nome
    evento.data = data
    evento.detalhe = detalhe

    evento.cadastrar(evento)

    return evento

def criarEvento2(nome: str, detalhe: str, data: str):

    evento = Evento

    evento.nome = nome
    evento.data = data
    evento.detalhe = detalhe

    botao = Botao(evento)

    return botao


def menu(listas):
    layout = [
        listas,
        [sg.Text("ADM"), sg.Button("login")]
    ]
    return sg.Window("Teste", layout, finalize=True)

def telaDetalhe():

    layout = [

        [sg.Button("Next")]
    ]
    return sg.Window("detalhe", layout, finalize=True)


a = criarEvento("peça 1", "apenas testes", "16/02/2023")

b = criarEvento2("teste", "apenas teste", "20")

z = menu(Evento.lista)



print(a.detalhe)

print(b.botoes)

for i in b.botoes:
    print(i)

"""while True:

    envents, values = z.read()
"""