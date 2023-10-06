import poo.associacao as so

piloto_1 = so.Piloto("ze")
piloto_2 = so.Piloto("Pedro")
piloto_3 = so.Piloto("ana")
piloto_4 = so.Piloto("gui")

carro_1 = so.Carro("S1000")
carro_2 = so.Carro("BMW M3")

piloto_1.Carro = carro_1

print(piloto_1.Carro.nome)

piloto_3.Carro = carro_2

piloto_3.Carro.dirigir()