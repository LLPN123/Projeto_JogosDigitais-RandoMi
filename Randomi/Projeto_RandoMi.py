import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RadoMi - Menu")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
BLUE = (0, 100, 255)
LIGHT_BLUE = (100, 200, 255)

# Fonte
title_font = pygame.font.SysFont('Arial', 64, bold=True)
menu_font = pygame.font.SysFont('Arial', 48)
selected_font = pygame.font.SysFont('Arial', 48, bold=True)

# Opções do menu
menu_options = ["Começar", "Fases", "Créditos"]
selected_option = 0

# Função para desenhar o menu
def draw_menu():
    screen.fill(BLACK)
    
    # Desenha o título
    title = title_font.render("RadoMi", True, WHITE)
    title_rect = title.get_rect(center=(WIDTH//2, HEIGHT//4))
    screen.blit(title, title_rect)
    
    # Desenha as opções do menu
    for i, option in enumerate(menu_options):
        if i == selected_option:
            text = selected_font.render(option, True, LIGHT_BLUE)
        else:
            text = menu_font.render(option, True, WHITE)
        
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2 + i * 70))
        screen.blit(text, text_rect)
    
    pygame.display.flip()

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)
            elif event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                # Ação quando uma opção é selecionada
                if selected_option == 0:
                    print("Começar o jogo!")
                elif selected_option == 1:
                    print("Abrir menu de fases!")
                elif selected_option == 2:
                    print("Mostrar créditos!")
    
    draw_menu()

pygame.quit()
sys.exit()