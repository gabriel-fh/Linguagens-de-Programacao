# 11. Iteradores
# Crie uma classe Contador que implemente um iterador que conta de 1 até n. No
# programa principal, percorra os valores utilizando for.

class Contador:
    def __init__(self, n):
        self.n = n
        self.atual = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual > self.n:
            raise StopIteration
        else:
            valor = self.atual
            self.atual += 1
            return valor

contador = Contador(5)
for numero in contador:
    print(numero)
