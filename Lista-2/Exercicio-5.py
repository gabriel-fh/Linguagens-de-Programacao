# 5. Verificação de Triângulo
# Peça ao usuário três números representando os lados de um triângulo. O programa deve
# verificar e informar se os valores formam um triângulo válido (a soma de dois lados deve ser
# sempre maior que o terceiro).

lados = []
for i in range(3):
    lados.append(float(input(f"Digite o {i+1}º lado: ")))

if lados[0] + lados[1] > lados[2] and lados[0] + lados[2] > lados[1] and lados[1] + lados[2] > lados[0]:
    print("Os lados formam um triângulo válido.")
else:
    print("Os lados não formam um triângulo válido.")
