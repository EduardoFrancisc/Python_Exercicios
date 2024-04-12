numeros_s = input("Digite a lista de números: ")
lista_formatada = numeros_s.strip().replace(',','.').split(' ')

soma = 0

for i in lista_formatada:
    soma += float(i)

media = soma/len(lista_formatada)
media_formatada = "{:.2f}".format(media)

print("Lista:",numeros_s)
print("A média:",media_formatada)