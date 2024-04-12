operacao_escolha_usuario = input("Escolha um operação matemática:(+,-,*,/)")
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

if operacao_escolha_usuario == "+":
    resultado_adicao = primeiro_numero + segundo_numero
    print("Resultado da Adiçao:",resultado_adicao)
elif operacao_escolha_usuario == "-":
    resultado_subtracao = primeiro_numero - segundo_numero
    print("Resultado da Subtração:",resultado_subtracao)
elif operacao_escolha_usuario == "*":
    resultado_multiplicacao = primeiro_numero * segundo_numero
    print("Resultado da Multiplicação:",resultado_multiplicacao)
elif operacao_escolha_usuario == "/":
    resultado_divisao = primeiro_numero / segundo_numero
    print("Resultado da Divisão:",resultado_divisao)
else: 
    print("Não foi possível calcular.")