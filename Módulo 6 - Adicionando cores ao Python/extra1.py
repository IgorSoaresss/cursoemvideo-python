"""
    CORES NO TERMINAL

    Primeiro campo: ESTILO.
    0 - None
    1 - Negrito
    4 - Sublinhado
    7 - Negativo/invertido

    Segundo campo: COR DO TEXTO.
    30 a 37 (padrão: 37 (cinza))

    Terceiro campo: COR DO BACKGROUND.
    40 a 47
"""

# Estilo padrão, texto branco, background vermelho.
print("\033[0;30;41mOlá, mundo!\033[m")
# Ou \033[30;41m

# Estilo sublinhado, texto amarelo, background azul escuro.
print("\033[4;33;44mOlá, mundo!\033[m")

# Estilo em negrito, texto roxo, background amarelo.
print("\033[1;35;43mOlá, mundo!\033[m")

# Estilo padrão, texto branco, background verde.
print("\033[30;42mOlá, mundo!\033[m")
# Ou \033[0;30;41m

# Estilo padrão, texto padrão, background padrão.
print("\033[mOlá, mundo!\033[m")
# Padrão do terminal (fundo preto e texto cinza)

# Estilo invertido, texto branco, background padrão.
print("\033[7;30mOlá, mundo!\033[m")
# O estilo 7 troca as cores do backgound e do texto
# Texto está em 30 (branco), mas como inverteu, será a cor do background

# Também funciona com variáveis
a = "Olá"
b = "mundo"
print(f"\033[32m{a}\033[m, \033[31m{b}\033[m!")
