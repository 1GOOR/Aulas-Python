from flet import *
#Criando um classe que retorna os usuarios
class Ususario(UserControl):
    def __init__(self):
        super().__init__()
        #Criando os botoes separado(usando o 'SubmenuButton') para inserir na barra de menu
        self.opsUsuario = SubmenuButton(content=Text("usuario"))
        self.opsProfessor = SubmenuButton(content=Text("Professor"))
        self.opsPonto = SubmenuButton(content=Text("Bater Ponto"))

        # Criando os Inputs/TestField
        self.txtFieldNome = TextField(label="Nome")
        self.txtFieldSobrNome = TextField(label="Sobre Nome")
        self.txtFieldCPF = TextField(label="CPF")
        self.txtFieldTelefone = TextField(label="Telefone")

        #Criando os Botes
        self.btn = ElevatedButton("Cadastrar")

        #criando uma tabala
        self.table = DataTable(

            expand=True,
            columns=[
                DataColumn(Text("ID")),
                DataColumn(Text("Nome")),
                DataColumn(Text("Sobre Nome")),
                DataColumn(Text("CPF")),
                DataColumn(Text("Telefone"))
            ],
            rows=[
                DataRow(cells=[
                    DataCell(Text("1")),
                    DataCell(Text("Igor")),
                    DataCell(Text("Josue")),
                    DataCell(Text("123.456.789")),
                    DataCell(Text("11 9 6514-7568"))
                ])
            ],
        )



    def build(self): #Este medodo vai me retornar o que eu criar como elementos
        menu = MenuBar(controls=[
            self.opsUsuario,
            self.opsProfessor,
            self.opsPonto


        ],
        expand=True)

        linhaMenu = Row(controls=[menu])

        lineFieldOne = Row(controls=[self.txtFieldNome, self.txtFieldSobrNome])

        lineFieldTwo = Row(controls=[self.txtFieldCPF, self.txtFieldTelefone])

        line = Row(controls=[self.table])
        coluna = Column(controls=[
            linhaMenu,
            lineFieldOne,
            lineFieldTwo,
            self.btn,
            line
        ])

        return coluna


if __name__ == '__main__':
    pass
