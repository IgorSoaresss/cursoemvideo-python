"""
    Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
"""

# Recebe um valor e armazena na variável 'a'.
a = input('Digite algo: ')

# Uma série de funções do Python para checar as perguntas escritas.
print(f'O tipo primitivo desse valor é {type(a)}')
print(f'Só tem espaços? - {a.isspace()}')
print(f'É um número? - {a.isnumeric()}')
print(f'É alfabético? - {a.isalpha()}')
print(f'É alfanumérico? - {a.isalnum()}')
print(f'Está em maiúsculas? - {a.isupper()}')
print(f'Está em minúsculas? - {a.islower()}')
print(f'Está capitalizada? - {a.istitle()}')
