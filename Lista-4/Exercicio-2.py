# 2. Encontrar o Maior e o Menor Número
# Escreva um programa que leia uma lista de números digitados pelo usuário e
# determine o maior e o menor número presentes na lista.

def maior_menor(lista):
    return max(lista), min(lista)

lista = list(map(int, input("Digite os números inteiros separados por espaço: ").split()))
maior, menor = maior_menor(lista)
print(f"Menor: {menor}\Maior: {maior}")