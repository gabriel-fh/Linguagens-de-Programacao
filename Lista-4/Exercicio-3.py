# 3. Cálculo da Média de uma Lista
# Crie uma função que receba uma lista de números e retorne a média dos valores.
# No programa principal, peça ao usuário para inserir os números e exiba a média
# utilizando a função criada.

def media(lista):
    return sum(lista) / len(lista)

lista = list(map(float, input("Digite os números separados por espaço: ").split()))
print(f"{media(lista):.2f}")