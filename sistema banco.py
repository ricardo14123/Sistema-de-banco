from abc import ABC, abstractmethod
from datetime import datetime
import random

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Historico:
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta, senha):
        pass
    
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta, senha):
        sucesso_transacao = conta.sacar(self.valor, senha)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta, senha=None):
        sucesso_transacao = conta.depositar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Conta:
    def __init__(self, cliente, senha):
        self._saldo = 0
        self._numero = random.randint(100000, 999999)  # Gera número aleatório
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        self._senha = senha
        
    @classmethod
    def nova_conta(cls, cliente, senha):
        return cls(cliente, senha)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    @property
    def senha(self):
        return self._senha
    
    def sacar(self, valor, senha):
        if senha != self.senha:
            print("\nOperação falhou! Senha incorreta.")
            return False
        
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")
        elif valor > 0:
            self._saldo -= valor
            print("\nSaque realizado com sucesso!")
            return True
        else:
            print("\nOperação falhou! O valor informado é inválido.")
            
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\nDepósito realizado com sucesso!")
            return True
        else:
            print("\nOperação falhou! O valor informado é inválido.")
            return False

class ContaCorrente(Conta):
    def __init__(self, cliente, senha, limite=500, limite_saques=3):
        super().__init__(cliente, senha)
        self.limite = limite
        self.limite_saques = limite_saques
        
    def sacar(self, valor, senha):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == "Saque"]
        )
        
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques
        
        if excedeu_limite:
            print("\nOperação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("\nOperação falhou! Número máximo de saques excedido.")
        else:
            return super().sacar(valor, senha)
        
        return False        

    def __str__(self):
        return f"""\
        {'*' * 30}
        {'Conta Corrente':^30}
        {'*' * 30}
        Agência:\t\t{self.agencia:<6}
        Número:\t\t{self.numero:<10}
        Titular:\t\t{self.cliente.nome:<20}
        Saldo:\t\t\tR$ {self.saldo:,.2f}
        {'*' * 30}
        """

class Menu:
    def __init__(self):
        self.clientes = {}
        self.contas = {}
        
    def exibir_menu(self):
        print("\n===== ESCOLHA UMA OPÇÃO =====")
        print("〡[1] Criar Usuário         〡")
        print("〡[2] Criar Conta Corrente  〡")
        print("〡[3] Adicionar Saldo       〡")
        print("〡[4] Sacar Dinheiro        〡")
        print("〡[5] Listar Contas         〡")
        print("〡[6] Exibir Extrato        〡")
        print("〡[0] Sair                  〡")
        print("=============================")
        
    def criar_usuario(self):
        cpf = input("Digite o CPF do usuário: ")
        
        if cpf in self.clientes:
            print("Cliente já existe!")
            return
        
        nome = input("Digite o nome do usuário: ")
        data_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Digite o endereço do usuário: ")
        
        cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
        self.clientes[cpf] = cliente
        print(f"Usuário {nome} criado com sucesso!")
        
    def criar_conta_corrente(self):
        cpf = input("Digite o CPF do cliente: ")
        
        if cpf not in self.clientes:
            print("Cliente não encontrado!")
            return
        
        senha = input("Digite a senha para a nova conta corrente: ")
        cliente = self.clientes[cpf]
        
        # Verifica se o cliente já tem uma conta
        if any(conta.cliente.cpf == cpf for conta in cliente.contas):
            print("Cliente já possui uma conta corrente!")
            return
        
        conta = ContaCorrente.nova_conta(cliente, senha)
        cliente.adicionar_conta(conta)
        self.contas[conta.numero] = conta
        print(f"Conta Corrente {conta.numero} criada com sucesso!")
        
    def adicionar_saldo(self):
        numero = int(input("Digite o número da conta: "))
        valor = float(input("Digite o valor a ser depositado: "))
        
        if numero in self.contas:
            conta = self.contas[numero]
            deposito = Deposito(valor)
            deposito.registrar(conta)
        else:
            print("Conta não encontrada!")
        
    def sacar_dinheiro(self):
        numero = int(input("Digite o número da conta: "))
        valor = float(input("Digite o valor a ser sacado: "))
        
        if numero in self.contas:
            conta = self.contas[numero]
            senha = input("Digite a senha da conta: ")
            saque = Saque(valor)
            saque.registrar(conta, senha)
        else:
            print("Conta não encontrada!")
        
    def listar_contas(self):
        if self.contas:
            print(f"\n{'*' * 50}")
            print(f"{'Listagem de Contas':^50}")
            print(f"{'*' * 50}")
            print(f"{'Nome':<20} {'Número':<10} {'Agência':<10} {'Tipo':<15}")
            print(f"{'-' * 50}")
            
            for numero, conta in self.contas.items():
                tipo = 'Conta Corrente'
                print(f"{conta.cliente.nome:<20} {conta.numero:<10} {conta.agencia:<10} {tipo:<15}")
            
            print(f"{'*' * 50}")
        else:
            print("Nenhuma conta encontrada!")
        
    def exibir_extrato(self):
        numero = int(input("Digite o número da conta: "))
        
        if numero in self.contas:
            conta = self.contas[numero]
            senha = input("Digite a senha da conta: ")
            if senha != conta.senha:
                print("\nOperação falhou! Senha incorreta.")
                return
            
            print(f"\n{'*' * 50}")
            print(f"{'Extrato da Conta Corrente':^50}")
            print(f"{'*' * 50}")
            print(f"{'Agência:':<20}{conta.agencia:<10}")
            print(f"{'Número:':<20}{conta.numero:<10}")
            print(f"{'Titular:':<20}{conta.cliente.nome:<20}")
            print(f"{'Saldo:':<20}R$ {conta.saldo:,.2f}")
            print(f"{'*' * 50}")
            print(f"{'Data':<20} {'Tipo':<15} {'Valor':>10}")
            print(f"{'-' * 50}")
            
            for transacao in conta.historico.transacoes:
                print(f"{transacao['data']:<20} {transacao['tipo']:<15} R$ {transacao['valor']:>10,.2f}")
            
            print(f"{'*' * 50}")
        else:
            print("Conta não encontrada!")
        
    def iniciar(self):
        while True:
            self.exibir_menu()
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                self.criar_usuario()
            elif opcao == '2':
                self.criar_conta_corrente()
            elif opcao == '3':
                self.adicionar_saldo()
            elif opcao == '4':
                self.sacar_dinheiro()
            elif opcao == '5':
                self.listar_contas()
            elif opcao == '6':
                self.exibir_extrato()
            elif opcao == '0':
                print("\nSaindo do sistema...")
                print("Obrigado por usar o Black Bank!")
                print("Seu atendimento foi registrado e o sistema será fechado. Se precisar de mais assistência, não hesite em entrar em contato com nosso suporte.")
                print("Tenha um ótimo dia e até a próxima!")
                break
            else:
                print("Opção inválida! Tente novamente.")

# Inicializando o menu
if __name__ == "__main__":
    Menu().iniciar()
