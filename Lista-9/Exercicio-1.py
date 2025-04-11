# 1. Importação de Módulos
# Escreva um programa que importe os módulos math e random e use suas funções para:
# • Calcular a raiz quadrada de um número informado pelo usuário.
# • Gerar um número aleatório entre 1 e 100.
import math
import random

numero = float(input("Digite um número: "))
raiz_quadrada = math.sqrt(numero)
print(f"A raiz quadrada de {numero} é {raiz_quadrada}")

numero_aleatorio = random.randint(1, 100)
print(f"O número aleatório gerado é {numero_aleatorio}")
