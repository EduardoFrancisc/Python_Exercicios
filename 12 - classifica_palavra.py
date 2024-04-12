palavra = input("Digite uma palavra:")

if len(palavra) > 5:
    print("Essa palavra é classificada como longa.")
elif len(palavra) < 5:
    print("Essa palavra é classificada como curta.")