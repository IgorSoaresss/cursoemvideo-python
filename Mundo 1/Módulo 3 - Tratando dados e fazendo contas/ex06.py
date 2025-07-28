"""
    Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

# Recebe um inteiro e armazena em 'num'.
num = int(input('Digite um número: '))

# Imprimindo no terminal o dobro, o triplo, e a raiz quadrada.
print('Dobro:', num*2)
print('Triplo:', num*3)

print('Raiz quadrada:', pow(num, (1/2)))
# print('Raiz quadrada:', num**(1/2)) - FORMA ALTERNATIVA
