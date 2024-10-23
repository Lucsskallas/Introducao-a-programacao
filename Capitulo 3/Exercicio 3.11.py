#Preço de uma mercadoria e percentual de desconto
mercadoria = int(input("Preço mercadoria: "))
desconto = float(input("Valor desconto: "))

p_desconto = desconto / 100
mercadoriadescontada = mercadoria - mercadoria * p_desconto
descontomercadoria = mercadoria * p_desconto

print("O valor do desconto é de %3d R$" % descontomercadoria)
print("O valor da mercadoria descontada é de %4d R$" % mercadoriadescontada)
