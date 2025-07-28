"""
    Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

    Considere
    US$1.00 = R$3.27
"""

# Armazenando em 'real' a quantidade recebida.
real = float(input('Quantos reais você tem na carteira?: '))

# Calculando a quantidade de dólares correspondentes.
dol = real / 3.27

# Informando quantos dólares podem ser comprados.
print(f'Você pode comprar {dol:.2f} dólares.')
