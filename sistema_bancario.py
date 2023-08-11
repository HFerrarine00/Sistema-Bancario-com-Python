menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    #Depósito
    if opcao == "d":            
        print("Depósito")
        deposito = float(input("Quanto você deseja depositar? "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"
        else:
            print("Você não pode digitar esse valor_saque, tente novamente.")
            
    #Saque
    elif opcao == "s":
        print("Saque")
        valor_saque = float(input("Quanto você deseja sacar? "))
        if valor_saque <= 500 and saldo >= valor_saque and LIMITE_SAQUES > 0:
            saldo -= valor_saque
            extrato += f"Saque: R${valor_saque:.2f}\n"
            LIMITE_SAQUES -= 1

        elif valor_saque > 500:
            print("Você só pode sacar R$500.00 por saque.")

        elif saldo < valor_saque:
            print("Não é possivel sacar, saldo insuficiente!")

        else:
            print("Limite de saque diário excedido, tente novamente amanhã.")

    #Extrato
    elif opcao == "e":
        print("================== Extrato ==================")
        print()
        print(extrato)
        print()
        print(f"Saldo: R${saldo:.2f}")
        print("=============================================")

    #Sair
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")