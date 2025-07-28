"""
    Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""

# Importando o método "choice" da biblioteca "random".
# A biblioteca "random" contém métodos de sorteio, ordenação, entre outros.
# O método "choice" escolhe um item aleatório de uma lista.
from random import choice

# Solicitando os nomes dos quatro alunos.
a1 = str(input("Primeiro aluno: "))
a2 = str(input("Segundo aluno: "))
a3 = str(input("Terceiro aluno: "))
a4 = str(input("Quarto aluno: "))

# Criando uma lista (com o nome de "lista"), que armazena os nomes dos quatro alunos recebidos.
lista = [a1, a2, a3, a4]

# Sorteando um item da lista (um aluno), e armazenando em "esc".
esc = choice(lista)

# Imprimindo a conclusão.
print(f"O aluno escolhido foi {esc}.")
