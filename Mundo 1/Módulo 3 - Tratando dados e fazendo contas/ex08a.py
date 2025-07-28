"""
    Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

# Pedindo um valor em metros e armazenando em 'm'.
m = float(input('Digite um valor em metros: '))

# Calculando o valor em centímetros e milímetros, e armazenando em suas devidas variáveis.
cm = m*100
mm = cm*10

# Imprimindo a conclusão.
print(f'{m} m corresponde à {cm} cm, ou {mm} mm.')
