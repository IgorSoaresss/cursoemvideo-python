"""
    Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""

# Importando o método "hypot" da biblioteca "math".
# A biblioteca "math" contém algumas funções matemáticas comuns.
# O método "hypot" calcula o valor da hipotenusa.
from math import hypot

# Pedindo os valores dos catetos.
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))

# O método "hypot" recebe os valores dos catetos e retorna a hipotenusa.
hip = hypot(co, ca)

# Imprimindo a conclusão.
print(f"O valor da hipotenusa é {hip}.")
