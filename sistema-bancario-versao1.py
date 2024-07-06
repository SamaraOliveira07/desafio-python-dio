#biblioteca importada
import time

#Criando o menu do sistema
menu = """\033[1m
============================
BEM VINDO AO (NOME DO BANCO)
============================
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

==>\033[m"""

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
        print(f"""\033[1;33mDepósito\033[m
Saldo atual: R${saldo} """)
        deposito = float(input("""\033[1mQual o valor deseja depositar?: """))
        if deposito > 0:
            extrato += f"Depósito de R${deposito:.2f} efetuado.\n"
            saldo += deposito
            print("""\033[1;32m
Valor depositado com sucesso. \nConfira seu extrato para visualizar a transação.\033[m""")
        elif deposito <= 0:
            print('\033[1;31mValor inválido. Por favor, tente novamente.\033[m')

    #parte de saque
    elif opcao == '2':
        print('\033[1;33mSaque\033[m')
        sacar = float(input('\033[1mQual valor deseja retirar? (Máx. R$500,00): '))
        if sacar > saldo:
            print('\033[1;31mSaldo insuficiente. Por favor, tente novamente.\033[m')
        if (sacar <= saldo) and (numero_saque <= 3) and (limite_saque != 0):
            p = str(input(f"Você realizou {numero_saque} saques e possui {limite_saque} disponível. \nDeseja prosseguir?[S/N]: ")).strip().upper()
            if (p == 'S'):
                if (sacar <= 500) and (sacar > 0):
                    saldo -= sacar
                    numero_saque += 1
                    limite_saque -= 1
                    extrato += f'Saque de R${sacar:.2f} efetuado.\n'
                    print(f"""\033[1;32m
R${sacar:.2f} retirados. \nProcessando notas, aguarde...\033[m""")
                    time.sleep(1)
                else:
                    print("""\033[1;31m
Você só pode sacar valores abaixo de R$500,00. \nPor favor, tente novamente.\033[m""")
            elif (p == 'N'):
                print('Retornando ao menu principal...')
                time.sleep(1)
            else:
                print('\033[1;31mCaracter inválido. Por favor, tente novamente.\033[m')
        if (numero_saque >= 3) and (limite_saque <= 0):
            print("""\033[1;31m
Você não possui mais saques disponíveis. \nPor favor, verifique o extrato da conta.\033[m""")
        
    #parte de extrato
    elif opcao == '3':
        print('\033[1;33mExtrato (Aperte ENTER para voltar ao menu.)\033[m')
        print(f'\033[1mSaldo disponível: R${saldo}')
        print(input(extrato))
        

    #encerrar a sessão
    elif opcao == '4':
        print('\033[1mSessão encerrada. Obrigado por utilizar nosso sistema!')
        time.sleep(1)
        break

    #erros do usuário
    elif opcao != '1234':
        print('\033[1;31mCaracter inválido. Por favor, tente novamente.\033[m')