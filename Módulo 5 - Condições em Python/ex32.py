"""
    Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""

from datetime import date

ano = int(input("Digite o ano que quer analisar (ou digite 0 para analisar o ano atual): "))

# Condição simples: se (if) o valor recebido for 0, executa o bloco definido.
# "date" se refere à data.
# "today" pega a data do dia atual registrado na máquina.
# "year" pega apenas o ano da data retornada.
if ano == 0:
    ano = date.today().year

# Anos bissextos são anos divisíveis por 4.
# Exceto múltiplos de 100 que não são múltiplos de 400.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} NÃO é um ano bissexto.")
