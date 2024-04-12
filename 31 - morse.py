def traduzir(frase,morse):
    '''
    Função rebece uma frase tipo srt e um dicionário para a substituição dos valores.

    Cria uma lista a partir de uma str, eliminando espaços em branco no início e no fim e formatando como minúsculas.
    Itera sobre a lista criada (frase_inlst) e compara com o dicionario morse, caso encontre a letra ele substitui pelo valor da key encontrada no dicionário. Substitui os espaços em branco por uma barra(/) e adiciona cada item da lista em uma frase traduzida e formatada (frase_formatada)

    Retorna a frase_formatada como uma str.
    '''
    frase_inlst = [x for x in frase.lower().strip()]
    frase_formatada = ''
    for i in frase_inlst:
        for letra,cod in morse.items():    
            if i == letra:
                idx = frase_inlst.index(i)
                frase_inlst[idx] = cod

    for i in frase_inlst:  
        if ' ' in frase_inlst:
            idx = frase_inlst.index(' ')
            frase_inlst.pop(idx)
            frase_inlst.insert(idx,"/")

    for i in frase_inlst:
        frase_formatada += ' '+i

    return frase_formatada.strip()

morse = {'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----','.':'.-.-.-',',':'--..--','?':'..--..','!':'-.-.--','´':'.----.','"':'.-..-.','(':'-.--.',')':'-.--.-','&':'.-...','---':'...',':':'---...',';':'-.-.-.','/':'-..-.','-':'..--.-','=':'-...-','+':'.-.-.','-':'-....-','$':'...-..-','@':'.--.-.'}

frase = input("Escreva uma frase e veja a tradução em código morse: ")

print(traduzir(frase,morse))