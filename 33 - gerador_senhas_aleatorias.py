import random as rd

def geraLetra():

    letras = ['a', 'e', 'i', 'o','u','b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y','z']
    final_letra = ''

    letra_rd = str(rd.choice(letras))

    sort_num=rd.randint(0,1)

    match sort_num:
        case 0:
            final_letra = letra_rd.upper()
        case 1:
            final_letra = letra_rd.lower()
    
    return final_letra
    
def geraNumero():
    num_rd = rd.randint(0,9)
    return str(num_rd)

def geraCaracterEspecial():
    caracteres = ["'",'"','!','#','$','%','¨','&','*','(',')','-','_','=','+','`','´','[',']','{','}','~','^','?','/','<',',','>','.','|']

    carac_esp = rd.choice(caracteres)

    return carac_esp

def gerarSenha(comprimento):
    senha = ''
    while len(senha) < comprimento:
        num_aleator = rd.randint(0,2)

        match num_aleator:
            case 0:
                senha += geraLetra()
            case 1:
                senha += geraNumero()
            case 2:
                senha += geraCaracterEspecial()      
    return senha

comprimento = input("Digite o comprimento para sua senha: ")

if comprimento == '0':
    print("Por favor, digite um valor maior que 0.")
else:
    if comprimento.isdecimal():
        print("Sua senha gerada aleatoriamente:", gerarSenha(int(comprimento)))
    else:
            print("Por favor, digite apenas números.")
