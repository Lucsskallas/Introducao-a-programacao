#Tempo de uma viagem de carro
velocidade = float(input("Coloque a velocidade do carro em KM: "))
distancia = float(input("Coloque a distância em KM para chegar ao seu destino: "))
tempo = distancia / velocidade
print("Levará %5.2f horas para chegar ao seu destino" % tempo)

tempo_s = int(tempo * 3600)
horas = int(tempo_s / 3600)
tempo_s = int(tempo_s % 3600)
minutos = int(tempo_s / 60)
segundos = int(tempo_s % 60)

print("%05d:%02d:%02d" % (horas, minutos, segundos))
