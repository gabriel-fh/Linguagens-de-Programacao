# 1. Cadastro de Alunos
# Crie um programa que permita cadastrar alunos em um dicionário. O programa
# deve solicitar o nome e a nota do aluno e armazená-los como chave e valor no
# dicionário. Após a inserção de pelo menos 3 alunos, exiba a lista de alunos e suas
# respectivas notas.

alunos = {}

while len(alunos) < 3:
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota

for nome, nota in alunos.items():
    print(f"Nome: {nome}, Nota: {nota}")