tempo_em_minutos_fornecido = int(input("Digite a quantidade de minutos: "))

horas = tempo_em_minutos_fornecido // 60
minutos = int(tempo_em_minutos_fornecido - horas * 60)

print("Conversão de minutos fornecidos em horas e minutos:",horas,"h e",minutos," minutos")

minutos_totais = horas * 60 + minutos

print("Conversão de horas e minutos para minutos totais:",minutos_totais)