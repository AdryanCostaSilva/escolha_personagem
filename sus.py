
import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Quadrado Selecionável')

# Cores
background_color = (0, 0, 0)  # Preto
square_color = (255, 0, 0)  # Vermelho
highlight_color = (0, 255, 0)  # Verde

# Configurações do quadrado
square_size = 50
square_x = screen_width // 2 - square_size // 2
square_y = screen_height // 2 - square_size // 2
square_rect = pygame.Rect(square_x, square_y, square_size, square_size)

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clique com o botão esquerdo do mouse
                if square_rect.collidepoint(event.pos):
                    print("Quadrado selecionado!")
                    square_color = highlight_color  # Mudar a cor do quadrado ao ser selecionado

    # Preencher o fundo
    screen.fill(background_color)

    # Desenhar o quadrado
    pygame.draw.rect(screen, square_color, square_rect)

    # Atualizar a tela
    pygame.display.flip()