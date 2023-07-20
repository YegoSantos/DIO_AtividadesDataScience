menu = """

[1]depositar
[2]sacar
[3]extrato
[0]sair

=> """
saque = 0
deposito = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input("Quanto você quer depositar?"))
        saldo += deposito
        extrato += f"Depósito: R${deposito}\n"
        print("Depósito realizado com sucesso!")
    elif opcao == 2:
        saque = float(input("Qual o valor do saque?"))
        if saque > saldo:
            print("Saldo Insuficiente")
        elif numero_saques < LIMITE_SAQUE:
            if saque <= limite:
                numero_saques += 1
                saldo -= saque
                extrato += f"Valor do saque: R${saque}\n"
                print("Saque realizado com sucesso!")
            else:
                print("Não foi possivel realizar sua operação, Seu limite saque é de R$500")
        else:
            print("Voçê não pode realizar mais de 3 saques no mesmo dia!")
    elif opcao == 3:
        if extrato == "":
            print("Não foram realizadas movimentações")
        else:
            extrato += f"Seu saldo é: R${saldo} \n"
            print(extrato)
    elif opcao == 0:
        print("Obrigado por utilizar nosso sistema bancario!:)")
        break
        
    else:
        print("Escolha uma das opcões!")
    
