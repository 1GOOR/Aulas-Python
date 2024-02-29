#Vamos aprender como é realizado a troca de telas
# Devemos importa as libs
from flet import *
# Vou importar minhas telas de arquivo externo
from usuarios import Ususario

# Para rodar o flet preciso de uma Page, neste caso
# vou criar uma atraves de uma função
def main(page:Page):
#    Estou pedido que seja passado um parametro do
#    tipo "Page" dentro da função, porque assim posso criar uma janela
#    com o flet



    telaUsuario=Ususario()
#     vou passar as configurações que quero para minha janela
    page.title="Troca de telas"
    page.window_width=600
    page.window_center() # Estou abrindo minha tela logo no centro, ele é um metodo
    # vou criar uma função que troca de tela
    def trocaPaginas(route):
        page.views.clear()
        # vou adicionar uma view dentro da minha tela
        page.views.append(
            # Estou criando uma view nova
            # O parametro route indica o endereço da tela
            # O controls serve para add os elementos da minha pagina,
            # ou uma pagina ja configurada
            View(
                route="/",
                controls=[
                    #Aqui vai ter uma tela de Login
                     Text("Login"),
                     ElevatedButton("Ir para a segunda tela", on_click=lambda e: page.go("/usuario"))
                ]
            )
        )
        if page.route=="/usuario":
            # vou adicionar mais uma view chamada usuario
            page.views.append(
                View(
                    route="/usuario",
                    controls=[
                        telaUsuario,
                        # Todo Button possui varios eventos, estamos usando o evento on_click
                        # o qual acontece quando a pessoa clica no bnt, mas o btn tem que realizar uma ação
                        # vamos passar essa ação atraves de uma função
                        # A função que quero usar é sem assinatura, Lambda, que vai realizar algo somente onde foi
                        # criada. quando ela ser a função ela vai dar o comando page.go() para trocar de rota
                        ElevatedButton("Voltar", on_click= lambda e: page.go("/") )
                    ]
                )
            )

        # Uma vez que eu editei o conteudo da view dentro da pagina
        # tenho que atualizar a pagina
        # Toda vez que eu modificar algo tenho que atualizar a pagina
        page.update()
    page.on_route_change= trocaPaginas
    page.go(page.route)

# Preciso colocar minha tela dentro da função app do flet para rodar
# Caso eu queira rodar na WEB tenho que usar o parametro view=WEB_BROWSER
app(target=main,view=WEB_BROWSER)