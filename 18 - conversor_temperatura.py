def conversaoFahren(temp_celsius):
    """
    Função que recebe a temperatura em celsius e converte para fahrenheit
    """
    return temp_celsius * 1.8 + 32
    

temp_celsius = int(input("Qual a temperatura em celsius a ser convertida? "))
print("Temperatura em celsius:",temp_celsius)
print("Temperatura em fahrenheit:",conversaoFahren(temp_celsius))
