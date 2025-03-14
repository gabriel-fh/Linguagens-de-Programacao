# 5. Contar Ocorrências de um Elemento
# Escreva um programa que peça ao usuário para inserir uma lista de números e um
# número específico. O programa deve contar quantas vezes esse número aparece
# na lista.

def contar(lista, n):
    return lista.count(n)

lista = list(map(int, input("Digite os números inteiros separados por espaço: ").split()))
n = int(input("Digite o número que deseja contar: "))
print(contar(lista, n))