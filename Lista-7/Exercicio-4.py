# 4. Estatísticas de um Texto
# Peça ao usuário para inserir uma frase. Utilize um dicionário para armazenar a
# contagem de palavras, ou seja, a chave será a palavra e o valor será o número de
# vezes que ela aparece na frase. Exiba o dicionário ao final.

frase = input("Digite uma frase: ").lower()
palavras = frase.split()
contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)