def verificaPrimo(numero):
    """
    Função recebe um número e verifica se é primo ou não dentro de um loop com range do próprio número - 1. Verificando se o número é divisível por mais algum número além dele mesmo e 1.
    """
    for i in range(2, numero-1):
        if numero % i == 0:
            return False
    return True

for i in range(2, 101):
    if verificaPrimo(i):
        print(i,"é primo.")
    else:
        print(i,"não é primo.")