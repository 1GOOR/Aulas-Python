from flet import *

class Login(UserControl):

    def build(self):
        iconName = Icon(icons.BOY)
        name = TextField(label="digite o seu nome")

        iconPassword = Icon(icons.PASSWORD)
        password = TextField(label="Digite seu Passworld", border_color="#8251bb")

        btnEnter = ElevatedButton("Entrar")

        img = Image(src="img_login_escola.png", width=300, height=300)

        forget_password = Text(value="Esqueci a senha", color="#8251bb")

        line_img = Row(controls=[img], alignment=MainAxisAlignment.CENTER)
        line_1 = Row(controls=[iconName, name], alignment=MainAxisAlignment.CENTER)
        line_2 = Row(controls=[iconPassword, password], alignment=MainAxisAlignment.CENTER)
        line_btn = Row(controls=[btnEnter], alignment=MainAxisAlignment.CENTER)
        line_forget_pswd = Row(controls=[forget_password], alignment=MainAxisAlignment.CENTER)

        colLogin = Column(controls=[
            line_img,
            line_1,
            line_2,
            line_btn,
            line_forget_pswd

        ], alignment=MainAxisAlignment.CENTER)

        return colLogin

def main(page: Page):
    page.title = "Pagina Login"

    page.add(Login())
    page.update()


app(target=main)
