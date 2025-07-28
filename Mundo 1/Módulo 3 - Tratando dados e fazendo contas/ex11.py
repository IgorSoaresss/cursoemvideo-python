"""
    Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
"""

# Recebendo os valores da largura e altura e armazenando em 'l' e 'h', respectivamente.
l = float(input('Largura da parede em metros: '))
h = float(input('Altura da parede em metros: '))

# Calculando a área e a quantidade de litros de tinta necessária para pintar.
a = l*h
li = a/2

# Imprimindo a conclusão.
print(f'Sua parede tem {a} m².')
print(f'Você precisa de {li} litros de tinta para pintar tudo.')
