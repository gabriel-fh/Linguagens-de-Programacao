# 5. Operações Bancárias com Tratamento de Erros
# Crie um programa que simule um sistema bancário simples. O saldo inicial do
# usuário é de R$ 1000,00. O programa deve permitir que o usuário insira um valor
# para saque e, caso o valor solicitado seja maior que o saldo disponível, uma
# exceção personalizada deve ser lançada informando que o saldo é insuficiente.

class SaldoError(Exception):

    pass


def realizar_saque(saldo, valor_saque):
    if valor_saque > saldo:
        raise SaldoError("Erro: Saldo insuficiente para realizar o saque.")
    if valor_saque <= 0:
        raise SaldoError("Erro: O valor do saque deve ser positivo.")
    saldo -= valor_saque
    return saldo


saldo = 1000.00

while True:
    try:
        valor_saque = float(
            input(f"Digite o valor para saque (Saldo disponível: R$ {saldo}): R$ ")
        )

        saldo = realizar_saque(saldo, valor_saque)

        print(f"Saque realizado com sucesso! Novo saldo: R$ {saldo}")
        break
    except SaldoError as e:
        print(e) 
    except ValueError:
        print("Erro: Digite um valor válido para o saque.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
