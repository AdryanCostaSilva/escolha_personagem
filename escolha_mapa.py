import pygame
import sys

# Iniciando tela
pygame.init()

# Iniciando mixer de som
pygame.mixer.init()
som_selecao = pygame.mixer.Sound("selecaosound.mp3")
selecionado = pygame.mixer.Sound('selecionado.mp3')

# Configurando tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("JOGO BÃO")

# Fonte da letra
font2 = pygame.font.Font("ARCADECLASSIC.TTF", 90)
font_p = pygame.font.Font("ARCADECLASSIC.TTF", 17)

# Imagem de fundo da tela
background_imagem = pygame.image.load('background.jpg').convert()
background_imagem = pygame.transform.scale(background_imagem, (largura, altura))

# Defina as CORES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VERMELHO = (108, 34, 34)
AZUL = (0, 0, 255)

# Largura e altura dos botões
botao_largura, botao_altura = 160, 110

# Carregando a foto
bibliotecaI = pygame.image.load('mapas/bibliotecaI.jpg').convert_alpha()
bibliotecaII = pygame.image.load('mapas/bibliotecaII.jpg').convert_alpha()
blocolaranja = pygame.image.load('mapas/bloco laranja.jpg').convert_alpha()
complexoesportivo = pygame.image.load('mapas/complexo esportivo.jpg').convert_alpha()
frentebiblioteca = pygame.image.load('mapas/frente biblioteca.jpg').convert_alpha()
blocoverde = pygame.image.load('mapas/interior bloco verde.jpg').convert_alpha()
museu = pygame.image.load('mapas/museu universitario.jpg').convert_alpha()
aleatorio = pygame.image.load('mapas/aleatorio.jpg')

# Lista dos personagens
mapas = [bibliotecaI, bibliotecaII, blocolaranja, complexoesportivo, frentebiblioteca, blocoverde, museu, aleatorio]

# Classe botão P1 e P2
class Button():
    def __init__(self, x, y, imagem, nome):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x, y)
        self.hovered_p1 = False
        self.hovered_p2 = False
        self.nome = nome

    def draw(self, selected_p1):
        if selected_p1 or self.hovered_p1:
            pygame.draw.rect(tela, WHITE, self.rect.inflate(8, 8), 4)
        else:
            pygame.draw.rect(tela, BLACK, self.rect.inflate(8, 8), 4)
        tela.blit(self.imagem, self.rect.topleft)
        # Renderizando o nome do mapa com borda preta
        self.draw_text_with_border(self.nome, font_p, (128, 0, 0), BLACK, self.rect.left + 5, self.rect.top + 5)

    def draw_text_with_border(self, text, font, color, border_color, x, y):
        text_surface = font.render(text, True, border_color)
        offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for ox, oy in offsets:
            tela.blit(text_surface, (x + ox, y + oy))
        text_surface = font.render(text, True, color)
        tela.blit(text_surface, (x, y))

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    tela.blit(text_surface, text_rect)

# Calculando a coordenada x
espacamento_horizontal = 20
espacamento_vertical = 10
total_largura_botoes = botao_largura * len(mapas) + espacamento_horizontal * (len(mapas) - 1)
x_inicial = (largura - total_largura_botoes) // 2

# Calculando a coordenada x inicial para centralizar os botões horizontalmente na tela
x_inicial = 50

# Definindo a posição y inicial para as duas linhas de botões
y_botoes_primeira_linha = 210
y_botoes_segunda_linha = 330

# Criando botões
botoes = []
for i, mapa in enumerate(mapas):
    personagem_redimensionada = pygame.transform.scale(mapa, (botao_largura, botao_altura))
    if i < 4:
        x = x_inicial + i * (botao_largura + espacamento_horizontal)
        y = y_botoes_primeira_linha + espacamento_vertical
    else:
        x = x_inicial + (i - 4) * (botao_largura + espacamento_horizontal)
        y = y_botoes_segunda_linha + espacamento_vertical
        y += espacamento_vertical
    nome_mapas = ["Biblioteca I", "Biblioteca II", "Bloco Laranja", "Complexo Esportivo", "Frente Biblioteca", "Bloco Verde", "Museu", "Aleatorio"]
    botao = Button(x, y, personagem_redimensionada, nome_mapas[i])
    botoes.append(botao)

selected_index_p1 = 0

# Loop do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Teclas de jogador 1 (P1)
            if event.key == pygame.K_a:
                selected_index_p1 = (selected_index_p1 - 1) % len(botoes)
                som_selecao.play()
            elif event.key == pygame.K_d:
                selected_index_p1 = (selected_index_p1 + 1) % len(botoes)
                som_selecao.play()
            elif event.key == pygame.K_w:
                selected_index_p1 = (selected_index_p1 - 4) % len(botoes)
                som_selecao.play()
            elif event.key == pygame.K_s:
                selected_index_p1 = (selected_index_p1 + 4) % len(botoes)
                som_selecao.play()
            elif event.key == pygame.K_RETURN:
                print("Mapa selecionado:", selected_index_p1)
                selecionado.play()
    
    tela.blit(background_imagem, (0, 0))
    draw_text("SELECIONE", font2, BLACK, largura // 2 + 4, 100)
    draw_text("SELECIONE", font2, VERMELHO, largura // 2, 103)
    for i, botao in enumerate(botoes):
        botao.draw(i == selected_index_p1)
    pygame.display.update()