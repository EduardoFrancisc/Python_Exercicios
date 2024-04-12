sair = True
cadidato_joao = 0
cadidato_maria = 0
cadidato_jose = 0

def numeroDeVotos():
    print("Número de votos do candidato João:",cadidato_joao)
    print("Número de votos da candidata Maria:",cadidato_maria)
    print("Número de votos do candidato José:",cadidato_jose)

while(sair):

    escolha_usuario = int(input("Deseja [1] - votar em alguma opção ou [2] - sair do programa?"))
    
    if escolha_usuario == 1:
        voto_usuario = int(input("[1] - João \n [2] - Maria \n [3] - José"))
        
        if voto_usuario == 1:
            cadidato_joao +=1
            numeroDeVotos()
        elif voto_usuario == 2:
            cadidato_maria +=1
            numeroDeVotos()
        elif voto_usuario == 3:
            cadidato_jose +=1
            numeroDeVotos()
        else:
            print("Esse candidato não existe.")
    elif escolha_usuario == 2:
        sair = False
    else:
        print("Opção inexistente.")
        sair = False