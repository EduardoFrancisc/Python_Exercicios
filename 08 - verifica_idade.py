usuario_idade = int(input("Digite sua idade:"))

if usuario_idade < 18:
    print("O usuário é menor de idade,",usuario_idade,"anos")
elif usuario_idade >= 18:
    print("O usuário é maior de idade,",usuario_idade,"anos")