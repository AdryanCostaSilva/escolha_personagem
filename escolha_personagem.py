import pygame
import sys

# Iniciando tela
pygame.init()

# Configurando tela
largura = 800
altura = 500
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("JOGO BÃO")

# Imagem de fundo da tela
background_imagem = pygame.image.load('puc.jpg')

# Carregando e redimensionando as imagens dos botões
# Tamanho desejado para os botões
botao_largura, botao_altura = 150, 150 
personagem_adryan = pygame.image.load('adryan.jpg').convert_alpha()
personagem_adryan = pygame.transform.scale(personagem_adryan, (botao_largura, botao_altura))

personagem_gustavo = pygame.image.load('gustavo.png').convert_alpha()
personagem_gustavo = pygame.transform.scale(personagem_gustavo, (botao_largura, botao_altura))

personagem_kelvin = pygame.image.load('kelvin.jpg').convert_alpha()
personagem_kelvin = pygame.transform.scale(personagem_kelvin, (botao_largura, botao_altura))

# Classe do botão
class Button():
    def __init__(self, x, y, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x, y)
    def draw(self):
        # Desenhando borda preta
        pygame.draw.rect(tela, (0, 0, 0), self.rect.inflate(4, 4))
        # Desenhando o botão na tela
        tela.blit(self.imagem, (self.rect.x, self.rect.y))
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

# Definindo as dimensões dos botões
botao_largura, botao_altura = 150, 150
espaco_entre_botoes = 50

# Calcula a largura total ocupada pelos botões e espaçamentos
total_largura_botoes = 4 * botao_largura + 3 * espaco_entre_botoes

# Posição inicial (x)
x_inicial = (largura - total_largura_botoes) / 2

# Posição inicial (y)
y_pos = (altura - botao_altura) / 2

# Criando instâncias dos botões
personagem_adryan = Button(x_inicial, y_pos, personagem_adryan)
personagem_gustavo = Button(x_inicial + (botao_largura + espaco_entre_botoes), y_pos, personagem_gustavo)
personagem_kelvin = Button(x_inicial + 2 * (botao_largura + espaco_entre_botoes), y_pos, personagem_kelvin)
# Adicione aqui a imagem e a posição para o botão do personagem Caio, caso tenha uma
# personagem_caio = Button(x_inicial + 3 * (botao_largura + espaco_entre_botoes), y_pos, personagem_caio_imagem)

# Loop do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Clicando com botão esquerdo do mouse
            if event.button == 1: 
                if personagem_adryan.is_clicked(event.pos):
                    print("Adryan selecionado!")
                elif personagem_gustavo.is_clicked(event.pos):
                    print("Gustavo selecionado!")
                elif personagem_kelvin.is_clicked(event.pos):
                    print("Kelvin selecionado!")
                # elif personagem_caio.is_clicked(event.pos):
                #     print("Caio selecionado!")

    # Desenhando a imagem de fundo
    tela.blit(background_imagem, (0, 0))

    # Desenhando os botões
    personagem_adryan.draw()
    personagem_gustavo.draw()
    personagem_kelvin.draw()
    # personagem_caio.draw()

    # Atualizando a tela
    pygame.display.flip()
