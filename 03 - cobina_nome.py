primeiro_nome = input("Digite o primeiro nome:")
segundo_nome = input("Digite o segundo nome:")

parte1 = primeiro_nome[:5]
parte2 = segundo_nome[:5]

nome_combinado = parte1 + parte2
nome_final = nome_combinado.capitalize()

print("Nome final: " + nome_final)