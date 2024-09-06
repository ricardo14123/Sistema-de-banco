from datetime import datetime, timedelta

menu = """
==================
〡 [1] Depositar 〡
〡 [2] Sacar     〡
〡 [3] Extrato   〡
〡 [0] Sair      〡
==================

=> """

saldo = 1000
limite = 500
extrato = ""
numeros_de_saques = 0
LIMITE_SAQUES = 3
LIMITE_TRANSACOES_DIARIAS = 10
transacoes_diarias = 0
data_ultimo_reset = datetime.now().date()

while True:
    
    if datetime.now().date() != data_ultimo_reset:
        transacoes_diarias = 0
        data_ultimo_reset = datetime.now().date()

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            extrato += f"Depósito: R$ {valor:.2f} em {data_hora}\n"
            transacoes_diarias += 1

        else:
            print("Operação Falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numeros_de_saques >= LIMITE_SAQUES
        excedeu_transacoes_diarias = transacoes_diarias >= LIMITE_TRANSACOES_DIARIAS
        
        if excedeu_transacoes_diarias:
            print("Operação falhou! Limite diário de transações excedido.")

        elif excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            extrato += f"Saque: R$ {valor:.2f} em {data_hora}\n"
            numeros_de_saques += 1
            transacoes_diarias += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n===================== EXTRATO ====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("====================================================")
        
    elif opcao == "0":
        print("Obrigado por acessar o sistema do Banco Black")
        print("Agradecemos pela sua confiança em nossos serviços. Se precisar de qualquer assistência ou tiver alguma dúvida, não hesite em nos contatar.")
        print("Estamos sempre à disposição para ajudar você a alcançar seus objetivos financeiros.")
        print("Até breve e tenha um ótimo dia!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
