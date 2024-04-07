def deposito(saldo, valor, extrato):
    try:
        
        valor = float(valor)
        saldo += valor

        extrato += f"[d] Depósito de R$ {valor:.2f}\n"

        print(f"Depósito no valor de R$ {valor:.2f} realizado com sucesso!")

        return saldo, extrato

    except:
        print("Valor digitado é inválido, operação cancelada.")

def saque(*, saldo, valor, extrato, numero_saques, limite_saques, limite):
    if numero_saques < limite_saques:
        try:
            valor = float(valor)

            if saldo >= valor and valor <= limite:
                saldo -= valor
                numero_saques += 1

                extrato += f"[s] Saque de R$ {valor:.2f}\n"

                print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso!")

                return saldo, extrato
            else: 
                if saldo <= valor:
                    print("[!] Saldo insuficiente para efetuar o saque.")

                if valor >= limite:
                    print(f"[!] Valor excede o limite de R$ {limite:.2f} para cada saque.")

        except:
            print("Valor digitado é inválido. Operação cancelada.")
    else:
        print("[!] Limite de saques diário já excedido. Tente novamente amanhã.")

def tirar_extrato(saldo, *, extrato):
    print(extrato)

    print(f"Saldo em conta: R$ {saldo:.2f}")