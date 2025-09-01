import pygame
import random
import os
import sys

# Definição de skins (cores)
SKINS = [
    ("Azul", (0, 0, 255)),
    ("Verde", (0, 255, 0)),
    ("Vermelho", (255, 0, 0)),
    ("Amarelo", (255, 255, 0)),
    ("Roxo", (128, 0, 255)),
    ("Laranja", (255, 140, 0)),
    ("Ciano", (0, 255, 255)),
    ("Rosa", (255, 0, 128)),
]

def escolher_dificuldade():
    print("Escolha a dificuldade:")
    print("1 - Fácil (Mapa pequeno, velocidade baixa)")
    print("2 - Médio (Mapa médio, velocidade média)")
    print("3 - Difícil (Mapa grande, velocidade alta)")
    while True:
        escolha = input("Digite 1, 2 ou 3: ")
        if escolha == "1":
            return 800, 600, 7
        elif escolha == "2":
            return 1200, 900, 12
        elif escolha == "3":
            return 1600, 1000, 18
        else:
            print("Opção inválida. Tente novamente.")

def escolher_skin(jogador):
    print(f"\nEscolha a skin do Jogador {jogador}:")
    for i, (nome, cor) in enumerate(SKINS):
        print(f"{i+1} - {nome}")
    while True:
        escolha = input(f"Digite o número da skin para o Jogador {jogador}: ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(SKINS):
            return SKINS[int(escolha)-1][1]
        else:
            print("Opção inválida. Tente novamente.")

# Configurações iniciais
LARGURA, ALTURA, velocidade_jogo = escolher_dificuldade()
tamanho_quadrado = 40

# Escolha de skins
cor_cobra1 = escolher_skin(1)
cor_cobra2 = escolher_skin(2)

pygame.init()
pygame.display.set_caption("Jogo da cobrinha 2 jogadores")
TELA = pygame.display.set_mode((LARGURA, ALTURA))
relogio = pygame.time.Clock()

# Cores clássicas
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
ROXO = (128, 0, 255)

# Sons
pygame.mixer.init()
EAT_SOUND = None
if os.path.exists("eat.wav"):
    EAT_SOUND = pygame.mixer.Sound("eat.wav")

def tocar_som():
    if EAT_SOUND:
        EAT_SOUND.play()

def gerar_comida(ocupados):
    # Gera comida fora do corpo das cobras
    while True:
        x = random.randrange(0, LARGURA, tamanho_quadrado)
        y = random.randrange(0, ALTURA, tamanho_quadrado)
        if (x, y) not in ocupados:
            return (x, y)

def desenhar_comida(pos, cor):
    centro = (pos[0] + tamanho_quadrado // 2, pos[1] + tamanho_quadrado // 2)
    pygame.draw.circle(TELA, cor, centro, tamanho_quadrado // 2 - 4)

def desenhar_cobra(corpo, cor):
    for parte in corpo:
        pygame.draw.rect(TELA, cor, (parte[0], parte[1], tamanho_quadrado, tamanho_quadrado), border_radius=8)

def mostrar_pontos(pontos1, pontos2, highscore1, highscore2):
    fonte = pygame.font.SysFont("Arial", 32, bold=True)
    texto = fonte.render(f"P1: {pontos1}    P2: {pontos2}    Recorde P1: {highscore1}    Recorde P2: {highscore2}", True, BRANCO)
    rect = texto.get_rect(center=(LARGURA // 2, 30))
    TELA.blit(texto, rect)

def mostrar_texto(texto, tamanho, cor, y):
    fonte = pygame.font.SysFont("Arial", tamanho, bold=True)
    txt = fonte.render(texto, True, cor)
    rect = txt.get_rect(center=(LARGURA // 2, y))
    TELA.blit(txt, rect)

def tela_inicial():
    while True:
        TELA.fill(PRETO)
        mostrar_texto("JOGO DA COBRINHA", 60, AMARELO, ALTURA // 2 - 120)
        mostrar_texto("1 - Jogar", 40, BRANCO, ALTURA // 2)
        mostrar_texto("2 - Sair", 40, BRANCO, ALTURA // 2 + 60)
        mostrar_texto("Controles: P1 = Setas | P2 = WASD | P = Pausa | R = Reiniciar", 28, ROXO, ALTURA // 2 + 120)
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    return
                elif evento.key == pygame.K_2:
                    pygame.quit()
                    sys.exit()

def tela_game_over(vencedor, pontos1, pontos2, highscore1, highscore2):
    while True:
        TELA.fill(PRETO)
        if vencedor == 1:
            mostrar_texto("P1 venceu!", 60, cor_cobra1, ALTURA // 2 - 60)
        elif vencedor == 2:
            mostrar_texto("P2 venceu!", 60, cor_cobra2, ALTURA // 2 - 60)
        else:
            mostrar_texto("Empate!", 60, ROXO, ALTURA // 2 - 60)
        mostrar_texto(f"P1: {pontos1}  P2: {pontos2}", 40, BRANCO, ALTURA // 2)
        mostrar_texto(f"Recorde P1: {highscore1}  Recorde P2: {highscore2}", 32, BRANCO, ALTURA // 2 + 40)
        mostrar_texto("Pressione R para jogar novamente ou ESC para sair", 32, BRANCO, ALTURA // 2 + 90)
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    return True
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def pausar():
    pausado = True
    mostrar_texto("PAUSADO", 60, AMARELO, ALTURA // 2)
    pygame.display.update()
    while pausado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    pausado = False

def jogar(highscore1, highscore2):
    # Cobra 1 (setas)
    x1, y1 = LARGURA // 4, ALTURA // 2
    velocidade_x1, velocidade_y1 = tamanho_quadrado, 0
    corpo1 = [[x1, y1]]
    tamanho1 = 1
    direcao1 = "DIREITA"
    proxima_direcao1 = "DIREITA"

    # Cobra 2 (WASD)
    x2, y2 = 3 * LARGURA // 4, ALTURA // 2
    velocidade_x2, velocidade_y2 = -tamanho_quadrado, 0
    corpo2 = [[x2, y2]]
    tamanho2 = 1
    direcao2 = "ESQUERDA"
    proxima_direcao2 = "ESQUERDA"

    ocupados = set(tuple(pos) for pos in corpo1 + corpo2)
    maca1 = gerar_comida(ocupados)
    ocupados.add(maca1)
    maca2 = gerar_comida(ocupados)

    fim_jogo = False
    vencedor = 0

    while not fim_jogo:
        TELA.fill(PRETO)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                # Cobra 1 (setas)
                if evento.key == pygame.K_UP and direcao1 != "BAIXO":
                    proxima_direcao1 = "CIMA"
                elif evento.key == pygame.K_DOWN and direcao1 != "CIMA":
                    proxima_direcao1 = "BAIXO"
                elif evento.key == pygame.K_LEFT and direcao1 != "DIREITA":
                    proxima_direcao1 = "ESQUERDA"
                elif evento.key == pygame.K_RIGHT and direcao1 != "ESQUERDA":
                    proxima_direcao1 = "DIREITA"
                # Cobra 2 (WASD)
                elif evento.key == pygame.K_w and direcao2 != "BAIXO":
                    proxima_direcao2 = "CIMA"
                elif evento.key == pygame.K_s and direcao2 != "CIMA":
                    proxima_direcao2 = "BAIXO"
                elif evento.key == pygame.K_a and direcao2 != "DIREITA":
                    proxima_direcao2 = "ESQUERDA"
                elif evento.key == pygame.K_d and direcao2 != "ESQUERDA":
                    proxima_direcao2 = "DIREITA"
                # Pausa
                elif evento.key == pygame.K_p:
                    pausar()
                # Reiniciar rápido
                elif evento.key == pygame.K_r:
                    return None, None, True

        # Atualiza direções
        direcao1 = proxima_direcao1
        direcao2 = proxima_direcao2

        # Atualiza velocidades
        if direcao1 == "CIMA":
            velocidade_x1, velocidade_y1 = 0, -tamanho_quadrado
        elif direcao1 == "BAIXO":
            velocidade_x1, velocidade_y1 = 0, tamanho_quadrado
        elif direcao1 == "ESQUERDA":
            velocidade_x1, velocidade_y1 = -tamanho_quadrado, 0
        elif direcao1 == "DIREITA":
            velocidade_x1, velocidade_y1 = tamanho_quadrado, 0

        if direcao2 == "CIMA":
            velocidade_x2, velocidade_y2 = 0, -tamanho_quadrado
        elif direcao2 == "BAIXO":
            velocidade_x2, velocidade_y2 = 0, tamanho_quadrado
        elif direcao2 == "ESQUERDA":
            velocidade_x2, velocidade_y2 = -tamanho_quadrado, 0
        elif direcao2 == "DIREITA":
            velocidade_x2, velocidade_y2 = tamanho_quadrado, 0

        # Atualiza posições
        x1 += velocidade_x1
        y1 += velocidade_y1
        x2 += velocidade_x2
        y2 += velocidade_y2

        # Só move se já começou
        corpo1.append([x1, y1])
        if len(corpo1) > tamanho1:
            del corpo1[0]
        corpo2.append([x2, y2])
        if len(corpo2) > tamanho2:
            del corpo2[0]

        # Colisão com parede
        if x1 < 0 or x1 >= LARGURA or y1 < 0 or y1 >= ALTURA:
            vencedor = 2
            fim_jogo = True
        if x2 < 0 or x2 >= LARGURA or y2 < 0 or y2 >= ALTURA:
            if fim_jogo and vencedor == 2:
                vencedor = 0  # Empate
            elif not fim_jogo:
                vencedor = 1
            fim_jogo = True

        # Colisão com o próprio corpo
        if [x1, y1] in corpo1[:-1]:
            vencedor = 2
            fim_jogo = True
        if [x2, y2] in corpo2[:-1]:
            if fim_jogo and vencedor == 2:
                vencedor = 0
            elif not fim_jogo:
                vencedor = 1
            fim_jogo = True

        # Colisão entre cobras (cabeça de uma no corpo da outra)
        if [x1, y1] in corpo2:
            vencedor = 2
            fim_jogo = True
        if [x2, y2] in corpo1:
            if fim_jogo and vencedor == 2:
                vencedor = 0
            elif not fim_jogo:
                vencedor = 1
            fim_jogo = True

        # Comer maçã cobra 1
        if (x1, y1) == maca1:
            tamanho1 += 1
            tocar_som()
            ocupados = set(tuple(pos) for pos in corpo1 + corpo2)
            ocupados.add(maca2)
            maca1 = gerar_comida(ocupados)
        elif (x1, y1) == maca2:
            tamanho1 += 1
            tocar_som()
            ocupados = set(tuple(pos) for pos in corpo1 + corpo2)
            ocupados.add(maca1)
            maca2 = gerar_comida(ocupados)

        # Comer maçã cobra 2
        if (x1, y1) == maca1:
            tamanho1 += 1
            tocar_som()
            ocupados = set([tuple(pos) for pos in corpo1 + corpo2] + [maca2])
            maca1 = gerar_comida(ocupados)
        elif (x1, y1) == maca2:
            tamanho1 += 1
            tocar_som()
            ocupados = set([tuple(pos) for pos in corpo1 + corpo2] + [maca1])
            maca2 = gerar_comida(ocupados)

        # Comer maçã cobra 2
        if (x2, y2) == maca1:
            tamanho2 += 1
            tocar_som()
            ocupados = set([tuple(pos) for pos in corpo1 + corpo2] + [maca2])
            maca1 = gerar_comida(ocupados)
        elif (x2, y2) == maca2:
            tamanho2 += 1
            tocar_som()
            ocupados = set([tuple(pos) for pos in corpo1 + corpo2] + [maca1])
            maca2 = gerar_comida(ocupados)
        desenhar_comida(maca1, VERMELHO)
        desenhar_comida(maca2, AMARELO)
        desenhar_cobra(corpo1, cor_cobra1)
        desenhar_cobra(corpo2, cor_cobra2)
        mostrar_pontos(tamanho1 - 1, tamanho2 - 1, highscore1, highscore2)

        pygame.display.update()
        relogio.tick(velocidade_jogo)

    return vencedor, tamanho1 - 1, tamanho2 - 1, False
def main():
    tela_inicial()
    highscore1 = 0
    highscore2 = 0
    while True:
        resultado = jogar(highscore1, highscore2)
        # Reinício rápido
        if resultado is not None and len(resultado) == 3 and resultado[2]:
            continue
        vencedor, pontos1, pontos2, _ = resultado
        if pontos1 > highscore1:
            highscore1 = pontos1
        if pontos2 > highscore2:
            highscore2 = pontos2
        if not tela_game_over(vencedor, pontos1, pontos2, highscore1, highscore2):
            break

if __name__ == "__main__":
    main()