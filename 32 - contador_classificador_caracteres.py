import re

def contaCaracteres(texto):
    count_num = 0
    count_low = 0
    count_uppe = 0
    count_car_espec = 0
    count_space= 0

    lista = [i for i in texto]

    for i in range(0,len(lista)):
        if lista[i].isalpha():
            if lista[i].islower():
                count_low+=1
            if lista[i].isupper():
                count_uppe+=1

        if lista[i].isdecimal():
            count_num+=1

        if lista[i] == " ":
            count_space+=1

    regex = re.compile(r'[@_.!´#$%`;-^&*(),<>?/\|}{~:\[\]]')
    caracteres_espec_encontrados = regex.findall(texto)

    for x in caracteres_espec_encontrados:
        count_car_espec+=1

    print("Frase:",texto)
    print("Qtd. de Caracteres:",len(lista))
    print("Qtd. de Letras maiúsculas:",count_uppe)
    print("Qtd. de Letras minúsculas:",count_low)
    print("Qtd. de Números:",count_num)
    print("Qtd. de Caracteres especiais:",count_car_espec)
    print("Qtd. de Espaços em brnaco:",count_space)

texto = input("Digite seu texto")
contaCaracteres(texto)