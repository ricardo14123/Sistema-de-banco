menu = """
==================
〡 [1] Depositar 〡
〡 [2] Sacar     〡
〡 [3] Extrato   〡
〡 [0] Sair      〡
==================

=> """

saldo = 0
limite = 500
extrato = ""
numeros_de_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ { valor:.2f}\n"

        else:
            print("Operação Falhou! O valor Informado é Inválido")

    elif opcao == "2":
        valor = float(input("informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numeros_de_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite")

        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            numeros_de_saques += 1

        else:
            print("Opeação falhou: O valor informado é inválido.")

    elif opcao == "3":
        print("\n=============== EXTRATO ===============")
        print("Nâo foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("\n=======================================")
        
    elif opcao == "0":
        print("Obrigado por acessar o sistema do banco break")
        print("Agradecemos pela sua confiança em nossos serviços. Se precisar de qualquer assistência ou tiver alguma dúvida, não hesite em nos contatar.")
        print("Estamos sempre à disposição para ajudar você a alcançar seus objetivos financeiros.")
        print("Até breve e tenha um ótimo dia!")
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")




