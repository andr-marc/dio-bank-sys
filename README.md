# Sistema Bancário
### Desafio do Coding The Future Vivo - Python AI Backend Developer

Este desafio é sugerido no modulo Dominando Python e Suas Estruturas de Dados.

## Objetivo

Implementar 3 operações: depósito, saque e extrato.

### Depósito

Todos os depositos devem ser armazenados em uma variável e exibidos na operação de extrato.

### Saque

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500 por saque. Caso o usuário não tenha salado em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

### Extrato

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.

Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:

```
1500.45 = R$ 1500.45
```

## Segunda parte

Atualizar depósito, saque e extrato para serem feito de uma forma modular, usando funções

### Saque

A função saque deve receber os argumentos apenas por nome.

### Depósito

A função depósito deve receber os argumentos apenas por posição.

### Extrato

A função extrato deve receber os argumentos por posição e nome.
