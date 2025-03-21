# 4. Nomes de Alunos e Notas
# Crie uma tupla que armazene o nome de cinco alunos e suas respectivas notas
# (ex: ('Ana', 8.5, 'Carlos', 7.0, 'Beatriz', 9.2, 'Daniel', 6.8, 'Eduarda', 8.0)). Depois, exiba
# apenas os nomes dos alunos e, em seguida, apenas as notas.

alunos = (
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Carlos", "nota": 7.0},
    {"nome": "Beatriz", "nota": 9.2},
    {"nome": "Daniel", "nota": 6.8},
    {"nome": "Eduarda", "nota": 8.0},
)

for aluno in alunos:
    print(f"Nome: {aluno['nome']}, Nota: {aluno['nota']}")
