# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuario. Calcule o total em segundos.
dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
total_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print("Em segundos é igual a %10d segundos." % total_segundos)
