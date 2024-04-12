palavra_usuario = input("Digite uma palavra:")
palavra_usuario.replace(" ","").lower()

palavra_inversa = palavra_usuario[::-1]

if palavra_usuario == palavra_inversa:
    print(f"{palavra_usuario} é um palíndromo!")
else:
    print(f"{palavra_usuario} não é um palíndromo.")