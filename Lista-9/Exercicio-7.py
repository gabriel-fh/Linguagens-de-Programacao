# 7. Criando uma Classe Carro
# Implemente uma classe Carro com os atributos marca, modelo e ano. A classe deve ter
# um método exibir_detalhes() que imprime essas informações. No programa
# principal, crie dois objetos da classe e exiba seus detalhes.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

carro1 = Carro("Fiat", "Uno", 2010)
carro2 = Carro("Ford", "Focus", 2018)

carro1.exibir_detalhes()
carro2.exibir_detalhes()
