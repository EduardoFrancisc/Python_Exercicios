lista_numerica = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in lista_numerica:
    if i % 2 == 0:
        lista_numerica.remove(i)

print("Números ínpares da lista:",lista_numerica)