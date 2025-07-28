"""
    Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
    A multa vai custar R$7,00 por cada Km acima do limite.
"""

vel = float(input("Digite a velocidade do carro, em km/h: "))

# Se (if) a velocidade recebida for MAIOR que 80, executa o primeiro bloco de comando (terá multa).
# Senão (else), executa o segundo bloco (não terá multa).
if vel > 80:
    # Subtrai 80, resultando na quantidade de KM que passaram do limite.
    # O resultado multiplica por 7, assim cada KM acima do limite corresponde à 7 reais.
    multa = (vel - 80) * 7

    print(f"\nVocê passou do limite de 80 km/h! Você será multado em R${multa:.2f}.")
else:
    print("\nEstá dentro do limite de velocidade. Obrigado!")
