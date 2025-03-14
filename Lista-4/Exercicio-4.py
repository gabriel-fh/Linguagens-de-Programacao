# 4. Inverter a Lista
# Escreva um programa que leia uma lista de palavras e exiba essa lista na ordem
# inversa.

def inverter(lista):
    return lista[::-1]

lista = input("Digite as palavras separadas por espaço: ").split()
print(inverter(lista))