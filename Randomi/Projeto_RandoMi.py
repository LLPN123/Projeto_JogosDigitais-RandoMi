import pygame
import sys

pygame.init()

# Tamanho da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RadoMi - Menu")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (100, 200, 255)
GRAY = (100, 100, 100)


# Fontes
title_font = pygame.font.SysFont('Arial', 64, bold=True)
menu_font = pygame.font.SysFont('Arial', 48)
selected_font = pygame.font.SysFont('Arial', 48, bold=True)

# Menu
menu_options = ["Start", "Fases", "Créditos"]
selected_option = 0

# Tamanho dos blocos (tiles)
TILE_SIZE = 40

# Carrega as texturas
floor_img = pygame.image.load("C:/Users/tadeu/Downloads/floor.jpeg")
floor_img = pygame.transform.scale(floor_img, (TILE_SIZE, TILE_SIZE))

wall_img = pygame.image.load("C:/Users/tadeu/Downloads/wall.jpg")
wall_img = pygame.transform.scale(wall_img, (TILE_SIZE, TILE_SIZE))

# Mapa do fundo
tilemap = [
    "....................",
    ".##################.",
    ".##################.",
    ".##################.",
    ".##################.",
    ".##################.",
    ".##################.",
    ".##################.",
    ".##################.",
    ".##################.", 
    ".##################.", 
    ".##################.",
    ".##################.",
    ".##################.",
    "....................",
]

# Desenha o fundo baseado no tilemap
def draw_background():
    for y, row in enumerate(tilemap):
        for x, tile in enumerate(row):
            pos = (x * TILE_SIZE, y * TILE_SIZE)
            if tile == '#':
                screen.blit(floor_img, pos)
            elif tile == '.':
                screen.blit(wall_img, pos)

# Desenha o menu
def draw_menu():
    draw_background()

    # Título
    title = title_font.render("RadoMi", True, BLACK)
    title_rect = title.get_rect(center=(WIDTH//2, HEIGHT//4))
    screen.blit(title, title_rect)

    # Opções do menu
    for i, option in enumerate(menu_options):
        if i == selected_option:
            text = selected_font.render(option, True, GRAY)
        else:
            text = menu_font.render(option, True, BLACK)

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
                if selected_option == 0:
                    print("Começar o jogo!")
                elif selected_option == 1:
                    print("Abrir menu de fases!")
                elif selected_option == 2:
                    print("Mostrar créditos!")

    draw_menu()

pygame.quit()
sys.exit()
