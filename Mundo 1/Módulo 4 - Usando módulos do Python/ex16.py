"""
    Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
    Ex: Digite um número: 6.127
    O número 6.127 tem a parte inteira 6.
"""

# Importando o método "trunc" da biblioteca "math".
# A biblioteca "math" contém algumas funções matemáticas comuns.
# O método "trunc" corta a parte decimal do número, e retorna apenas a parte inteira.
from math import trunc

# Pedindo um número e armazenando na variável "num".
num = float(input("Digite um número: "))

# "trunc" recebe o número e retorna ele truncado (sem a parte decimal).
truncado = trunc(num)

# Aplicando o método e imprimindo a conclusão.
print(f"O número {num} tem a parte Inteira {truncado}.")
