#-*- coding: latin-1 -*-

import PySimpleGUI as sg

def janelaLogin():

    layout = [

        [sg.Push(background_color="#2F6073"), sg.Text("LOGIN", font="Helvetica 20", text_color="#2F6073", background_color="#2F6073"),sg.Push(background_color="#2F6073")],
        [sg.Push(background_color="#2F6073"), sg.Image("img/login.png", background_color="#2F6073"), sg.Push(background_color="#2F6073")],
        [sg.Image("img/1.png", background_color="#2F6073"), sg.Text("Login", size=7, background_color="#2F6073", text_color="#E8BF58", font=" roboto 20"),sg.Input(size=20, background_color="#ffffff", font=" roboto 15", key="-LOGIN-")],
        [sg.Image("img/2.png", background_color="#2F6073"), sg.Text("Senha", size=7, background_color="#2F6073", text_color="#E8BF58", font=" roboto 20"),sg.Input(size=20, background_color="#ffffff", font=" roboto 15", password_char="*", key="-SENHA-")],
        [sg.Push(background_color="#2F6073"), sg.Button("Entrar", size=10, font="arial 15", pad=25, mouseover_colors=("#E8BF58", "#FFE054"), button_color="#E8BF58", key="-ENTRAR-"), sg.Push(background_color="#2F6073")],
        [sg.Push(background_color="#2F6073"), sg.Text("Recuperar Senha", background_color="#2F6073", text_color="#E8BF58"),sg.Push(background_color="#2F6073")]

    ]

    return sg.Window("Tela Login", layout, background_color="#2F6073", finalize=True)


def recuperarSenha():

    layout=[

    [sg.Push(background_color="#2F6073")], [sg.Image("img/recuperar.png", background_color="#2F6073")], [sg.Push(background_color="#2F6073")],
    [sg.Text("Entre com seu CPF", background_color="#2F6073", text_color="#E8BF58", font=" roboto 11")], [sg.Input(key="-CPF-", size=20, background_color="#ffffff", font=" roboto 15")],
    [sg.Button("Recuperar Senha", font="arial 15", pad=25, mouseover_colors=("#E8BF58", "#FFE054"), button_color="#E8BF58")], [sg.Text("", visible=False, background_color="#2F6073", text_color="#E8BF58")]

    ]
    return sg.Window("Recuperar Senha", layout, background_color="#2F6073", finalize=True)


def telacadastro():

    cargos = ["Gerente", "TI", "Administração", "Recursos Humanos"]

    layout = [
        [sg.Image("img/logo.png", background_color="#2F6073"),
         sg.Push(background_color="#2F6073"),
         sg.Text("CADASTRO DE FUNCIORIO", font=("Helvetica", 18), text_color="#ffffff", background_color="#2F6073"),
         sg.Push(background_color="#2F6073")],

        [sg.Push(background_color="#2F6073")],
        [sg.Push(background_color="#2F6073")],
        [sg.HSep()],
        [sg.Push(background_color="#2F6073")],
        [sg.Push(background_color="#2F6073")],

        [sg.Text("Nome", size=5, background_color="#2F6073", font=("Helvetica", 14)),
         sg.Input(size=(50, 30), background_color="#ffffff", font=("Helvetica", 14)),
         sg.Text("Nascimeto", background_color="#2F6073", font=("Helvetica", 14)),
         sg.Input(size=(15, 15), background_color="#ffffff", font=("Helvetica", 14))],

        [sg.Text("CPF", size=5, text_color="#FFFFFF", font=("Helvetica", 14), background_color="#2F6073"),
         sg.Input(size=30, background_color="#FFFFFF", font=("Helvetica", 14)),
         sg.Text("Cargo", size=5, text_color="#FFFFFF", font=("Helvetica", 14), background_color="#2F6073"),
         sg.Combo(cargos, size=16, default_value="Escolha um cargo", font=("Helvetica", 14)),
         sg.Text("Cadastrar contato", text_color="#FFFFFF", font=("Helvetica", 14), background_color="#2F6073"),
         sg.Image("img/contato.png", background_color="#2F6073")],

        [sg.Push(background_color="#2F6073")],
        [sg.Push(background_color="#2F6073")],
        [sg.HSep()],
        [sg.Push(background_color="#2F6073")],
        [sg.Push(background_color="#2F6073")],

        [sg.Text("Senha", size=5, background_color="#2F6073", text_color="#FFFFFF", font=("Helvetica", 14)),
         sg.Input(size=(30, 30), background_color="#ffffff", font=("Helvetica", 14), password_char=" "),
         sg.Text("Nivel", size=5, background_color="#2F6073", text_color="#FFFFFF", font=("Helvetica", 14)),
         sg.Radio("ADM", "Ratio1", text_color="#FFFFFF", font=("Helvetica", 14), background_color="#2F6073"),
         sg.Radio("Comum", "Ratio1", default=True, text_color="#FFFFFF", font=("Helvetica", 14), background_color="#2F6073"),
         sg.Button("Deletar"),
         sg.Button("Atualizar", size=20),
         sg.Input(),
         sg.Button("Buscar")
         ]
    ]
    return sg.Window("Recuperar Senha", layout, background_color="#2F6073", finalize=True)

def contatos():

    estados = ["SP", "RJ", "BA", "BH", "PA", "RS"]

    layout = [
        [sg.Image("img/logo.png", background_color="#2F6073"),
         sg.Push(background_color="#2F6073"),
         sg.Text("CONTATOS", font=("Helvetica", 18), text_color="#ffffff", background_color="#2F6073"),
         sg.Push(background_color="#2F6073")],

        [sg.HSep()],

        [sg.Text("Email", size=6, background_color="#2F6073", text_color="#FFFFFF", font=("Helvetica", 14)),
         sg.Input(size=35, background_color="#ffffff", font=("Helvetica", 14)),
         sg.Text("Telefone", size=8, background_color="#2F6073", text_color="#FFFFFF", font=("Helvetica", 14)),
         sg.Input(size=22, background_color="#ffffff", font=("Helvetica", 14))],

        [sg.Text("Rua", size=6, background_color="#2F6073", text_color="#FFFFFF", font=("Helvetica", 14)),
         sg.Input(size=27, background_color="#ffffff", font=("Helvetica", 14)),
         sg.Text("Nº", size=2, background_color="#2F6073", text_color="#FFFFFF", font=("Helvetica", 14)),
         sg.Push(background_color="#2F6073"),
         sg.Input(size=3, background_color="#ffffff", font=("Helvetica", 14)),
         sg.Text("CEP", size=8, background_color="#2F6073", text_color="#FFFFFF", font=("Helvetica", 14)),
         sg.Input(size=22, background_color="#ffffff", font=("Helvetica", 14))],

        [sg.Text("Estado", size=6, background_color="#2F6073", text_color="#FFFFFF", font=("Helvetica", 14)),
         sg.Combo(estados, size=3, default_value="SP", font=("Helvetica", 14)),
         sg.Text("Cidade", size=6, background_color="#2F6073", text_color="#FFFFFF", font=("Helvetica", 14)),
         sg.Push(background_color="#2F6073"),
         sg.Input(size=22, background_color="#ffffff", font=("Helvetica", 14)),
         sg.Text("Bairro", size=8, background_color="#2F6073", text_color="#FFFFFF", font=("Helvetica", 14)),
         sg.Input(size=22, background_color="#ffffff", font=("Helvetica", 14))]

    ]
    return sg.Window("Contatos", layout, background_color="#2F6073", finalize=True)


def baterPonto():

    cabecalho = ["Entrada", "Saida Alimentaçao", "volta alimentaçao", "Saida"]

    layout = [
        [sg.Image("img/voltar.png", background_color="#2F6073", enable_events=True),
         sg.Image("img/logo.png", background_color="#2F6073"),
         sg.Push(background_color="#2F6073"),
         sg.Text("Bater Ponto", font=("Helvetica", 18), text_color="#ffffff", background_color="#2F6073"),
         sg.Push(background_color="#2F6073")],

        [sg.HSep()],

        [sg.Text("CPF", text_color="#FFFFFF", font=("Helvetica", 14), background_color="#2F6073"),
         sg.Input(size=15, background_color="#ffffff", font=("Helvetica", 14)),
         sg.Image("img/pesquisa.png", background_color="#2F6073", enable_events=True),
         sg.Text("Data", text_color="#FFFFFF", font=("Helvetica", 14), background_color="#2F6073"),
         sg.Input(size=8, background_color="#ffffff", font=("Helvetica", 14), disabled=True),
         sg.Image("foto/usuario.png", background_color="#2F6073")
         ],

        [sg.HSep()],

        [sg.Button("Entrada", size=12),
         sg.Button("Saida Alimentação", size=16),
         sg.Button("Volta Alimentação", size=16),
         sg.Button("Saida", size=12)],

        [sg.Table(headings=cabecalho, values=[])]

    ]
    return sg.Window("Tela bater ponto", layout, background_color="#2F6073", finalize=True)


def janelaMenu():
    layout = [
        [sg.Image("img/voltar.png", background_color="#2F6073", enable_events=True),
         sg.Image("img/logo.png", background_color="#2F6073"),
         sg.Push(background_color="#2F6073"),
         sg.Text("MENU", font=("Helvetica", 18), text_color="#ffffff", background_color="#2F6073"),
         sg.Push(background_color="#2F6073")],

        [sg.HSep()],

        [sg.Button("Cadastrar", key="-CADASTRAR-")],
        [sg.Button("Listar Funcionario", key="-LISTAR-")],
        [sg.Button("Bater Ponto", key="-PONTO-")]

    ]
    return sg.Window("Menu", layout, background_color="#2F6073", finalize=True)


telalogin, telacasdasto, telacontato, telarecuperasenha, telabateponto, telamenu = janelaLogin(), None, None, None, None, None


while True:

    window, events, values = sg.read_all_windows()

    if window == telalogin and events == sg.WINDOW_CLOSED:
        break

    if window == telalogin and events == "-ENTRAR-":
        nome = values["-LOGIN-"]
        senha = values["-SENHA-"]

        if nome in ["carlos", "maria", "pedro"] and senha == "123":
            sg.Popup("Seja Bem Vindo!", nome)
            telamenu = janelaMenu()
            telalogin.hide()

    ###############################################################

    if window == telamenu and events == "-CADASTRAR-":
        telamenu.hide()
        telacasdasto = telacadastro()


    if window == telamenu and events == sg.WINDOW_CLOSED():
        break

    if window == telacasdasto and events == sg.WINDOW_CLOSED():
        break