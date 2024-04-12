def contaVogais(frase):
    '''
    Recebe uma lista onde cada item é uma letra da frase fornecida pelo usuario.
    Itera sobre a lista, caso algum item da lista estiver também presente na lista de vogais, +1 é somado ao contador.
    Retorna o total de vogais da frase recebida.
    '''
    vogais=['a','e','i','o','u']
    contador_vogais = 0
    for i in frase:
        if i in vogais:
            contador_vogais = contador_vogais + 1
    return contador_vogais

frase_crua = input("Digite a frase para saber a quantidade de vogais e consoantes: ")

frase_usuario = frase_crua.replace(' ','')

if frase_usuario.isalpha():

    lista_formatada = [x.lower() for x in frase_usuario]
    
    print("Frase solicitata:", frase_crua.strip())
    print("Vogais nessa frase:",contaVogais(lista_formatada))
    print("Consoantes nessa frase:",len(lista_formatada) - contaVogais(lista_formatada))
else:
    print("Digite apenas letras!")
