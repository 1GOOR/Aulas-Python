import PySimpleGUI as sg

lista = []
class Evento:
    def __int__(self, nome, detalhe, data):

        self.__nome = nome
        self.__detalhe = detalhe
        self.__data = data

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def email(self, nome):
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

    def btn(self):
        layout = [
            sg.Button(button_text=self.nome, size=10, key=len(lista))
        ]
        lista.append(layout)

def criarEvento(nome: str, detalhe: str, data: str):

    evento = Evento

    evento.nome = nome
    evento.data = data
    evento.detalhe = detalhe

    evento.btn(evento)

    return evento

def menu(listas):
    layout = [
        listas,
        [sg.Text("ADM"), sg.Button("login")]
    ]
    return sg.Window("Teste", layout, finalize=True)

a = criarEvento("1", "outro", "16/12/2023")
b = criarEvento("ola", "apanas testes", "20/10/2023")
c = criarEvento("peca", "apanas testes", "20/10/2023")
d = criarEvento("p", "apanas testes", "20/10/2023")
e = criarEvento("peca", "apanas testes", "20/10/2023")


z = menu(lista)

while True:

    envents, values = z.read()