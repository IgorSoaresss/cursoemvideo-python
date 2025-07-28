"""
    Escreva um programa que leia um valor em metros e o exiba convertido em todas as unidades de medidas de metro.
"""

# Pedindo um valor em metros e armazenando em 'm'.
m = float(input('Digite um valor em metros: '))

# Imprimindo todas as unidades de medida.
print(f'{m} metros corresponde à:')
print(f'{m/1000} km;')
print(f'{m/100} hm;')
print(f'{m/10} dam;')
print(f'{m*10} dm;')
print(f'{m*100} cm;')
print(f'{m*1000} mm.')
