def expoFunc(numero=2,exponencial = 2):
    """
    Realiza o calculo de um número elevado, por padrão, ao quadrado, isso pode ser mudado caso o usuário passe o expoente desejado assim como o número.
    """
    resultado = numero**exponencial
    return resultado

escolha_usuario = int(input("Deseja mudar o numero ou o expoente?\n1 - Número\n2 - Expoente\n3 - Não"))

if escolha_usuario == 1:
    escolha_numero = int(input("Digite o novo numero: "))
    expoFunc(escolha_numero)
elif escolha_usuario == 2:
    escolha_expo = int(input("Digite o novo expoente: "))
    expoFunc(escolha_expo)
elif escolha_usuario == 3 :
    print("Obrigado por usar.")
    print("Resultado padrão:",expoFunc())