import pygame
import sys

#iniciando tela
pygame.init()


#configurando tela
largura = 800
altura = 500
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("JOGO BÃO")


#imagem de fundo da tela
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


#classe do botão
class Button():
    def __init__(self, x, y, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x, y)
    def draw(self):
        #Desenhando borda preta
        pygame.draw.rect(tela, (0, 0, 0), self.rect.inflate(4, 4))
        #desenhando o botão na tela
        tela.blit(self.imagem, (self.rect.x, self.rect.y))
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


# Calculando posições para os botões
espaco_entre_botoes = 50
total_largura_botoes = 2 * botao_largura + espaco_entre_botoes
x_inicial = (largura - total_largura_botoes) / 2
y_pos = (altura - botao_altura) / 2


# Calculando a posição x para centralizar a nova imagem
personagem_kelvin_x = (largura - botao_largura) // 2

# Calculando a posição y para a nova imagem abaixo das imagens existentes
personagem_kelvin_y = y_pos + botao_altura + 50

#criando instancias do botão
personagem_adryan = Button(x_inicial, y_pos, personagem_adryan)
personagem_gustavo = Button(x_inicial + botao_largura + espaco_entre_botoes, y_pos, personagem_gustavo)
personagem_kelvin = Button(personagem_kelvin_x, personagem_kelvin_y, personagem_kelvin)


#loop do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Clicando com botão esquerdo do mouse
            if event.button == 1: 
                if personagem_adryan.is_clicked(event.pos):
                    print(f"Adryan selecionado!")
                elif personagem_gustavo.is_clicked(event.pos):
                    print(f"Gustavo selecionado!")
                elif personagem_kelvin.is_clicked(event.pos):
                    print(f"Kelvin selecionado!")
    pygame.display.update()

    tela.blit(background_imagem, (0, 0))
    personagem_adryan.draw()
    personagem_gustavo.draw()
    personagem_kelvin.draw()
    pygame.display.flip()
