# "strip" para cortar espaços indesejados.
# "upper" para deixar tudo em maiúsculo.
frase = str(input("Digite qualquer frase: ")).strip().upper()

# Aqui, "count" conta a quantidade de letras "A" que tem na frase.
qtd = frase.count('A')

# Aqui, "find" acha a primeira letra "A" que tem na frase.
inicio = frase.find('A')

# Aqui, "rfind" acha a primeira letra "A" que tem na frase, porém começando da direita para a esquerda.
fim = frase.rfind('A')

print(f"\nA letra \"A\" aparece {qtd} vezes.")

# A contagem de máquina começa com 0.
# A contagem dos humanos, geralmente, começa com 1.
# Então, somei +1 para cada posição, para ficar de maior entendimento.
print(f"A letra aparece, pela primeira vez, na {inicio + 1}ª posição.")
print(f"A letra aparece, pela última vez, na {fim + 1}ª posição.")
