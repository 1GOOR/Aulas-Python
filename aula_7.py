#trabalhando com Listas
#vamos colocar todas as letras em maiscula
nomes =['Ana', 'gui', 'bia', 'ze']

print(nomes)

for index in range(len(nomes)):
    nomes[index] = nomes[index].title()

print(nomes)

print('\n#################################################\n')

#outra maneira de criar listas

Nova_lista = [] # ou asimm Nova_lista = list()

Nova_lista.append("E") # adiciona um linha na nossa lista
Nova_lista.append("B")
Nova_lista.append("D")
Nova_lista.append("A")
Nova_lista.append("C")

print(Nova_lista)
#count() vai contar quantas vezes o elemeto aparece
print(Nova_lista.count('E'))

#remove() Remove o determinado objeto
Nova_lista.remove(Nova_lista[0]) # ou Nova_lista.remove('Rua')

#sort() organiza a lista

Nova_lista.sort()
print(Nova_lista)
