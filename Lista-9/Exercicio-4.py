# 4. Processamento de Strings
# Peça ao usuário para digitar uma frase e implemente funções para:
# • Contar quantas vezes cada vogal aparece na frase.
# • Exibir a frase ao contrário.
# • Substituir todos os espaços por -.

frase = input("Digite uma frase: ")

vogais = 'aeiou'
contagem_vogais = {vogal: frase.lower().count(vogal) for vogal in vogais}
print("Contagem das vogais:", contagem_vogais)

frase_reversa = frase[::-1]
print("Frase ao contrário:", frase_reversa)

frase_substituida = frase.replace(' ', '-')
print("Frase com espaços substituídos por '-':", frase_substituida)
