import random

def jogarDado():
    dado = int((random.random() * 6) + 1)
    return dado

quantidada_de_dados = int(input("Digite quantos dados deseja jogar:"))

for i in range(quantidada_de_dados):
    print("Dado",i+1,"=",jogarDado())