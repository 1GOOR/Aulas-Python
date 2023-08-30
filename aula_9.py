    #set  //colections
"""
    lista = [1,2,4,7,2,7]
    
    tupla = (1,3,45,6,4)
    
    dicionario = {"um": 1, "dois": 2, "tres": 3, "quatro":4}
    
    conjunto = {1,3,5,7,4} #//set Nao repete os valores //Nao se pode pegar objetos por index//organiza os valores//os dados sao acessados de forma mais rapida
    
    print(f"Lista {lista}\n")
    
    print(f"tupla {tupla}\n")
    
    print(f"dicionario {dicionario}\n")
    
    print(f"conjunto {conjunto}\n")
"""

print("Bem Vindo!")

logins = {"admin"} # || logins = set()

while True:
    login = input("cadastre o seu login :")
    tamanho = len(logins)
    logins.add(login)

    if len(logins) != tamanho:
        break
    else:
        print("esse login ja exite")
