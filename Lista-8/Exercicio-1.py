# 1. Divisão Segura
# Crie um programa que solicite ao usuário dois números e realize a divisão do
# primeiro pelo segundo. Utilize tratamento de exceções para evitar erros de
# divisão por zero e erros de entrada inválida (como caracteres não numéricos).

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

try:
    num1 = float(num1)
    num2 = float(num2)
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
