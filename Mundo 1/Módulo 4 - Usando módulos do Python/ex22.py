"""
    Crie um programa que leia o nome completo de uma pessoa e mostre:
    ▸ O nome com todas as letras maiúsculas
    ▸ O nome com todas minúsculas.
    ▸ Quantas letras ao todo (sem considerar espaços).
    ▸ Quantas letras tem o primeiro nome.
"""

# Pedindo e armazenando o nome.
# O método strip é para cortar espaços indesejados antes e depois do nome.
nome = str(input("Digite o seu nome completo: ")).strip()

# PARTE 1
# O método "upper" transforma todos os caracteres da string mencionada em maiúsculo.
print(f"\nSeu nome todo em maiúsculo é: {nome.upper()}.")

# PARTE 2
# O método "lower" transforma todos os caracteres da string mencionada em minúsculo.
print(f"Seu nome todo em minúsculo é: {nome.lower()}.")

# PARTE 3
# O método "count" conta quantas vezes o caracter mencionado (espaço) aparece na string.
# Armazenei a quantidade na variável "espacos".
espacos = nome.count(' ')

# A função "len" conta o total de caracteres na string passada como argumento (incluindo espaços).
# Subtraí a quantidade de espaços da quantidade total de caracteres. O valor foi armazenado em "qtdLetras".
qtdLetras = len(nome) - espacos
print(f"O nome completo tem {qtdLetras} letras.")

# O método "split" separa tudo que é dividido por espaço na string, e armazena no formato de lista.
dividido = nome.split()

# Peguei o primeiro elemento de dividido (o primeiro nome) e contei a quantidade de caracteres com "len".
print(f"Seu primeiro nome é {dividido[0]}, que tem {len(dividido[0])} letras.")

# Outro método:
# print(f"Seu primeiro nome tem {nome.find(" ")} letras.")
# A posição do primeiro espaço será equivalente à quantidade de caracteres do primeiro nome.
