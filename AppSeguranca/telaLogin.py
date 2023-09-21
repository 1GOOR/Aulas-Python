#-*- coding: latin-1 -*-

import PySimpleGUI as sg

def janelaLogin():

    layout = [

        [sg.Push(background_color="#2F6073"), sg.Text("LOGIN", font="Helvetica 20", text_color="#2F6073", background_color="#2F6073"),sg.Push(background_color="#2F6073")],
        [sg.Push(background_color="#2F6073"), sg.Image("img/login.png", background_color="#2F6073"), sg.Push(background_color="#2F6073")],
        [sg.Image("img/1.png", background_color="#2F6073"), sg.Text("Login", size=7, background_color="#2F6073", text_color="#E8BF58", font=" roboto 20"),sg.Input(size=20, background_color="#ffffff", font=" roboto 15", key="-LOGIN-")],
        [sg.Image("img/2.png", background_color="#2F6073"), sg.Text("Senha", size=7, background_color="#2F6073", text_color="#E8BF58", font=" roboto 20"),sg.Input(size=20, background_color="#ffffff", font=" roboto 15", password_char="*", key="-SENHA-")],
        [sg.Push(background_color="#2F6073"), sg.Button("Entrar", size=10, font="arial 15", pad=25, mouseover_colors=("#E8BF58", "#FFE054"), button_color="#E8BF58", key="-BOTAO-"), sg.Push(background_color="#2F6073")],
        [sg.Push(background_color="#2F6073"), sg.Text("Recuperar Senha", background_color="#2F6073", text_color="#E8BF58"),sg.Push(background_color="#2F6073")]

    ]

    return sg.Window("Tela Login", layout, background_color="#2F6073")


def recuperarSenha():

    layout=[

    [sg.Push(background_color="#2F6073")], [sg.Image("img/recuperar.png", background_color="#2F6073")], [sg.Push(background_color="#2F6073")],
    [sg.Text("Entre com seu CPF", background_color="#2F6073", text_color="#E8BF58", font=" roboto 11")], [sg.Input(key="-CPF-", size=20, background_color="#ffffff", font=" roboto 15")],
    [sg.Button("Recuperar Senha", font="arial 15", pad=25, mouseover_colors=("#E8BF58", "#FFE054"), button_color="#E8BF58")], [sg.Text("", visible=False, background_color="#2F6073", text_color="#E8BF58")]

    ]
    return sg.Window("Recuperar Senha", layout, background_color="#2F6073")


def telaLogin():

    layout = [
        [sg.Image("img/logo.png", background_color="#2F6073"), sg.Text("Ola", font="Helvetica 8", text_color="#ffffff", background_color="#2F6073"), sg.Push(background_color="#2F6073")],
        [sg.Text("Nome", background_color="#2F6073"), sg.Input(size=20, background_color="#ffffff", font=" roboto 15")]
    ]
    return sg.Window("Recuperar Senha", layout, background_color="#2F6073")

telaLogin().read()
