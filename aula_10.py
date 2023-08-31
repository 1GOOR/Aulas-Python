# Funções

valor1 = 2
valor2 = 6.3
valor3 = 8.5

media = (valor1 + valor2 + valor3) / 3

print(media)

valores = [2, 6.3, 8.5]
mediao = sum(valores) / len(valores)


def media(n_1: str, n_2: str, n_3: str):
    if n_1.isdigit() and n_2.isdigit() and n_3.isdigit():
        print((int(n1) + int(n2) + int(n3)) / 3)


n1 = input("valor 1:")
n2 = input("valor 2:")
n3 = input("valor 3:")

media(n1, n2, n3)

print("funcoes".center(30, "-"))


def mult(num_1: int, num_2: int):
    print(num_1 * num_2)


num1 = int(input("Numero 1: "))
num2 = int(input("Numer0 2: "))

mult(num1, num2)

print("Ler os Valores".center(30, "-"))

def lerValores (lista:list()):
    for i in lista:
        print(i)



lerValores(["ola", "cha", "swjs"])




