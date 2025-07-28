"""
    Faça um programa que leia um número de 1000 a 9999 e mostre na tela cada um dos dígitos separados.
    Ex:
    "
        Digite um número: 1834
        unidade: 4
        dezena: 3
        centena: 8
        milhar: 1
    "
"""

# Armazenando o número primeiro como int, para evitar que o usuário digite um valor de outro tipo.
num = int(input("Digite um número entre 0 e 9999: "))

# Convertendo em string para poder pegar cada caracter com o índice e cortando espaços indesejados.
num = str(num).strip()

print(f"\nUnidade: {num[3]}")
print(f"Dezena: {num[2]}")
print(f"Centena: {num[1]}")
print(f"Milhar: {num[0]}")
