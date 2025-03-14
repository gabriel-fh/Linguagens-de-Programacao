# 3. Remover Duplicatas
# Escreva um programa que leia uma lista de números e remova os valores
# duplicados, mantendo a ordem original.

def remove_duplicatas(lista):
    return list(dict.fromkeys(lista))

lista = list(map(int, input("Digite os números inteiros separados por espaço: ").split()))
print(remove_duplicatas(lista))