"""
    Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
    Ex:
    "
        Ana Maria de Souza
        primeiro = Ana
        último = Souza
    "
"""

# "title" serve para deixar a primeira letra de todas as palavras em maiúsculo.
# "split" serve para separar todas as palavras, em forma de lista.
nome = str(input("Digite o seu nome completo: ")).title().split()

# O primeiro nome é o primeiro elemento da lista.
primeiro = nome[0]

# O último nome é o último elemento da lista.
# A posição dele é a quantidade total de elementos na lista, menos 1.
ultimo = nome[len(nome) - 1]

print("\nPrazer em te conhecer!")
print(f"Seu primeiro nome é {primeiro}.")
print(f"Seu último nome é {ultimo}.")
