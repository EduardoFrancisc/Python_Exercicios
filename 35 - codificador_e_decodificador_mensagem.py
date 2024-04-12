def decodificarMensagem(cifra):
    frase = input("Digite sua frase: ")

    frase_decodificada = ''
    frase_inlst = [x for x in frase.lower().strip()]


    for y in frase_inlst:
        for letra,cod in cifra.items():   
            if y == cod:
                idx = frase_inlst.index(y)
                frase_inlst[idx] = letra

    for x in frase_inlst:
        frase_decodificada += x

    return frase_decodificada

def codificarMensagem(cifra):
    frase = input("Digite sua frase: ")

    frase_codificada = ''
    frase_inlst = [x for x in frase.lower().strip()]


    for i in frase_inlst:
        for letra,cod in cifra.items():    
            if i == letra:
                idx = frase_inlst.index(i)
                frase_inlst[idx] = cod

    for x in frase_inlst:
        frase_codificada += x

    return frase_codificada

cifra = {'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m',}

print("Deseja codificar ou decodificar uma mensagem?\n1 - codificar\n2 - decodificar\n")
descisao = int(input("Digite o número."))

match descisao:
    case 1:
        print(codificarMensagem(cifra))
    case 2:
        print(decodificarMensagem(cifra))
    case _:
        print("Essa opção não existe, tente novamente.")