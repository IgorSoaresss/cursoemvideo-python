"""
    Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

# Importando os métodos necessários da biblioteca "math".
# O método "sin" calcula o seno do ângulo.
# O método "cos" calcula o cosseno do ângulo.
# O método "tan" calcula a tangente do ângulo.
# O método "radians" converte o valor recebido para radianos, garantindo que os resultados sejam corretos.
from math import sin, cos, tan, radians

# Pedindo o valor do ângulo.
ang = float(input("Digite o valor do ângulo: "))

# Calculando os itens pedidos.
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))

# Imprimindo a conclusão.
print(f"Seno: {seno:.2f}")
print(f"Cosseno: {coss:.2f}")
print(f"Tangente: {tang:.2f}")
