#Programa KM percorrido e preço a pagar
carro = 60
dia = float(input("Quantos dias utilizou o carro: "))
aluguel = carro * dia
distancia = float(input("Quantos KM foram percorridos com o carro: "))
distancia_aluguel = distancia * 0.15
preco = aluguel + distancia_aluguel

print("o valor total a pagar é %5.2f R$" % preco)
