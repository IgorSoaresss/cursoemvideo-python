"""
    Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
"""

# Recebendo um inteiro e armazenando em 'num'.
num = int(input('Digite um número inteiro para ver sua tabuada: '))

# Imprimindo a tabuada formatada, alinhando os símbolos de '='.
print('-' * 11)
print(f'{num} x {0:<2} = {num*0}')
print(f'{num} x {1:<2} = {num*1}')
print(f'{num} x {2:<2} = {num*2}')
print(f'{num} x {3:<2} = {num*3}')
print(f'{num} x {4:<2} = {num*4}')
print(f'{num} x {5:<2} = {num*5}')
print(f'{num} x {6:<2} = {num*6}')
print(f'{num} x {7:<2} = {num*7}')
print(f'{num} x {8:<2} = {num*8}')
print(f'{num} x {9:<2} = {num*9}')
print(f'{num} x 10 = {num*10}')
print('-' * 11)
