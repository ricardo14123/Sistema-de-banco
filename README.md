# Sistema Bancário Simples

Este é um sistema bancário simples em Python que permite criar usuários, contas correntes, realizar depósitos, saques e listar contas, além de exibir extratos. O sistema demonstra conceitos básicos de programação orientada a objetos e abstração em Python.

## Funcionalidades

- **Criar Usuário:** Permite criar um novo usuário com CPF, nome, data de nascimento e endereço.
- **Criar Conta Corrente:** Cria uma nova conta corrente para um usuário existente.
- **Adicionar Saldo:** Permite adicionar um valor a uma conta corrente.
- **Sacar Dinheiro:** Permite retirar um valor da conta corrente, se a senha e o saldo permitirem.
- **Listar Contas:** Exibe uma lista de todas as contas correntes criadas.
- **Exibir Extrato:** Mostra o extrato de uma conta corrente, incluindo transações realizadas.

## Requisitos

- Python 3.x

## Instalação

1. Clone este repositório ou baixe o arquivo Python.
2. Certifique-se de ter o Python 3.x instalado em seu sistema.
3. Execute o script com o comando:

    ```bash
    python nome_do_arquivo.py
    ```

## Como Usar

1. Ao iniciar o script, um menu será exibido com as seguintes opções:
   - **Criar Usuário**
   - **Criar Conta Corrente**
   - **Adicionar Saldo**
   - **Sacar Dinheiro**
   - **Listar Contas**
   - **Exibir Extrato**
   - **Sair**

2. Escolha uma opção digitando o número correspondente e siga as instruções fornecidas pelo menu.

## Estrutura do Código

### Classes

- **Cliente**
  - **Atributos:**
    - `endereco`: Endereço do cliente.
    - `contas`: Lista de contas do cliente.
  - **Métodos:**
    - `adicionar_conta(conta)`: Adiciona uma conta à lista de contas do cliente.

- **PessoaFisica (herda de Cliente)**
  - **Atributos:**
    - `nome`: Nome do cliente.
    - `data_nascimento`: Data de nascimento do cliente.
    - `cpf`: CPF do cliente.

- **Historico**
  - **Atributos:**
    - `_transacoes`: Lista de transações.
  - **Métodos:**
    - `adicionar_transacao(transacao)`: Adiciona uma transação ao histórico.

- **Transacao (classe abstrata)**
  - **Métodos Abstratos:**
    - `valor`: Retorna o valor da transação.
    - `registrar(conta, senha)`: Registra a transação na conta.

- **Saque (herda de Transacao)**
  - **Atributos:**
    - `_valor`: Valor do saque.
  - **Métodos:**
    - `valor`: Retorna o valor do saque.
    - `registrar(conta, senha)`: Registra o saque na conta.

- **Deposito (herda de Transacao)**
  - **Atributos:**
    - `_valor`: Valor do depósito.
  - **Métodos:**
    - `valor`: Retorna o valor do depósito.
    - `registrar(conta, senha=None)`: Registra o depósito na conta.

- **Conta**
  - **Atributos:**
    - `_saldo`: Saldo da conta.
    - `_numero`: Número da conta (gerado aleatoriamente).
    - `_agencia`: Agência da conta.
    - `_cliente`: Cliente da conta.
    - `_historico`: Histórico de transações.
    - `_senha`: Senha da conta.
  - **Métodos:**
    - `sacar(valor, senha)`: Realiza um saque da conta.
    - `depositar(valor)`: Realiza um depósito na conta.

- **ContaCorrente (herda de Conta)**
  - **Atributos:**
    - `limite`: Limite de saque da conta corrente.
    - `limite_saques`: Limite de saques permitido.
  - **Métodos:**
    - `sacar(valor, senha)`: Realiza um saque, respeitando o limite e o número máximo de saques.
    - `__str__()`: Retorna uma string formatada com as informações da conta corrente.

- **Menu**
  - **Atributos:**
    - `clientes`: Dicionário de clientes (CPF como chave).
    - `contas`: Dicionário de contas (número da conta como chave).
  - **Métodos:**
    - `exibir_menu()`: Exibe o menu principal.
    - `criar_usuario()`: Cria um novo usuário.
    - `criar_conta_corrente()`: Cria uma nova conta corrente.
    - `adicionar_saldo()`: Adiciona saldo a uma conta.
    - `sacar_dinheiro()`: Realiza um saque.
    - `listar_contas()`: Lista todas as contas.
    - `exibir_extrato()`: Exibe o extrato de uma conta.
    - `iniciar()`: Inicia o menu e o loop de operação do sistema.

## Exemplo de Uso

1. **Criar um novo usuário**:
   - Selecione a opção "Criar Usuário" e forneça as informações solicitadas.

2. **Criar uma conta corrente**:
   - Selecione a opção "Criar Conta Corrente" e forneça o CPF do cliente e a senha para a nova conta.

3. **Adicionar saldo**:
   - Selecione a opção "Adicionar Saldo" e informe o número da conta e o valor a ser depositado.

4. **Sacar dinheiro**:
   - Selecione a opção "Sacar Dinheiro" e informe o número da conta, o valor a ser sacado e a senha da conta.

5. **Listar todas as contas**:
   - Selecione a opção "Listar Contas" para visualizar todas as contas correntes.

6. **Exibir extrato da conta**:
   - Selecione a opção "Exibir Extrato" e forneça o número da conta e a senha para visualizar o extrato.

## Contribuições

Contribuições são bem-vindas! Por favor, faça um fork do repositório e envie um pull request com suas melhorias ou correções.



## Conecte-se comigo
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ricardo-ambrosio-7949772bb/) [![Instagram](https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/rii_ambrosio/) [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ricardo14123) [![Gmail](https://img.shields.io/badge/Gmail-333333?style=for-the-badge&logo=gmail&logoColor=red)](mailto:ricardoambrosiodasilva1512@gmail.com)
