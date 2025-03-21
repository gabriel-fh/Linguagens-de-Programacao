# 5. Classificação de Times de Futebol
# Crie uma tupla contendo os 10 primeiros colocados de um campeonato de
# futebol. Depois, exiba:
# • Os três primeiros colocados.
# • Os últimos três colocados.
# • Os times em ordem alfabética.
# • A posição de um time específico informado pelo usuário.

times = (
    "Flamengo", "Internacional", "Atlético-MG", "São Paulo", "Fluminense",
    "Palmeiras", "Santos", "Grêmio", "Corinthians", "Athletico-PR"
)

print(f"Os três primeiros colocados são: {times[:3]}")
print(f"Os três últimos colocados são: {times[-3:]}")
print(f"Times em ordem alfabética: {sorted(times)}")

time = input("Digite o nome de um time: ")
if time in times:
    print(f"O time {time} está na posição {times.index(time) + 1}.")
else:
    print("Time não encontrado.")