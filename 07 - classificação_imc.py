usuario_altura = float(input("Digite sua altura:"))
usuario_peso = float(input("Digite seu peso:"))

calculo_imc = usuario_peso / (usuario_altura**2)

if calculo_imc < 18.5:
    print("Seu IMC",calculo_imc,"está classificado como: MAGREZA, Obesidade Grau 0")
elif calculo_imc < 24.9 and calculo_imc > 18.5:
    print("Seu IMC",calculo_imc,"está classificado como: NORMAL, Obesidade Grau 0")
elif calculo_imc < 29.9 and calculo_imc > 25:
    print("Seu IMC",calculo_imc,"está classificado como: SOBREPESO, Obesidade Grau 1")
elif calculo_imc < 39.9 and calculo_imc > 30:
    print("Seu IMC",calculo_imc,"está classificado como: OBESIDADE, Obesidade Grau 2")
elif calculo_imc > 40:
    print("Seu IMC",calculo_imc,"está classificado como: OBESIDADE GRAVE, Obesidade Grau 3")