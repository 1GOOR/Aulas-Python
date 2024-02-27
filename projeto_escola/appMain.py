from flet import *
from login import ViewLogin
from viewMenu import ViewMenu
#from viewMenu.viewBarNav import ViewBarNav

def main(page:Page):
    page.title="Login"
    page.window_width=450
    page.window_max_width=450
    page.window_min_width=450
    page.window_center()
    page.horizontal_alignment=MainAxisAlignment.CENTER
    # My views
    viewLogin=ViewLogin(page)
    viewMenu= ViewMenu()
    #viewBar= ViewBarNav()
    def changeRoutes(route):
        page.views.clear()
        page.views.append(
            View("/",
            [
              viewLogin
            ]
        ))
        if page.route=="/menu":
            page.views.append(
                View("/menu",
                [
                # Depois vamos colocar a nossa segunda tela
                    viewMenu,
                    Text("Nova Tela"),
                    ElevatedButton("Voltar para o login", on_click=lambda e: page.go("/"))
                ]
            )
        )

        page.update()
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    page.on_route_change = changeRoutes
    page.on_view_pop = view_pop
    page.go(page.route)


app(target=main)