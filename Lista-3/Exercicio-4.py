# 4. Números Ímpares em um Intervalo
# Peça ao usuário dois números inteiros, representando um intervalo A,B. O programa deve
# exibir todos os números ímpares dentro desse intervalo (inclusive os limites, se forem
# ímpares).

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

for i in range(a, b + 1):
    if i % 2 != 0:
        print(i)
