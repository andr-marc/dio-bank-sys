import funcoes as fn
import contas as ct

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Cadastrar usuário
[c] Cadastrar conta corrente
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []
contas = []
AGENCIA = "0001"

while True:
    opcao = input(menu)
    if opcao.lower() == "d":
        print("Depósito")
        valor = input("Quanto o valor a ser depositado? ")
        saldo, extrato = fn.deposito(saldo, valor, extrato)
        
    elif opcao.lower() == "s":
        print("Saque")
        valor = input("Quanto o valor a ser sacado? ")
        saldo, extrato = fn.saque(saldo=saldo, valor=valor, extrato=extrato, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES, limite=limite)

    elif opcao.lower() == "e":
        print("Extrato")
        fn.tirar_extrato(saldo, extrato=extrato)

    elif opcao.lower() == "u":
        print("Cadastrar novo usuário")
        usuarios.append(ct.cadastrar_usuario(usuarios=usuarios))

    elif opcao.lower() == "c":
        print("Cadastrar nova conta corrente")
        contas.append(ct.cadastrar_conta(usuarios=usuarios, agencia=AGENCIA, contas=contas))
       
    elif opcao.lower() == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
