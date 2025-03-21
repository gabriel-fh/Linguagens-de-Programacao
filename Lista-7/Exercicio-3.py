# 3. Dicionário de Tradução
# Crie um dicionário que contenha algumas palavras em português como chave e
# suas respectivas traduções para inglês como valor. Permita que o usuário digite
# uma palavra em português e retorne sua tradução. Caso a palavra não esteja no
# dicionário, exiba uma mensagem informando que a tradução não foi encontrada.

traducoes = {
    "cachorro": "dog",
    "gato": "cat",
    "pássaro": "bird",
    "peixe": "fish",
    "rato": "rat"
}

palavra = input("Digite uma palavra em português: ").lower()
traducao = traducoes.get(palavra)

if traducao:
    print(f"A tradução de {palavra} é {traducao}.")
else:
    print("Tradução não encontrada.")

