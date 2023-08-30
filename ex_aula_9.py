validar = set()
logins = list()

print("sistema de cadastro")
while True:
    usuario = list()
    login = input("Login: ")
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

entrada =input ("Login: ")

for i in logins:

    if entrada == i[0]:
        print("bem vindo")



