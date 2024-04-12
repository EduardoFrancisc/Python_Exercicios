numero_secreto = 15
usuario_palpite = int(input("Tente adivinhar o número secreto de 0 a 20"))

if numero_secreto == usuario_palpite:
    print("Você acertou, o número secreto é",numero_secreto)
elif usuario_palpite > numero_secreto:
    print("Seu palpite está muito alto, Tente Novamente.")
elif usuario_palpite < numero_secreto:
    print("Seu palpite está muito baixo, Tente Novamente.")
else:
    print("Tente outro número.")