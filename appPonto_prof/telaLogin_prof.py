# -*- coding: utf-8 -*-
import PySimpleGUI as sg

from appPonto_prof.controller.FuncionarioController import FuncionarioController

"""
#Pegar nomes de fontes
from tkinter import Tk, font
root = Tk()
font_tuple = font.families()
#Creates a Empty list to hold font names
FontList=[]
for font in font_tuple:
    FontList.append(font)
print(FontList)
"""
# Padroes
fonteTitulo = ("Helvetica ", 17, "bold")
fontTexto = ("Helvetica", 14)
cor_fundo = "#2F6073"


def janelaLogin():
    layout = [
        [sg.Push(background_color="#2F6073"), sg.Image("img/fundoApp.png", background_color="#2F6073"),
         sg.Push(background_color="#2F6073")],

        [sg.Image("img/dentro.png", background_color="#2F6073"),
         sg.Text("Login", size=7, background_color="#2F6073", text_color="#FFFFFF", font=fontTexto),
         sg.Input(size=20, background_color="#FFFFFF", font=" roboto 15", key="-LOGIN-")],

        [sg.Image("img/seguro.png", background_color="#2F6073"),
         sg.Text("Senha", size=7, background_color="#2F6073", text_color="#FFFFFF", font=fontTexto),
         sg.Input(size=20, background_color="#FFFFFF", font=" roboto 15", password_char="*", key="-SENHA-")],

        [sg.Push(background_color="#2F6073"),
         sg.Button("Entrar", size=10, font="arial 15", pad=25, mouseover_colors=("#FFFFFF", "#FFE054"),
                   button_color="#5AADBF", key="-ENTRAR-"),
         sg.Push(background_color="#2F6073")],

        [sg.Push(background_color="#2F6073"),
         sg.Text("Recuperar Senha!", background_color="#2F6073", text_color="#5AADBF", font=("Helvetica", 12),
                 enable_events=True, key="-CREATE_USER-"),
         sg.Push(background_color="#2F6073")]
    ]
    return sg.Window("Login", layout, background_color="#2F6073", finalize=True)


def janelaRecuperarSenha():
    layout = [

        [sg.Image("img/volte.png", background_color=cor_fundo, enable_events=True, key="-VOLTAR-")],

        [sg.Push(background_color="#2F6073"),
         sg.Image("img/mudarSenha.png", background_color="#2F6073"),
         sg.Push(background_color="#2F6073")],

        [sg.Text("Entre com o seu CPF", size=18, text_color="#FFFFFF", font=("Helvetica", 12),
                 background_color="#2F6073"),
         sg.Input(key="-CPF-", size=20, background_color="#FFFFFF", font="Helvetica 15")],

        [sg.Button("Recuperar Senha", size=15, font="arial 15", pad=8, mouseover_colors=("#FFFFFF", "#FFE054"),
                   button_color="#5AADBF"),
         sg.Text("", visible=False, background_color="#2F6073", text_color="#5AADBF")]
    ]
    return sg.Window("Recuperar Senha", layout, background_color="#2F6073", finalize=True)


def janelaCadastrarFuncionario():
    lista = ["Gerente", "Supervisor", "Suporte", "Segurança"]
    layout = [
        [sg.Image("img/volte.png", background_color=cor_fundo, enable_events=True, key="-VOLTAR-"),
         sg.Image("img/logoAPP.png", background_color="#2F6073"), sg.Push(background_color="#2F6073"),
         sg.Text("CADASTRAR FUNCIONARIO", background_color="#2F6073", font=fonteTitulo),
         sg.Push(background_color="#2F6073")],

        [sg.HSep()],

        [sg.Text("Nome", background_color="#2F6073", font=fontTexto, size=10),
         sg.Input(size=(70, 50), background_color="#FFFFFF", font=fontTexto, key="-NOME-"),
         sg.Text("Nascimento", background_color="#2F6073", font=fontTexto),
         sg.Input(size=20, background_color="#FFFFFF", font=fontTexto, key="-NASCIMENTO-"),
         sg.Image("img/calendar.png", background_color="#2F6073", key="-CALENDARIO-")],

        [sg.Text("CPF", background_color="#2F6073", font=fontTexto, size=10),
         sg.Input(size=20, background_color="#FFFFFF", font=fontTexto, key="-CPF-"),
         sg.Text("Cargo", background_color=cor_fundo, font=fontTexto, size=10),
         sg.Combo(lista, size=30, default_value="Escolha o Cargos", font=fontTexto, button_arrow_color="#FFFFFF", button_background_color="#2F6073", key="-GARGO-"),
         sg.Text("Cadastrar Contato", size=15, font=fontTexto, background_color=cor_fundo),
         sg.Image("img/contato.png", background_color="#2F6073", enable_events=True, key="-CONTATO-"),
         sg.Text("ID", size=3, font=fontTexto, background_color=cor_fundo),
         sg.Input(key="-ID_CONTATO-", size=6, background_color="#FFFFFF", font=fontTexto)],

        [sg.HSep()],

        [sg.Text("Senha", size=10, background_color=cor_fundo, font=fontTexto),
         sg.Input(font=fontTexto, size=15, password_char='*', key="-SENHA-"),
         sg.Text("Nivel", font=fontTexto, background_color=cor_fundo),
         sg.Radio("ADM", "radio1", font=fontTexto, background_color=cor_fundo),
         sg.Radio("COMUM", "radio1", default=True, font=fontTexto, background_color=cor_fundo),
         sg.Button("Cadastrar", font=fontTexto, size=20, key="-CADASTRAR-"),
         sg.Input(key="-PATH_PHOTO-"),
         sg.FileBrowse("ADD FOTO", initial_folder="img", target="-PATH_PHOTO-"),
         sg.Button("Carregar", key="-CARREGAR-")],

        [sg.HSep()],

        [sg.Push(background_color=cor_fundo),
         sg.Image("img/fundoCadastro.png", background_color=cor_fundo),
         sg.Push(background_color=cor_fundo),
         sg.Image(key="FOTO")],

        [sg.HSep()],

        [sg.Push(background_color=cor_fundo),
         sg.Text("By: Rogério Sobral Ribeiro", background_color=cor_fundo),
         sg.Push(background_color=cor_fundo)]
    ]
    return sg.Window("Cadastro", layout, resizable=True, background_color="#2F6073", finalize=True)


def janelaContato():
    layout = [
        [sg.Image("img/volte.png", background_color=cor_fundo, enable_events=True, key="-VOLTAR-"),
         sg.Image("img/logoAPP.png", background_color="#2F6073"),
         sg.Push(background_color="#2F6073"),
         sg.Text("Contato", background_color="#2F6073", font=fonteTitulo),
         sg.Push(background_color="#2F6073")],

        [sg.HSep()],

        [sg.Text("Email", background_color="#2F6073", font=fontTexto, size=10),
         sg.Input(size=(45, 50), background_color="#FFFFFF", font=fontTexto),
         sg.Text("Telefone", background_color="#2F6073", font=fontTexto, size=10),
         sg.Input(size=20, background_color="#FFFFFF", font=fontTexto)],

        [sg.HSep()],

        # Rua | Numero | CEP
        [sg.Text("Rua", background_color="#2F6073", font=fontTexto, size=10),
         sg.Input(size=(45, 50), background_color="#FFFFFF", font=fontTexto),
         sg.Text("Numero", background_color="#2F6073", font=fontTexto, size=10),
         sg.Input(size=10, background_color="#FFFFFF", font=fontTexto),
         sg.Text("CEP", background_color="#2F6073", font=fontTexto, size=5),
         sg.Input(size=16, background_color="#FFFFFF", font=fontTexto),
         sg.Button("Buscar", font=fontTexto)
         ],
        # Bairro | Cidade | SP
        [sg.Text("Bairro", background_color="#2F6073", font=fontTexto, size=10),
         sg.Input(size=(45, 50), background_color="#FFFFFF", font=fontTexto),
         sg.Text("Cidade", background_color="#2F6073", font=fontTexto, size=10),
         sg.Input(size=25, background_color="#FFFFFF", font=fontTexto),
         sg.Text("Estado", background_color="#2F6073", font=fontTexto, size=10),
         sg.Input(size=10, background_color="#FFFFFF", font=fontTexto)
         ],
        # Button Cadastrar e o Buscar
        [sg.Push(background_color=cor_fundo),
         sg.Button("Voltar", font=fontTexto, size=18),
         sg.Button("Cadastrar", font=fontTexto, size=18),
         sg.Push(background_color=cor_fundo)]
    ]
    return sg.Window("Contato", layout, background_color="#2F6073", finalize=True)


def janelaListarFuncionario():
    lista = ["Gerente", "Supervisor", "Suporte", "Segurança"]

    top_tabela = ["Nome", "Nascimento", "CPF", "Cargo", "Telefone", "Nivel"]

    valores = [[]]

    layout = [
        [sg.Image("img/volte.png", background_color=cor_fundo, enable_events=True, key="-VOLTAR-"),
         sg.Image("img/logoAPP.png", background_color="#2F6073"),
         sg.Push(background_color="#2F6073"),
         sg.Text("LISTAR FUNCIONARIO", background_color="#2F6073", font=fonteTitulo),
         sg.Push(background_color="#2F6073")],

        [sg.HSep()],

        [sg.Text("Nome", background_color="#2F6073", font=fontTexto, size=10),
         sg.Input(size=(70, 50), background_color="#FFFFFF", font=fontTexto),
         sg.Text("Nascimento", background_color="#2F6073", font=fontTexto),
         sg.Input(size=20, background_color="#FFFFFF", font=fontTexto),
         sg.Image("img/calendar.png", background_color="#2F6073")],

        [sg.Text("CPF", background_color="#2F6073", font=fontTexto, size=10),
         sg.Input(size=20, background_color="#FFFFFF", font=fontTexto),
         sg.Text("Cargo", background_color=cor_fundo, font=fontTexto, size=10),
         sg.Combo(lista, size=30, default_value="Escolha o Cargos", font=fontTexto, button_arrow_color="#FFFFFF", button_background_color="#2F6073"),
         sg.Text("Cadastrar Contato", size=15, font=fontTexto, background_color=cor_fundo),
         sg.Image("img/contato.png", background_color="#2F6073")],

        [sg.HSep()],

        [sg.Text("Senha", size=10, background_color=cor_fundo, font=fontTexto),
         sg.Input(font=fontTexto, size=15, password_char='*'),
         sg.Text("Nivel", font=fontTexto, background_color=cor_fundo),
         sg.Radio("ADM", "radio1", font=fontTexto, background_color=cor_fundo),
         sg.Radio("COMUM", "radio1", default=True, font=fontTexto, background_color=cor_fundo),
         sg.Push(background_color=cor_fundo),
         sg.Button("Deletar", font=fontTexto, size=20),
         sg.Button("Atualizar", font=fontTexto, size=20),
         sg.Input(size=25, background_color="#FFFFFF", font=fontTexto),
         sg.Button("Buscar", font=fontTexto)],

        [sg.HSep()],

        # Vai entrar uma tabela mostrando os usuarioas
        [sg.Table(headings=top_tabela, values=valores, auto_size_columns=False, def_col_width=27)],

        [sg.HSep()],

        [sg.Push(background_color=cor_fundo),
         sg.Text("By: Rogério Sobral Ribeiro", background_color=cor_fundo),
         sg.Push(background_color=cor_fundo)]
    ]
    return sg.Window("Listar", layout, resizable=False, background_color="#2F6073", finalize=True)


def janelaBaterPonto():
    cabecalho = ["Entrada", "Saída Alimentação", "Volta Alimentação", "Saída"]

    layout = [

        [sg.Image("img/volte.png", background_color=cor_fundo, enable_events=True, key="-VOLTAR-"),
         sg.Image("img/logoAPP.png", background_color="#2F6073"),
         sg.Push(background_color="#2F6073"),
         sg.Text("BATER PONTO", background_color=cor_fundo, font=fonteTitulo),
         sg.Push(background_color=cor_fundo)],

        [sg.HSep()],

        [sg.Text("CPF", background_color=cor_fundo, font=fontTexto),
         sg.Input(size=20, background_color="#FFFFFF", font=fontTexto),
         sg.Image("img/pesquisa.png", background_color=cor_fundo, enable_events=True),
         sg.Text("Data", background_color=cor_fundo, font=fontTexto),
         sg.Input(size=20, background_color="#FFFFFF", font=fontTexto, disabled=True),
         sg.Push(background_color=cor_fundo),
         sg.Image("fotos/maria.png"),
         sg.Push(background_color=cor_fundo)],

        [sg.HSep()],

        [sg.Button("Entrada", font=fontTexto, size=20), sg.Button("Saída Alimentação", font=fontTexto, size=20),
         sg.Button("Volta Alimentação", font=fontTexto, size=20),
         sg.Button("Saída", font=fontTexto, size=20)],

        [sg.Table(headings=cabecalho, values=[], auto_size_columns=False, def_col_width=27, font=("Helvetica", 10))]
    ]
    return sg.Window("Ponto", layout, resizable=False, background_color="#2F6073", finalize=True)


def janelaMenu():
    layout = [

        [sg.Image("img/logoAPP.png", background_color="#2F6073"),
         sg.Push(background_color="#2F6073"),
         sg.Text("MENU", background_color="#2F6073", font=fonteTitulo),
         sg.Push(background_color="#2F6073")],

        [sg.Button("Cadastras", font=fonteTitulo, size=20, key="-CADASTRAR-")],

        [sg.Button("Listar Funcionarios", font=fonteTitulo, size=20, key="-LISTAR-")],

        [sg.Button("Bater Ponto", font=fonteTitulo, size=20, key="-BATER_PONTO-")],
    ]
    return sg.Window("Menu", layout, resizable=False, background_color="#2F6073", finalize=True)


telaLogin, telaCadastrar, telaContato, telaListarUsuarios, telaPonto, telaMenu, telaRecuperaSenha = janelaLogin(), None, None, None, None, None, None


#Inicio do Programa

while True:
    window, events, values = sg.read_all_windows()

    if window == telaLogin and events == sg.WIN_CLOSED:
        break

    if window == telaLogin and events == "-ENTRAR-":
        nome = values["-LOGIN-"]
        senha = values["-SENHA-"]

        if nome in ["carlos", "maria", "pedro"] and senha == "123":
            sg.Popup("Seja bem vindo! ", nome)
            telaMenu = janelaMenu()
            telaLogin.hide()

    if window == telaMenu and events == sg.WIN_CLOSED:
        break
    ##############################################################
    if window == telaMenu and events == "-CADASTRAR-":
        telaCadastrar = janelaCadastrarFuncionario()
        telaMenu.hide()

    if window == telaCadastrar and events == "-VOLTAR-":
        telaMenu.un_hide()
        telaCadastrar.hide()

    #TELA DE CADASTRO DE FUNCIONARIO
    if window == telaCadastrar and events == "-CADASTRAR-":
        nome = values["-NOME-"]
        cpf = values["-CPF-"]
        data_nasc = values["-NASCIMENTO-"]
        cargo = values["-GARGO-"]
        id = values["-ID_CONTATO-"]
        senha = values["-SENHA-"]
        nivel= "Comum"

        #testando a captura dos valores

        FuncionarioController(nome, cpf, data_nasc, cargo, id, senha, nivel)

        print(nome)
        print(cpf)
        print(data_nasc)
        print(cargo)
        print(id)
        print(senha)
        print(nivel)

        #FuncionarioControler(nome, cpf, ):

    if window == telaCadastrar and events == "-CONTATO-":
        telaContato = janelaContato()

    if window == telaContato and events == "-VOLTAR-":
        telaContato.hide()

    #############################################################

    if window == telaMenu and events == "-LISTAR-":
        telaListarUsuarios = janelaListarFuncionario()
        telaMenu.hide()

    if window == telaListarUsuarios and events == "-VOLTAR-":
        telaMenu.un_hide()
        telaListarUsuarios.hide()

    ############################################################

    if window == telaMenu and events == "-BATER_PONTO-":
        telaPonto = janelaBaterPonto()
        telaMenu.hide()

    if window == telaPonto and events == "-VOLTAR-":
        telaMenu.un_hide()
        telaPonto.hide()

    #############################################################
    if window == telaLogin and events == "-CREATE_USER-":
        telaRecuperaSenha = janelaRecuperarSenha()

    if (window == telaRecuperaSenha and events == sg.WIN_CLOSED) or (window == telaRecuperaSenha and events == "-VOLTAR-"):
        telaRecuperaSenha.hide()

    ##############################################################
    if window == telaContato and events == sg.WIN_CLOSED:
        telaContato.hide()

    if window == telaListarUsuarios and events == sg.WIN_CLOSED:
        telaListarUsuarios.hide()
        telaMenu.un_hide()

    if window == telaCadastrar and events == sg.WIN_CLOSED:
        telaCadastrar.hide()
        telaMenu.un_hide()

    if window == telaPonto and events == sg.WIN_CLOSED:
        telaPonto.hide()
        telaMenu.un_hide()

####
###
# destruido o arquivo tk usado para pegar as fontes
# root.destroy()
