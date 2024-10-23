#Expressão para decidir se um aluno foi ou não aprovado.

materia1 = int(input("Digite a nota da materia 1: "))
materia2 = int(input("Digite a nota da materia 2: "))
materia3 = int(input("Digite a nota da materia 3: "))

media = ((materia1 + materia2 + materia3) / 3 )
aprovado = (media >= 7)

print (f"{media:3.2f}")
if aprovado:
    print("Aprovado")
else:
    print("Reprovado")
