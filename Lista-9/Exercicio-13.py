# 13. Processamento de Arquivos de Texto
# Crie um programa que leia um arquivo chamado dados.txt, conte quantas linhas ele
# possui e exiba o conteúdo na tela.

try:
    with open("dados.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        print(f"Total de linhas: {len(linhas)}")
        for linha in linhas:
            print(linha.strip())
except FileNotFoundError:
    print("O arquivo dados.txt não foi encontrado.")
