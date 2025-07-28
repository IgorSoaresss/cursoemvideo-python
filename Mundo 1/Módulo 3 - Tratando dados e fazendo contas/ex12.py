"""
    Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

# Recebendo o preço inicial.
pInicial = float(input('Digite o preço do produto a receber o desconto: '))

# Calculando a quantos reais corresponde o desconto de 5%.
desconto = 5/100 * pInicial

# Subtraindo o valor do desconto do preço inicial, obtendo o preço final.
pFinal = pInicial - desconto

# Imprimindo a conclusão.
print(f'Recebendo 5% de desconto, o preço final do produto é de R${pFinal:.2f}.')
