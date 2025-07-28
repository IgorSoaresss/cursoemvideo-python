"""
    Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

# Armazena os valores pedidos em 'dia' e 'rodou'.
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

# Calcula o preço total.
preco = (dias*60) + (km*0.15)

# Imprime a conclusão.
print(f'O total a pagar é de R${preco:.2f}.')
