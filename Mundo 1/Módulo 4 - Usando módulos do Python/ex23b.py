"""
    Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
    Ex:
    "
        Digite um número: 0834
        unidade: 4
        dezena: 3
        centena: 8
        milhar: 0
    "
    Receba o número como inteiro.
"""

# Armazenando o número como string para poder pegar cada caracter com o índice.
num = int(input("Digite um número entre 0 e 9999: "))

# Realizando divisões inteiras para resultar só no algarismo a ser armazenado.
# O resto das mesmas divisões serão incluídos em divisões inteiras subsequentes.
# Ex: 9345 // 1000 -> 9
# 9345 % 1000 -> 345
# 345 // 100 -> 3
# Etc...
m = num // 1000
c = (num % 1000) // 100
d = ((num % 1000) % 100) // 10
u = ((num % 1000) % 100) % 10

print(f"\nUnidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")
