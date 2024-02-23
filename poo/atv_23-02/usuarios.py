class UsuarioComum:
    usuarios = []
    def __init__(self, nome, cpf, senha, email):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.email = email

class UsuarioADM(UsuarioComum):
    def __init__(self, nome, cpf, senha, email):
        super().__init__(nome, cpf, senha, email)
        self.__adm = True
    @property
    def get(self):
        return self.__adm

def tornarADM(user: UsuarioComum):
    if(type(user) == UsuarioComum):
        print("usuario cadastrado")
        usuario = UsuarioADM(nome=user.nome, cpf=user.cpf, senha=user.senha, email=user.email)
        UsuarioADM.usuarios.append(usuario)
        return usuario
    else:
        print("nao foi possivel cadastrar")

def cadastrar(nome,cpf,senha,email):
    usuario = UsuarioComum(nome,cpf,senha,email)
    UsuarioComum.usuarios.append(usuario)
    return usuario
def isADM(user: UsuarioADM):
    try:
        return print(user.get)
    except:
        return print(False)

def verUsuarios(user: UsuarioComum):
    for i in user.usuarios:
        print(f"{i.nome} {i.cpf} {i.email}")

if __name__ == '__main__':

    cadastrar("ze", "123.456.789", "*******","ze@gmail.com")
    cadastrar("fabricio","45645","**","fab@gmail.com")


    verUsuarios(UsuarioADM)


