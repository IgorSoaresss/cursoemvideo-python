"""
    Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

# Recebendo o salário inicial.
salInicial = float(input('Quanto você recebe?: '))

# Calculando a quantos reais corresponde o aumento de 15%.
aumento = 15/100 * salInicial

# Somando o valor do aumento ao salário inicial, obtendo o salário final.
salFinal = salInicial + aumento

# Imprimindo a conclusão.
print(f'Recebendo 15% de aumento, seu salário ficará R${salFinal:.2f}.')
