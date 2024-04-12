import string
import random

def geradorSenhas():
    """
    Função que retorna uma senha aleatória entre simbolos, numeros de 0-100, letras, maiusculas e minusculas de a-Z
    """
    simbolos = random.choice(string.punctuation)
    numeros = random.randint(0,100)
    minusculas = random.choice(string.ascii_lowercase)
    maiusculas = random.choice(string.ascii_uppercase)

    senhaAleatoria = str(numeros)+simbolos+maiusculas+minusculas

    print("Senha aleatória gerada:",senhaAleatoria)
    
geradorSenhas()