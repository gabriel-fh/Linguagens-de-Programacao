# 5. Manipulação de Listas e Strings
# Solicite ao usuário que insira uma lista de palavras separadas por espaço. Em seguida,
# exiba:
# • A lista ordenada alfabeticamente.
# • O número total de palavras.
# • As palavras convertidas para maiúsculas.

entrada = input("Digite uma lista de palavras separadas por espaço: ")
lista_palavras = entrada.split()

lista_palavras.sort()
print("Lista ordenada alfabeticamente:", lista_palavras)

print("Número total de palavras:", len(lista_palavras))

palavras_maiusculas = [palavra.upper() for palavra in lista_palavras]
print("Palavras em maiúsculas:", palavras_maiusculas)
