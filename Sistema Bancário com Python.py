menu = """
[0] Depósito
[1] Saque
[2] Extrato
[3] Sair

"""

Valor_conta = 0
Saques_realizados = 0

LIMITE_SAQUES = 3   
VALOR_LIMITE = 500

extrato = ""

while True:
    print(menu)
    operacao = int(input("Operação que deseja realizar: "))

    if(operacao == 0):
        valor = float(input("Digite o valor a ser depositado: "))
        if(valor > 0):
            Valor_conta += valor
            extrato += f"Deposito: R$ {valor:.2f} \n"
            print("Valor depositado com sucesso!")
        else:
            print("Valor inválido!")

    elif(operacao == 1):
        valor = float(input("Digite o valor a ser sacado: "))

        valor_insuficinete = valor > Valor_conta
        exedeu_saque_Limite = valor > VALOR_LIMITE
        exedeu_qtd_Saque = Saques_realizados >= LIMITE_SAQUES


        if(valor_insuficinete):
            print("Saldo insuficiente!")
        elif(exedeu_saque_Limite):
            print("Valor superior ao valor limite de saque")
        elif(exedeu_qtd_Saque):
            print("Limite de saque diário atingido")

        elif(valor > 0):
            Valor_conta -= valor
            extrato += f"Saque: R$ {valor:.2f} \n" 
            Saques_realizados += 1
            print("Saque realizado com sucesso!")
        else:
            print("Valor inválido!")
    
    elif(operacao == 2):
        print("================= EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações")
        else:   
            print(f"{extrato}\nSaldo Atual:R$ {Valor_conta:.2f}")
        print("==========================================")

    elif(operacao == 3):
        print("Obrigado por usar nosso sistema!")
        break

    else: 
        print("Comando inválido")