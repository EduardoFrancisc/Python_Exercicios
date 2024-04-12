import random

personagens_lista = ["Eduardo","Lucas","Maria","João","Nayanda","Rodrigo"]
acoes_lista = [" espancou alguém"," deu dois tiros pro alto"," bebeu uma coquinha"," roubou um banco"," começou a gritar"," fez o TP"]
locais_lista = [" em Madureira."," na Central."," no Maracanã."," em Niterói."," na igreja."," no México."]

numero_aleatorio_personagens = int(random.random() * 6)
numero_aleatorio_acoes = int(random.random() * 6)
numero_aleatorio_locais = int(random.random() * 6)

print(personagens_lista[numero_aleatorio_personagens]+acoes_lista[numero_aleatorio_acoes]+locais_lista[numero_aleatorio_locais])