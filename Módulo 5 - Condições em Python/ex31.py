"""
    Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
"""

dist = float(input("Digite a distância da viagem, em km: "))

# Se (if) a distância for menor ou igual a 200, executa o primeiro bloco de comando (cada km vale 0,50).
# Senão (else), executa o segundo bloco (cada km vale 0,45).
if dist <= 200:
    valor = dist * 0.50
else:
    valor = dist * 0.45

print(f"\nA passagem irá custar R${valor:.2f}.")
