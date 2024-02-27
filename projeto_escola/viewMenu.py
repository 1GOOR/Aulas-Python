from flet import (UserControl,MenuBar, SubmenuButton,Text, Row,MenuStyle,ButtonStyle,MaterialState,
                  Column, Container,Dropdown,dropdown)
from cadastro import ViewRegister

class ViewMenu(UserControl):
    def __init__(self):
        super().__init__()
        self.menuSummary=SubmenuButton(
            content=Text("Resumo",color="#ffffff",size=22),
            style=ButtonStyle(
                  bgcolor={
                      MaterialState.DEFAULT:"#7b44f2",
                  }
        ))

        self.menuRegister= SubmenuButton(content=Text("Cadastrar",color="#ffffff",size=22))
        self.menuTimeSheet= SubmenuButton(content=Text("Ponto",color="#ffffff",size=22))
        self.menuReport= SubmenuButton(content=Text("Relatorio",color="#ffffff",size=22))
        self.modaiBTN = ViewRegister
    def build(self):
        menuBar=MenuBar(
            expand=True,
            style=MenuStyle(
                bgcolor="#7b44f2",

            ),
            controls=[
                self.menuSummary, self.menuRegister, self.menuTimeSheet, self.menuReport
            ],)

        coluna = Column(controls=[Row(controls= [menuBar]), Row(controls= [self.modaiBTN])])

        return coluna