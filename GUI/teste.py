#-*- coding: latin-1 -*-

import PySimpleGUI as sg

layout = [
    [sg.Push(background_color="#2f6873"), sg.Text("LOGIN", font="Helvetica 20",text_color="#E8BF58", background_color="#2f6873"), sg.Push(background_color="#2f6873")],
    [sg.Push(background_color="#2f6873"), sg.Image("imagem1.png"), sg.Push(background_color="#2f6873")],
    [sg.Text("Login", size=7, background_color="#2f6873", text_color="#E8BF58", font=" roboto 20"), sg.Input(size=20, background_color="#2f6873", font=" roboto 15", key="-LOGIN-")],
    [sg.Text("Senha", size=7, background_color="#2f6873", text_color="#E8BF58", font=" roboto 20"), sg.Input(size=20, background_color="#2f6873", font=" roboto 15", password_char="*", key="-SENHA-")],
    [sg.Push(background_color="#2f6873"), sg.Button("Entrar", size=10, font="arial 15", pad=25, mouseover_colors=("#E8BF58", "#FFE054"), button_color="#E8BF58", key="-BOTAO-"), sg.Push(background_color="#2f6873")],
    [sg.Push(background_color="#2f6873"), sg.Text("Recuperar Senha", background_color="#2f6873", text_color="#E8BF58"), sg.Push(background_color="#2f6873")]
]

window = sg.Window("Tela Login", layout, background_color="#2f6873")

while True:

    events, values = window.read()

    if events == sg.WIN_CLOSED:
        break
    elif events == "-BOTAO-":
        nome = values["-LOGIN-"]
        senha = values["-SENHA-"]
        if nome in ["carlos", "pedro", "maria"] and senha in ["123", "222", "12345"]:
            print("Você esta dentro do sistema")