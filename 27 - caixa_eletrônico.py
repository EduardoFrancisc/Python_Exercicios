saldo = 1000
print('Seu saldo é de:', saldo)
while True:
    print('1-sacar\n2-depositar\n3-sair')
    escolha_principal = int(input('faça sua escolha.'))
    if escolha_principal == 1:
        print('Opção saque selecionada:')
        saque = int(input('Quanto deseja sacar:'))
        saldo -= saque

        resto = saque % 50
        numero_de_notas_cinquenta = (saque - resto) / 50

        resto_de_dez = resto % 10
        numero_de_notas_dez = (resto - resto_de_dez) / 10

        resto_de_cinco = resto_de_dez % 5
        numero_de_otas_cinco = (resto_de_dez - resto_de_cinco) / 5

        resto_de_um = resto_de_cinco % 1
        numero_de_notas_um = (resto_de_cinco - resto_de_um) / 1

        print("Saque realizado com sucesso! \nNotas entregues:",numero_de_notas_cinquenta,"de B$50,",numero_de_notas_dez,"de B$10,", numero_de_otas_cinco,"de B$5 e",numero_de_notas_um,"de B$1.")
    elif escolha_principal == 2:
        print('Opção depósito selecionada:')
        deposito = int(input('Quanto deseja depositar:'))
        saldo += deposito
        print('Depóaito de R$',deposito,'realizado com sucesso.')
    elif escolha_principal == 3:
        break