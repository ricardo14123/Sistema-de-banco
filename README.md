# 💲Sistema Bancário Simples em Python💲


Este é um sistema bancário simples desenvolvido em Python, que simula as operações básicas de um banco. O sistema permite a criação de usuários, a criação de contas correntes, a realização de depósitos e saques, e a visualização de extratos. O código utiliza um dicionário para armazenar as informações dos usuários e suas contas correntes, e um sistema básico de autenticação para garantir a segurança das transações.

## Funcionalidades

- **Criar Usuário**: Permite criar um novo usuário fornecendo um CPF e uma senha.
- **Criar Conta Corrente**: Permite criar uma conta corrente associada a um usuário existente, solicitando informações adicionais como nome completo, data de nascimento e endereço.
- **Adicionar Saldo**: Adiciona saldo à conta corrente de um usuário, sem solicitar senha.
- **Realizar Depósito**: Permite ao usuário realizar depósitos na conta corrente. Não é necessário fornecer senha para depósitos.
- **Realizar Saque**: Permite ao usuário realizar saques da conta corrente, com verificações de saldo e limites diários. A senha é solicitada para confirmar a transação.
- **Listar Contas Correntes**: Exibe informações sobre todas as contas correntes cadastradas, incluindo saldo, número de saques e dados pessoais.
- **Exibir Extrato**: Exibe o extrato da conta corrente de um usuário, com detalhes das movimentações realizadas.

## Funcionalidades Adicionais

- **Resetar Transações Diárias**: Reseta o número de saques diários permitidos quando um novo dia começa.
- **Autenticação de Senha**: Verifica a senha fornecida pelo usuário antes de realizar operações sensíveis, como saques e visualização de extratos de outros usuários.

## Estrutura do Código

- **Constantes**: Define limites de saque diário e valores máximos de saque.
- **Variáveis Globais**: Armazena dados sobre usuários e contas correntes.
- **Funções**:
  - `resetar_transacoes_diarias()`: Reseta a quantidade de saques diários.
  - `criar_usuario()`: Cria um novo usuário.
  - `criar_conta_corrente()`: Cria uma nova conta corrente para um usuário existente.
  - `adicionar_saldo()`: Adiciona saldo à conta corrente.
  - `depositar()`: Realiza depósitos na conta corrente.
  - `sacar()`: Realiza saques da conta corrente após autenticação.
  - `exibir_extrato()`: Exibe o extrato da conta corrente.
  - `exibir_extrato_usuario()`: Exibe o extrato de outro usuário após autenticação.
  - `listar_contas()`: Lista todas as contas correntes cadastradas.
  - `exibir_menu()`: Exibe o menu principal e captura a escolha do usuário.
  - `sistema_bancario()`: Função principal que gerencia o sistema bancário.

## Instruções para Execução

1. Clone o repositório para sua máquina local.
2. Execute o script Python usando o comando `python nome_do_arquivo.py`.
3. Siga as instruções no menu para realizar as operações bancárias.

## Dependências

O sistema não requer bibliotecas externas além da biblioteca padrão do Python.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues com sugestões e melhorias.

---
## Conecte-se comigo
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ricardo-ambrosio-7949772bb/) [![Instagram](https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/rii_ambrosio/) [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ricardo14123) [![Gmail](https://img.shields.io/badge/Gmail-333333?style=for-the-badge&logo=gmail&logoColor=red)](mailto:ricardoambrosiodasilva1512@gmail.com)
