validar = set()
logins = list()

print(f"Sistema de cadastro\n digite 'exit' para sair")
while True:
    usuario = list()
    login = input("informe o Login do usuario: ")
    tamanho = len(validar)

    if login.strip()[0].lower() == "e":
        break

    validar.add(login)

    if len(validar) == tamanho:
        print(f"login ja exite")
    else:
        senha = input("senha: ")
        usuario.append(login)
        usuario.append(senha)
        logins.append(usuario)

print(f"\n--------Logon--------")

while True:
    entrada = input("Login: ")
    for i in logins:
        if entrada == i[0]:
            senha = input("senha: ")
            if senha == i[1]:
                print("bem vindo")
                break
            else:
                print("senha incorreta")
                break
        else:
            print("login invalido")
            break