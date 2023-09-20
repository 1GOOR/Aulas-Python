import PySimpleGUI as sg

def telaCalculadora():
    layout = [
        [sg.Push(), sg.Text("Calculadora"), sg.Push()],
        [sg.Input(key="-VALOR1-"), sg.Text("+"), sg.Input(key="-VALOR2-")],
        [sg.Button("Calcular", key="-CALCULAR-"), sg.Text("resulatado"), sg.Input(disabled=True, key="-RESULTADO-")]
    ]

    return sg.Window("calculadora", layout)


janela_1 = telaCalculadora()

while True:

    events, values = janela_1.read()

    if events == sg.WIN_CLOSED:
        break


    try:
        if events == "-CALCULAR-":
            v1 = float(values["-VALOR1-"])
            v2 = float(values["-VALOR2-"])

            somar = v1 + v2

            janela_1["-RESULTADO-"].update(value=somar)

            janela_1["-VALOR1-"].update(value="")
            janela_1["-VALOR2-"].update(value="")
    except Exception as e:

        sg.Popup("digite apenas numeros seu cavalo")
        janela_1["-VALOR1-"].update(value="")
        janela_1["-VALOR2-"].update(value="")