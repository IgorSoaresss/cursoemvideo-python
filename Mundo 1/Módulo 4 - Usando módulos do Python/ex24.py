"""
    Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""

# Armazenando o nome da cidade.
# O método "strip" é para cortar espaços indesejados.
# O método "upper" é para transformar tudo em maiúsculo. Servirá para fazer apenas uma comparação.
cid = str(input("Digite o nome da sua cidade: ")).strip().upper()

# Checando se os primeiros 5 caracteres de "cid" são igual a "SANTO".
# Se forem, imprimirá "True".
# Se não forem, imprimirá "False".
print(f"\n{cid[:5] == "SANTO"}.")
