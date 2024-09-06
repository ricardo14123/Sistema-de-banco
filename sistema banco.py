from datetime import datetime

# Constantes
LIMITE_SAQUES = 3
LIMITE_SAQUE = 500

# Variáveis globais
usuarios = {}  # Dicionário para armazenar usuários e suas informações
contas_correntes = {}  # Dicionário para armazenar contas correntes de cada usuário
usuario_atual = None
data_ultimo_reset = datetime.now().date()

# Função para resetar as transações diárias ao mudar o dia
def resetar_transacoes_diarias():
    global data_ultimo_reset
    if datetime.now().date() != data_ultimo_reset:
        data_ultimo_reset = datetime.now().date()
        for conta in contas_correntes.values():
            conta['numeros_de_saques'] = 0
        print("Transações diárias resetadas.")

# Função para criar um novo usuário
def criar_usuario():
    global usuarios
    cpf = input("Informe o CPF do usuário: ")
    senha = input("Informe a senha do usuário: ")
    if cpf in usuarios:
        print("Usuário já existe!")
    else:
        usuarios[cpf] = {
            'senha': senha
        }
        print(f"Usuário com CPF '{cpf}' criado com sucesso!")

# Função para criar uma conta corrente para um usuário
def criar_conta_corrente(cpf_usuario):
    global contas_correntes
    if cpf_usuario in contas_correntes:
        print(f"Conta corrente para CPF '{cpf_usuario}' já existe!")
    else:
        nome_completo = input("Informe o nome completo do usuário: ")
        data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
        endereco = input("Informe o endereço do usuário: ")
        if not nome_completo or not data_nascimento or not endereco:
            print("Todos os campos são obrigatórios!")
            return
        contas_correntes[cpf_usuario] = {
            'nome_completo': nome_completo,
            'cpf': cpf_usuario,
            'data_nascimento': data_nascimento,
            'endereco': endereco,
            'saldo': 0,
            'extrato': "",
            'numeros_de_saques': 0
        }
        print(f"Conta corrente criada para CPF '{cpf_usuario}' com sucesso!")

# Função para listar todas as contas correntes
def listar_contas():
    global contas_correntes
    if not contas_correntes:
        print("Não há contas correntes cadastradas.")
    else:
        print("\n===================== LISTA DE CONTAS ====================")
        for cpf, conta in contas_correntes.items():
            print(f"CPF: {cpf}")
            print(f"  Nome Completo: {conta['nome_completo']}")
            print(f"  Saldo: R$ {conta['saldo']:.2f}")
            print(f"  Número de saques: {conta['numeros_de_saques']}")
            print(f"  Data de Nascimento: {conta['data_nascimento']}")
            print(f"  Endereço: {conta['endereco']}")
            print("===========================================================")

# Função para adicionar saldo à conta do usuário
def adicionar_saldo(cpf_usuario, valor):
    global contas_correntes
    if cpf_usuario not in contas_correntes:
        print("Conta não encontrada!")
        return
    if valor <= 0:
        print("O valor para adição deve ser positivo.")
        return
    
    conta = contas_correntes[cpf_usuario]
    conta['saldo'] += valor
    data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    conta['extrato'] += f"Adição de saldo: R$ {valor:.2f} em {data_hora}\n"
    print(f"Saldo de R$ {valor:.2f} adicionado com sucesso!")

# Função para realizar depósito, aceitando apenas argumentos por posição
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        extrato += f"Depósito: R$ {valor:.2f} em {data_hora}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

# Função para realizar saque, aceitando apenas argumentos nomeados
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques, cpf_usuario):
    senha = input("Digite a senha para realizar o saque: ")
    if cpf_usuario not in contas_correntes:
        print("Conta não encontrada!")
        return saldo, extrato
    if senha != usuarios[cpf_usuario]['senha']:
        print("Senha incorreta!")
        return saldo, extrato

    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato

    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > limite:
        print(f"Operação falhou! Limite de saque de R$ {limite:.2f} excedido.")
    elif numero_saques >= limite_saques:
        print(f"Operação falhou! Número máximo de {limite_saques} saques diários excedido.")
    else:
        saldo -= valor
        data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        extrato += f"Saque: R$ {valor:.2f} em {data_hora}\n"
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    
    return saldo, extrato

# Função para exibir o extrato, aceitando saldo por posição e extrato por nome
def exibir_extrato(saldo, *, extrato):
    print("\n===================== EXTRATO ====================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("====================================================")

# Função para exibir o extrato de outro usuário
def exibir_extrato_usuario():
    global contas_correntes
    cpf_usuario = input("Informe o CPF do usuário para exibir o extrato: ")
    senha = input("Digite a senha para exibir o extrato do usuário: ")
    if cpf_usuario in contas_correntes:
        if senha == usuarios[cpf_usuario]['senha']:
            conta = contas_correntes[cpf_usuario]
            exibir_extrato(conta['saldo'], extrato=conta['extrato'])
        else:
            print("Senha incorreta!")
    else:
        print("Usuário não encontrado!")

# Função para exibir o menu e obter a escolha do usuário
def exibir_menu():
    menu = """
    ==============================
    〡 [1] Criar Usuário        〡
    〡 [2] Criar Conta Corrente 〡
    〡 [3] Adicionar Saldo      〡
    〡 [4] Sacar Direto         〡
    〡 [5] Listar Contas        〡
    〡 [6] Exibir Extrato       〡
    〡 [0] Sair                 〡
    ==============================

    => """
    return input(menu)

# Função principal que gerencia o sistema bancário
def sistema_bancario():
    global usuario_atual
    
    while True:
        if usuario_atual is None:
            opcao = exibir_menu()
            if opcao == "1":
                criar_usuario()
            elif opcao == "2":
                cpf_usuario = input("Informe o CPF do usuário para criar a conta corrente: ")
                if cpf_usuario in usuarios:
                    criar_conta_corrente(cpf_usuario)
                else:
                    print("Usuário não encontrado!")
            elif opcao == "3":
                cpf_usuario = input("Informe o CPF do usuário para adicionar saldo: ")
                try:
                    valor = float(input("Informe o valor a ser adicionado: "))
                    adicionar_saldo(cpf_usuario, valor)
                except ValueError:
                    print("Valor inválido. Tente novamente.")
            elif opcao == "4":
                cpf_usuario = input("Informe o CPF do usuário para realizar o saque: ")
                if cpf_usuario in contas_correntes:
                    try:
                        valor = float(input("Informe o valor do saque: "))
                        conta = contas_correntes[cpf_usuario]
                        saldo, extrato = sacar(
                            saldo=conta['saldo'], 
                            valor=valor, 
                            extrato=conta['extrato'], 
                            limite=LIMITE_SAQUE, 
                            numero_saques=conta['numeros_de_saques'], 
                            limite_saques=LIMITE_SAQUES,
                            cpf_usuario=cpf_usuario
                        )
                        conta['saldo'] = saldo
                        conta['extrato'] = extrato
                        conta['numeros_de_saques'] += 1
                    except ValueError:
                        print("Valor inválido. Tente novamente.")
                else:
                    print("Conta não encontrada!")
            elif opcao == "5":
                listar_contas()
            elif opcao == "6":
                exibir_extrato_usuario()
            elif opcao == "0":
                print("Obrigado por acessar o sistema do Banco Black.")
                print("Agradecemos pela sua confiança. Até breve!")
                break
            else:
                print("Operação inválida! Tente novamente.")
        else:
            resetar_transacoes_diarias()
            conta = contas_correntes[usuario_atual]
            saldo = conta['saldo']
            extrato = conta['extrato']
            numeros_de_saques = conta['numeros_de_saques']

            opcao = exibir_menu()

            if opcao == "1":
                try:
                    valor = float(input("Informe o valor do depósito: "))
                    saldo, extrato = depositar(saldo, valor, extrato)
                    conta['saldo'] = saldo
                    conta['extrato'] = extrato
                except ValueError:
                    print("Valor inválido. Tente novamente.")
            elif opcao == "2":
                try:
                    valor = float(input("Informe o valor do saque: "))
                    saldo, extrato = sacar(
                        saldo=saldo, 
                        valor=valor, 
                        extrato=extrato, 
                        limite=LIMITE_SAQUE, 
                        numero_saques=numeros_de_saques, 
                        limite_saques=LIMITE_SAQUES,
                        cpf_usuario=usuario_atual
                    )
                    conta['saldo'] = saldo
                    conta['extrato'] = extrato
                    conta['numeros_de_saques'] += 1
                except ValueError:
                    print("Valor inválido. Tente novamente.")
            elif opcao == "3":
                exibir_extrato(saldo, extrato=extrato)
            elif opcao == "4":
                try:
                    valor = float(input("Informe o valor do saque: "))
                    saldo, extrato = sacar(
                        saldo=saldo, 
                        valor=valor, 
                        extrato=extrato, 
                        limite=LIMITE_SAQUE, 
                        numero_saques=numeros_de_saques, 
                        limite_saques=LIMITE_SAQUES,
                        cpf_usuario=usuario_atual
                    )
                    conta['saldo'] = saldo
                    conta['extrato'] = extrato
                    conta['numeros_de_saques'] += 1
                except ValueError:
                    print("Valor inválido. Tente novamente.")
            elif opcao == "5":
                listar_contas()
            elif opcao == "6":
                exibir_extrato_usuario()
            elif opcao == "0":
                print("Obrigado por acessar o sistema do Banco Black.")
                print("Agradecemos pela sua confiança. Até breve!")
                break
            else:
                print("Operação inválida! Tente novamente.")

# Executa o sistema bancário
sistema_bancario()
