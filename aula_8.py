#Collections

#List
# . Permite buscar pelo index
# . Listas são Mutaveis /permite que os valores armazenados seja modificado
#Tupla
# . Permite buscar pelo index
# . Não mutavel
#Dict
# . posibilita nomear os index e chalos pelo nome
#Set

Lista = [12,34,68,96,34]
Lista.append(90)
#pegando o valor pelo index
print(Lista[5])
#mutavel /mudando o valor da lista
Lista[5] = 5
print(Lista[5])

print("#"*40)

###########################################
tupla = (12,34,56,78,90)
#pegando o valor pelo index
print(tupla[3])
#nao permite mudar o valor da tupla
#tupla[4] = 23
print("#"*40)

print("Primeira Forma")
for i in range(len(tupla)):
    print(tupla[i])
print("#"*40)

print("Segunda forma")
for i in tupla:
    print(i)
print("#"*40)

print("Terceira")
for num, valor_tupla in enumerate(tupla):
    print(f"posição: {num}  valor: {valor_tupla}")
print("#"*40)

###########################################

#dict
aluno={"nome": "igor", "idade": 20, "RG": "12.345.345-43"}

chaves = aluno.keys()
print(f"Apens as Chaves \n{chaves}\n")

print("pegando apenas os valores")
valores = aluno.values()
print(f"Apens os Valores \n{valores}\n")

print(f"pegando os itens")
itens = aluno.items()
print(f"Pegando as Chave e os Valores \n{itens}\n\n")


aluno["cpf"] = "123.121.121-23"

print(f"pegando")
for chave,valor in aluno.items():
    print(f"Chave: {chave} valor: {valor}")






