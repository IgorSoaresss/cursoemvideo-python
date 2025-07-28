"""
Escreva um programa que receba uma temperatura digitada em °C e a converta para °F.
"""

# Recebe a temperatura e armazena em 'c'.
c = float(input('Informe a temperatura em °C: '))

# Calcula o valor em Fahrenheit e armazena em 'f'.
f = 9*c / 5 + 32

# Imprime a conclusão.
print(f'A temperatura de {c}°C corresponde a {f}°F!')
