# Importando a biblioteca "pygame".
# Esta biblioteca contém métodos para construir jogos.
import pygame

# Inicializa todos os módulos que foram importados, ou seja, inicializa a biblioteca inteiramente.
pygame.init()

# O módulo "mixer" é responsável por lidar com som e música.
# O submódulo "music" controla a reprodução do som em streaming (lido aos poucos e em tempo real, ao invés de ser carregado de uma só vez).
# A função "load" carrega o arquivo de música que indiquei e deixa pronto para ser usado.
pygame.mixer.music.load('ex21.mp3')

# A função "play" toca a música.
pygame.mixer.music.play()

# O input, aqui, serve para manter o programa rodando enquanto a música toca.
# Sem ele, o programa iniciaria e acabaria no mesmo momento.
# Para encerrar o programa, só apertar [enter], e concluir o input.
input()
