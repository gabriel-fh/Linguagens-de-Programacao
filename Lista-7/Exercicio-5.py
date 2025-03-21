# 5. Catálogo de Produtos
# Crie um dicionário onde as chaves representem códigos de produtos e os valores
# sejam tuplas contendo o nome do produto e seu preço. Permita que o usuário
# informe um código para buscar o nome e o preço do produto correspondente.

produtos = {
    1: ('Notebook', 2500.00),
    2: ('Smartphone', 1500.00),
    3: ('Tablet', 800.00),
    4: ('Smartwatch', 500.00),
    5: ('Fone de Ouvido', 150.00)
}

codigo = int(input("Digite o código do produto: "))
if codigo in produtos:
    produto = produtos[codigo]
    print(f"Nome: {produto[0]}")
    print(f"Preço: R${produto[1]:.2f}")
else:
    print("Produto não encontrado.")

