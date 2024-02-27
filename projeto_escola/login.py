from flet import (UserControl, Image,TextField,ElevatedButton,
                  IconButton,icons,Row,MainAxisAlignment, Column)

class ViewLogin(UserControl):
    def __init__(self, page):
        super().__init__()
        self.input_login = TextField(label="Login")
        self.input_password = TextField(label="Password")
        self.btn_enter = ElevatedButton(text="Entrar", on_click= lambda e: self.page.go("/menu"))
        self.page=page
    def build(self):
        img_logo = Image(src="img_login.png")
        icon_google = IconButton(icon=icons.BED)
        icon_gitHup = IconButton(icon=icons.ADD)
        line1 = Row(controls=[img_logo], alignment=MainAxisAlignment.CENTER)
        line2 = Row(controls=[self.input_login], alignment=MainAxisAlignment.CENTER)
        line3 = Row(controls=[self.input_password], alignment=MainAxisAlignment.CENTER)
        line4 = Row(controls=[self.btn_enter], alignment=MainAxisAlignment.CENTER)
        line5 = Row(controls=[icon_google, icon_gitHup], alignment=MainAxisAlignment.SPACE_AROUND)
        return Column(
            controls=[
                line1,
                line2,
                line3,
                line4,
                line5
            ]
        )