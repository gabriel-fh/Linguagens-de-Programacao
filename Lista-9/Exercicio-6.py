# 6. Tratamento de Exceções
# Crie um programa que solicite ao usuário dois números e tente dividir o primeiro pelo
# segundo. O programa deve capturar exceções como ZeroDivisionError e ValueError
# e exibir mensagens apropriadas.

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Digite um número válido.")
