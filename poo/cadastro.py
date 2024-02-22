from flet import *
from cliente import Customer
from produto import Produto
from carrinho_compra import ShoppingCart
class ViewRegisterProduct(UserControl):
    def __init__(self):
        super().__init__()
        self.carrinho = ShoppingCart
    def build(self):

        #functions
        def registerCustomer(e):
            c1 = Customer(name.value, cpf.value)
            resposta.value = str(c1)
            resposta.update()

        def registerProducts(e):
            p1 = Produto(descript=descript.value,price=price.value)

        #customer
        titler_1 = Text("Cadastro de Cliente")
        name = TextField(col={"":12,"sm":6},label="Name")
        cpf = TextField(col={"":12,"sm":6},label="CPF")
        btnRegisterCustomer= ElevatedButton(text="Register client", on_click=registerCustomer)
        lineCustomer = ResponsiveRow(controls=[name, cpf])
        resposta = Text()

        #Products
        title_2 = Text("Cadastro de Produtos")
        descript = TextField(col={"":12,"sm":4, "md":3}, label="Descricão do produto")
        price = TextField(col={"":6,"sm":3, "md":3}, label="Price", prefix_text="R$")
        marca = TextField(col={"":6,"sm":3, "md":3}, label="marca")
        btnRegisterProducts = ElevatedButton(text="Register Product")

        lineProduts = ResponsiveRow(controls=[descript, price, marca])

        respostaProdutos = Text()

        return Column(controls=[

            titler_1,
            lineCustomer,
            btnRegisterCustomer,
            resposta,
            title_2,
            lineProduts,
            btnRegisterProducts,
            respostaProdutos
        ])

def main(page:Page):
    #setup my page

    page.title = "cadastro de produto"
    page.horizontal_alignment = "center"
    page.window_center()

    #setup my views

    """"
    hot reload
    
    apontar o caminho do arquivo
    
    flet -r cadastro.py
          ||
    flet rum cadastro.py -d
    """
    viewRegisterPro = ViewRegisterProduct()


    page.add(viewRegisterPro)

    page.update()





if __name__ == '__main__':

    app(target=main)
