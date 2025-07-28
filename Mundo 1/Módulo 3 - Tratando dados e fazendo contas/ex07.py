"""
    Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""

# Recebe as notas 1 e 2 como floats e armazena em 'n1' e 'n2', respectivamente.
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

# Calculando a média e armazenando em 'm'.
m = (n1+n2)/2

# Imprimindo a média.
print(f'Sua média é {m:.2f}.')
