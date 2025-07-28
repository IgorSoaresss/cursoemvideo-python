"""
    Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

print("Digite três números, um de cada vez.")
n1 = float(input("Primeiro: "))
n2 = float(input("Segundo: "))
n3 = float(input("Terceiro: "))

# Se (if) n1 for maior ou igual a n2 e também for maior ou igual a n3, ele é o maior número.
# Senão, se (elif) n2 for maior ou igual a n1 e também for maior ou igual a n3, ele é o maior número.
# Senão (else), o maior número é o n3.
if n1 >= n2 and n1 >= n3:
    print(f"\nO maior número é {n1}.")
elif n2 >= n1 and n2 >= n3:
    print(f"\nO maior número é {n2}.")
else:
    print(f"\nO maior número é {n3}.")

# Se (if) n1 for menor ou igual a n2 e também for menor ou igual a n3, ele é o menor número.
# Senão, se (elif) n2 for menor ou igual a n1 e também for menor ou igual a n3, ele é o menor número.
# Senão (else), o menor número é o n3.
if n1 <= n2 and n1 <= n3:
    print(f"O menor número é {n1}.")
elif n2 <= n1 and n2 <= n3:
    print(f"O menor número é {n2}.")
else:
    print(f"O menor número é {n3}.")
