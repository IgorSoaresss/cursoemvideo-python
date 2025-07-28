"""
    Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

# O método "upper" é para deixar tudo em maiúsculo, servirá para fazer apenas uma comparação.
nome = str(input("Digite o seu nome completo: ")).upper()

# "in", aqui, serve para checar se "SILVA" está presente no nome.
print(f"\nSeu nome tem \"SILVA\"? <- {"SILVA" in nome}")
