# 1. Soma dos Elementos de uma Lista
# Escreva um programa que solicite ao usuário uma lista de números inteiros e
# calcule a soma de todos os elementos da lista.

def soma(lista):
    return sum(lista)

lista = list(map(int, input("Digite os números inteiros separados por espaço: ").split()))
print(soma(lista))