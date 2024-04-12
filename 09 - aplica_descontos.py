valor_compra = float(input("Digite o valor da compra:"))

if valor_compra >= 100:
    valor_desconto = valor_compra * 0.1
    valor_compra = valor_compra - valor_desconto
    print("O valor da conta com desconto ficou R$",valor_compra)
elif valor_compra >= 200:
    valor_desconto = valor_compra * 0.15
    valor_compra = valor_compra - valor_desconto
    print("O valor da conta com desconto ficou R$",valor_compra)