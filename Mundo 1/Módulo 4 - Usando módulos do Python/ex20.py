"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

# Importando o método "shuffle" da biblioteca "random".
# A biblioteca "random" contém métodos de sorteio, ordenação, entre outros.
# O método "shuffle" embaralha os itens de uma lista.
from random import shuffle

# Solicitando os nomes dos quatro alunos.
a1 = str(input("Primeiro aluno: "))
a2 = str(input("Segundo aluno: "))
a3 = str(input("Terceiro aluno: "))
a4 = str(input("Quarto aluno: "))

# Criando uma lista (com o nome de "lista"), que armazena os nomes dos quatro alunos recebidos.
lista = [a1, a2, a3, a4]

# "shuffle" recebe a lista dos alunos e retorna a mesma lista, porém embaralhada.
shuffle(lista)

# Imprimindo a conclusão.
print("\nA ordem de apresentação será:")
print(f"1. {lista[0]}")
print(f"2. {lista[1]}")
print(f"3. {lista[2]}")
print(f"4. {lista[3]}")
