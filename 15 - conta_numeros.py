import random

def geradorNumeros(quantidade_numeros):
    """
    Função recebe a quantidade de números que a lista deverá conter
    Retorna uma lista com números aleatórios (positivos e negativos)
    """
    for i in range(quantidade_numeros):
        negativos = random.randint(-100,0)
        positivos = random.randint(0,100)

        numero = negativos + positivos

        lista_numeros.append(numero)

    return lista_numeros

def contaNumeros(lista):
    """
    Função que recebe uma lista e conta os números positivos
    """
    numeros_positivos = 0

    for i in lista:
        if i > 0:
            numeros_positivos +=1
    
    return numeros_positivos

quantidade_numeros = int(input("Quantos números deseja colocar na lista? "))
lista_numeros = []

if quantidade_numeros == 0:
    print("Não é possível criar uma lista com 0 números.")
else:
    print("Lista com",quantidade_numeros,"números:", geradorNumeros(quantidade_numeros))
    print("Existem", contaNumeros(lista_numeros), "números positivos.")