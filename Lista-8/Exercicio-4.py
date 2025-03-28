# 4. Acesso a Elementos de uma Lista
# Crie uma lista com cinco números e permita que o usuário informe um índice para
# acessar um valor da lista. Utilize tratamento de exceções para evitar erros caso o
# usuário digite um índice inválido.
lista = [10, 20, 30, 40, 50]

while True:
    indice = input("Digite um índice (0 a 4) para acessar um valor da lista: ")
    try:
        indice = int(indice)
        valor = lista[indice]
        print(f"O valor no índice {indice} é: {valor}")
        break
    except IndexError:
        print("Erro: Índice inválido. Por favor, digite um índice entre 0 e 4.")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
