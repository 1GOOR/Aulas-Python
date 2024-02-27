from flet import *

class modalBTN(Container):
    def __init__(self,title):
        super().__init__()
        self.title = title
        self.width = 200
        self.height = 200
        self.content = Text(value=self.title)
        self.bgcolor = "#f15a24"
class ViewRegister(UserControl):
    def __init__(self):
        super().__init__()
        self.btnProf = modalBTN("Professor")
        self.btnPonto = modalBTN("Ponto")

    def build(self):
        return ResponsiveRow(controls=[self.btnProf, self.btnPonto])