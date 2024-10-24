#Programa para calcular a redução do tempo de vida de um fumante
cigarros = int(input ("Quantos cigarros você consome diariamente: "))
anos = int(input ("Há quantos anos você fuma: "))
fuma = cigarros * (anos * 365)
perde = fuma * 10
perde_dias = perde / 1440

print("Sua expectativa de vida caiu em %3d dias" % perde_dias)