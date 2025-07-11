menu = """
Seja bem-vindo ao banco, qual operação deseja realizar?

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        valor_depositado = float(input("Digite o valor que deseja depositar:"))
        
        if valor_depositado > 0:
            saldo += valor_depositado
            extrato += f"Depósito: {valor_depositado:.2f}\n"
            print(f'Valor de R$ {valor_depositado:.2f} depositado!')
        else:
            print("Valor invalido!")

    elif opcao == "s":
        valor_sacado = float(input("Digite o valor que deseja sacar:"))
        
        exedeu_saldo = valor_sacado > saldo #Para verificar se passou do limite de saldo da conta
        
        exedeu_limite = valor_sacado > limite #para verificar se passou do limite de R$500

        exedeu_saque = numero_saques >= LIMITE_SAQUES #para verificar o se passou do limite de saques

        if exedeu_saldo:
            print('O saldo é insuficiente! Operação cancelada!')
        elif exedeu_limite:
            print("O seu limite de saque é de R$500,00")
        elif exedeu_saque:
            print("O seu limite de saques foi atingido!")
        elif valor_sacado > 0:
            saldo -= valor_sacado
            print(f"O valor sacado foi de R$ {valor_sacado:.2f}")
            extrato += f"Saque: R$ {valor_sacado:.2f}\n"
            numero_saques += 1
        else:
            print("A operação falhou! Informe novos valores")


    elif opcao == "e":
        print('\n =======Extrato=======')
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================")
        

    elif opcao == 'q':
        break

    else:
        print("Operação invalida, digite novamente o que deseja.")

