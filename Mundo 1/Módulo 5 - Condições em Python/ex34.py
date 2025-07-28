"""
    Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
    Para salários superiores a R$1.250,00, calcule um aumento de 10%.
    Para os inferiores ou iguais, o aumento é de 15%.
"""

sal = float(input("Digite o valor do seu salário: "))

# Se (if) o salário for maior que 1250, executa o primeiro bloco de comando (0.1)
# Se não (else), executa o segundo bloco (0.15)
if sal > 1250:
    aumt = 0.1 * sal
else:
    aumt = 0.15 * sal

final = sal + aumt

print(f"\nSeu salário após o acréscimo do desconto, fica de R${final:.2f}.")
