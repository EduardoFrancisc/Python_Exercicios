def imprimir_histograma(frequencia):
    print("Histograma das Letras da Frase:")
    for letra, freq in sorted(frequencia.items()):
        print(f"|{letra}: {'=' * freq}")
        
def contar_letras(texto):
    frequencia = {}
    for letra in texto:
        if letra.isalpha():
            letra = letra.lower()
            if letra in frequencia:
                frequencia[letra] += 1
            else:
                frequencia[letra] = 1
        else:
            print("Digite apenas letras!")
            break

    imprimir_histograma(frequencia)

texto = input("Digite o texto: ")
text_strp = texto.replace(' ','')
contar_letras(text_strp)