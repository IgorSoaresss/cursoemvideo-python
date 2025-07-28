"""
    Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
    O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint
from time import sleep

# "randint", aqui, sorteia um inteiro entre 0 e 5.
num = randint(0, 5)

print("\n" + "-=-" * 18)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar!")
print("-=-" * 18)

palp = int(input("Em que número eu pensei?: "))

print("Que rufem os tambores...")
sleep(2) # O sistema aguardará 2 segundos antes de executar as próximas linhas.

# Se (if) o palpite for igual ao número sorteado, executa o primeiro print.
# Senão (else), executa o segundo print.
if palp == num:
    print("Parabéns! Você acertou!")
else:
    print(f"Você errou! Eu pensei no número {num}, e não no {palp}.")
