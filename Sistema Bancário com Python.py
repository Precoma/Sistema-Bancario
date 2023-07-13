def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n=== Usuário criado com sucesso! ===")



def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
        print("\n=== Conta criada com sucesso! ===")
    
    else:
        print("Usuário não encontrado!")



def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def Saque(*, saldo, valor, extrato, numero_saques, limite_saques, valor_limite):
    valor_insuficinete = valor > saldo
    exedeu_saque_Limite = valor > valor_limite
    exedeu_qtd_Saque = numero_saques >= limite_saques

    if(valor_insuficinete):
        print("Saldo insuficiente!")
        
    elif(exedeu_saque_Limite):
        print("Valor superior ao valor limite de saque")
        
    elif(exedeu_qtd_Saque):
        print("Limite de saque diário atingido")
    
    elif(valor > 0):
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f} \n" 
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Valor inválido!")
        
    return saldo, extrato, numero_saques
    
def Deposito(saldo, valor, extrato,/):
    novo_valor = saldo + valor
    extrato += f"Deposito: R$ {valor:.2f} \n"
    print("Valor depositado com sucesso!")

    return novo_valor, extrato


def Exibir_extrato(Valor_conta, / , * , extrato):
    print("================= EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações")
    else:   
        print(f"{extrato}\nSaldo Atual:R$ {Valor_conta:.2f}")
    print("==========================================")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print(linha)
        print("=" * 100)

def main():
    Valor_conta = 0
    Saques_realizados = 0

    LIMITE_SAQUES = 3   
    VALOR_LIMITE = 500
    AGENCIA = "0001"

    usuarios = []
    contas = []
    extrato = ""

    menu = """
[0] Depósito
[1] Saque
[2] Extrato
[3] Criar Usuario
[4] Criar Conta
[5] Listar Contas
[6] Sair

"""
    while True:
        print(menu)
        operacao = int(input("Operação que deseja realizar: "))

        if(operacao == 0):
            valor = float(input("Digite o valor a ser depositado: "))
            if(valor > 0):
                Valor_conta, extrato = Deposito(Valor_conta, valor, extrato)
            else:
                print("Valor inválido!")

        elif(operacao == 1):
            valor = float(input("Digite o valor a ser sacado: "))
            Valor_conta, extrato, Saques_realizados = Saque(valor = valor, saldo = Valor_conta, extrato = extrato, numero_saques = Saques_realizados, limite_saques = LIMITE_SAQUES, valor_limite = VALOR_LIMITE )

        elif(operacao == 2):
            Exibir_extrato(Valor_conta, extrato = extrato)

        elif(operacao == 3):
            criar_usuario(usuarios)

        elif(operacao == 4):
            criar_conta(AGENCIA, len(contas)+1, usuarios, contas)

        elif(operacao == 5):
            listar_contas(contas)

        elif(operacao == 6):
            print("Obrigado por utilizar nosso sistema!")
            break

        else: 
            print("Comando inválido")

main()
