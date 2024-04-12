import random

lista_dados = []
freq1_lista = 0
freq2_lista = 0
freq3_lista = 0
freq4_lista = 0
freq5_lista = 0
freq6_lista = 0
soma_dados = 0

def jogarDado():
  """
  Retorna um dado de seis faces.
  """
  dado = int((random.random() * 6) + 1)
  return dado

quantidada_de_dados = int(input("Digite quantos dados deseja jogar:"))

for i in range(quantidada_de_dados):
  lista_dados.append(jogarDado())

for i in lista_dados:
  soma_dados +=i

media_dados = soma_dados/quantidada_de_dados

for i in lista_dados:
   if i == 1:
     freq1_lista += 1
   elif i == 2:
     freq2_lista += 1
   elif i == 3:
     freq3_lista += 1
   elif i == 4:
     freq4_lista += 1
   elif i == 5:
     freq5_lista += 1
   elif i == 6:
     freq6_lista += 1

print("Lista com",quantidada_de_dados,"dados:",lista_dados)
print("Média da soma dos dados: ",media_dados)
print("Freqência dos elementos na lista:\n1:",freq1_lista,"\n2:",freq2_lista,"\n3:",freq3_lista,"\n4:",freq4_lista,"\n5:",freq5_lista,"\n6:",freq6_lista)