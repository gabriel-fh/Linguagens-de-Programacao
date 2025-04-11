# 14. Processamento de Arquivos Binários
# Escreva um programa que crie um arquivo binário dados.bin e grave uma lista de
# números inteiros nele. Em seguida, abra o arquivo e exiba os números armazenados.

import struct

numeros = [1, 2, 3, 4, 5]
with open("dados.bin", "wb") as arquivo_bin:
    for numero in numeros:
        arquivo_bin.write(struct.pack("i", numero))

with open("dados.bin", "rb") as arquivo_bin:
    while True:
        dados = arquivo_bin.read(4)
        if not dados:
            break
        numero = struct.unpack("i", dados)[0]
        print(numero)
