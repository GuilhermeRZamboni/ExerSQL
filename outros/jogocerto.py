#pip install pygame
import pygame
import random
import time

# Configurações inciais
pygame.init()
pygame.display.set_caption("Jogo da cobrinha")
LARGURA, ALTURA = 1200, 800
TELA = pygame.display.set_mode((LARGURA,ALTURA))
relogio = pygame.time.Clock()

#Cores RGB (R, G, B)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = [0, 0, 255]
roxo_claro = [255, 0, 255]
#parametros do jogo
tamanho_quadrado = 50
velocidade_jogo = 5
imagem_maca = pygame.image.load(".png")
imagem_maca = pygame.transform.scale(imagem_maca, (tamanho_quadrado, tamanho_quadrado))
VERDE = [[0, 128, 0], [0, 255, 0]]
def gerar_comida():
    x = random.randrange(0, LARGURA - tamanho_quadrado, tamanho_quadrado)
    y = random.randrange(0, ALTURA - tamanho_quadrado, tamanho_quadrado)
    return x, y

def desenhar_comida(x, y):
    TELA.blit(imagem_maca, (x, y))
def desenhar_cobra(corpo):
    for parte in corpo:
        pygame.draw.rect(TELA, AZUL, (parte[0], parte[1], tamanho_quadrado, tamanho_quadrado))

def mostrar_pontos(pontos):
    fonte = pygame.font.SysFont("Arial Title", 30)
    texto = fonte.render(f"Pontos: {pontos}", True, roxo_claro)
    TELA.blit(texto, (10, 10))

def jogar():
    x = LARGURA // 2
    y = ALTURA // 2
    velocidade_x = 0
    velocidade_y = 0
    corpo_cobra = []
    tamanho_cobra = 1    
    comida_x, comida_y = gerar_comida()

    fim_jogo = False

    while not fim_jogo:
        TELA.fill(PRETO)
        for y1 in range(0, ALTURA, tamanho_quadrado):
            for x1 in range(0, LARGURA, tamanho_quadrado):
                if (x1 + y1) // tamanho_quadrado % 2 == 0:
                    TELA.fill(VERDE[1], (x1, y1, tamanho_quadrado, tamanho_quadrado))
                else:
                    TELA.fill(VERDE[0], (x1, y1, tamanho_quadrado, tamanho_quadrado))

        #Verificar eventos (teclas, fechar janela e etc..)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w:
                    velocidade_x, velocidade_y = 0, -tamanho_quadrado
                elif evento.key == pygame.K_s:
                    velocidade_x, velocidade_y = 0, tamanho_quadrado
                elif evento.key == pygame.K_d:
                    velocidade_x, velocidade_y = tamanho_quadrado, 0
                elif evento.key == pygame.K_a:
                    velocidade_x, velocidade_y = -tamanho_quadrado, 0
               
        x += velocidade_x
        y += velocidade_y

        corpo_cobra.append([x,y])
        if len(corpo_cobra) > tamanho_cobra:
            del corpo_cobra[0]
        if x < 0 or x >= LARGURA or y < 0 or y >= ALTURA:
            fim_jogo = True
        if [x, y] in corpo_cobra[:-1]:
            fim_jogo = True
        
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()
        desenhar_comida(comida_x, comida_y)
        desenhar_cobra(corpo_cobra)
        mostrar_pontos(tamanho_cobra - 1)

        pygame.display.update()
        relogio.tick(velocidade_jogo)


#Chamar a função do jogo
jogar()