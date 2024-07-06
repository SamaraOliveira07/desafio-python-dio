#Criando o menu do sistema
menu = """
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

==>"""

#Criando as variáveis
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

#Início do sistema
while True:

    opcao = input(menu)

    #parte de depósito
    if opcao == '1':
        print(f"""Depósito
    Saldo atual: R${saldo} """)
        deposito = int(input("""Qual o valor deseja depositar?: 
                             """))
        if deposito > 0:
            extrato += f"Depósito de R${deposito:.2f} efetuado.\n"
            saldo += deposito
            print('Valor depositado com sucesso. \nConfira seu extrato para visualizar a transação.')
        elif deposito <= 0:
            print('Valor inválido. Por favor, tente novamente.')

    #parte de saque
    elif opcao == '2':
        print('Saque')
        sacar = int(input('Qual valor deseja retirar?: '))
        if sacar <= saldo:
            quantidade = f"Você realizou {numero_saque} saques e possui {limite_saque} restantes. \nDeseja prosseguir?[S/N]: "
    #parte de extrato
    elif opcao == '3':
        print('Extrato')
        input(extrato)
        print(f'Saldo disponível: R${saldo}')

    #encerrar a sessão
    elif opcao == '4':
        print('Sessão encerrada. Obrigado por utilizar nossos sistemas!')
        break

    #erros do usuário
    else:
        print('Caracter inválido. Por favor, tente novamente.')