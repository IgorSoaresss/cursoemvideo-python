"""
    Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

num = int(input("Digite um número inteiro qualquer: "))

# Todo número par é divisível por 2 (tem resto 0).
# Se (if) o resto da divisão do número por 2 for 0, executa o primeiro bloco (é par).
# Senão (else), executa o segundo bloco (é ímpar).
if num % 2 == 0:
    print(f"O número {num} é PAR.")
else:
    print(f"O número {num} é ÍMPAR.")
