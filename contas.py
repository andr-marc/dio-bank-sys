def verificar_cpf(usuarios):
    cpf = input('Por favor, informe seu CPF: ')
    cpf.replace(".", "")
    cpf.replace("-", "")

    
    for usuario in usuarios:
        if usuario.get("cpf") == cpf:
            return True, cpf
    return False, cpf

def cadastrar_usuario(*, usuarios):
    eh_usuario, cpf = verificar_cpf(usuarios)

    if eh_usuario: 
        print("[!] Usuário já cadastrado!")
    else: 
        nome = input("Informe seu nome: ")
        data_nascimento = input("Informe sua data de nascimento (DD/MM/AAAA): ")
        logradouro  = input("Informe seu lograroudo: ")
        numero = input("Informe o número: ")
        bairro = input("Informe o seu bairro: ")
        cidade = input("Informe a sua cidade: ")
        uf = input("Informe sua UF: ")

        enderco = f"{logradouro}, {numero} - {bairro} - {cidade}/{uf}"

        print(f"Usuário {nome} cadastrado com sucesso!")
        return {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "enderco": enderco}

def cadastrar_conta(*, usuarios, agencia, contas):
    eh_usuario, cpf = verificar_cpf(usuarios)

    if eh_usuario: 
        usuario = list(filter(lambda usuario: usuario.get("cpf") == cpf, usuarios))
        
        print(f"Conta corrente de {usuario[0].get('nome')} cadastrada com sucesso!")
        return {"agencia": agencia, "conta": len(contas) + 1, "usuario": usuario }
    else: 
        print("[!] Usuário não cadastrado!")