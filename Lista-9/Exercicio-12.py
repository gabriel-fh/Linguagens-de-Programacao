# 12. Closures
# Implemente uma função multiplicador(fator) que recebe um número fator e
# retorna uma função que multiplica qualquer número por esse fator. Teste a função no
# programa principal.

def multiplicador(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar

dobro = multiplicador(2)
triplo = multiplicador(3)

print(dobro(5))  
print(triplo(5))  
