menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao.lower() == "d":
        print("Depósito")

        valor = input("Quanto o valor a ser depositado? ")
        
        try:
            valor = float(valor)
            saldo += valor

            extrato += f"[d] Depósito de R$ {valor:.2f}\n"

            print(f"Depósito no valor de R$ {valor:.2f} realizado com sucesso!")

        except:
            print("Valor digitado é inválido, operação cancelada.")

    elif opcao.lower() == "s":
        print("Saque")

        if numero_saques < LIMITE_SAQUES:
            valor = input("Quanto o valor a ser sacado? ")

            try:
                valor = float(valor)

                if saldo >= valor and valor <= limite:
                    saldo -= valor
                    numero_saques += 1

                    extrato += f"[s] Saque de R$ {valor:.2f}\n"

                    print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso!")
                else: 
                    if saldo <= valor:
                        print("[!] Saldo insuficiente para efetuar o saque.")

                    if valor >= limite:
                        print(f"[!] Valor excede o limite de R$ {limite:.2f} para cada saque.")

            except:
                print("Valor digitado é inválido. Operação cancelada.")

        else:
            print("[!] Limite de saques diário já excedido. Tente novamente amanhã.")

    
    elif opcao.lower() == "e":
        print("Extrato")

        print(extrato)

        print(f"Saldo em conta: R$ {saldo:.2f}")

    elif opcao.lower() == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")