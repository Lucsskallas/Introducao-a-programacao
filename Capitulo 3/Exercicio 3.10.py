#faça um programa que calcule o aumento de um salario
salario = float(input("Digite o seu Salario atual: "))
s_aumento = float (input("Digite a porcentagem de aumento: "))
aumento = s_aumento / 100

novo_salario = salario * aumento + salario
novo_aumento = salario * aumento

print("Seu aumento foi de %2d R$ em um salario de %5d R$" % (novo_aumento, salario))
print("Seu novo salário é de %5d R$" % novo_salario)
