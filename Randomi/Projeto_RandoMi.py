import pygame
import sys
import os

# Inicializar pygame uma vez
pygame.init()

# Tela do menu
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
menu_options = ["Começar", "Fases", "Créditos"]
selected_option = 0

# Tile settings
TILE_SIZE = 40

# Carregar imagens de fundo
floor_img_menu = pygame.image.load("C:/Users/tadeu/Downloads/floor.jpeg")
floor_img_menu = pygame.transform.scale(floor_img_menu, (TILE_SIZE, TILE_SIZE))

wall_img_menu = pygame.image.load("C:/Users/tadeu/Downloads/wall.jpg")
wall_img_menu = pygame.transform.scale(wall_img_menu, (TILE_SIZE, TILE_SIZE))

# Mapa de fundo do menu
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

def draw_background():
    for y, row in enumerate(tilemap):
        for x, tile in enumerate(row):
            pos = (x * TILE_SIZE, y * TILE_SIZE)
            if tile == '#':
                screen.blit(floor_img_menu, pos)
            elif tile == '.':
                screen.blit(wall_img_menu, pos)

def draw_menu():
    draw_background()

    title = title_font.render("RadoMi", True, BLACK)
    title_rect = title.get_rect(center=(WIDTH//2, HEIGHT//4))
    screen.blit(title, title_rect)

    for i, option in enumerate(menu_options):
        if i == selected_option:
            text = selected_font.render(option, True, GRAY)
        else:
            text = menu_font.render(option, True, BLACK)

        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2 + i * 70))
        screen.blit(text, text_rect)

    pygame.display.flip()

# === FUNÇÃO QUE COMEÇA O JOGO === #
def start_game():
    TILE_SIZE = 20
    RED = (255, 0, 0)

    # Recarregar imagens para tamanho menor
    floor_img = pygame.image.load("C:/Users/tadeu/Downloads/floor.jpeg")
    wall_img = pygame.image.load("C:/Users/tadeu/Downloads/wall.jpg")
    floor_img = pygame.transform.scale(floor_img, (TILE_SIZE, TILE_SIZE))
    wall_img = pygame.transform.scale(wall_img, (TILE_SIZE, TILE_SIZE))

    # Mapa do labirinto
    maze_layout = [
    "#################################################",
    "#.....................#.........................#",
    "#.########.######.###.#.#######################.#",
    "#.#......#.#....#.#.#.#.............#...........#",
    "#.#.####.#.#.##.#.#.#.###########...#.#########.#",
    "#.#....#.#.#.#..#...#.#.........#.....#.......#.#",
    "#.####.#.#.#.#.#######.#.#######.##..#.#.####.#.#",
    "#......#...#.#.....#...#.......#.#.#.#.#....#.#.#",
    "###########.#.#####.#########.#.#.#.#.#####.#.#.#",
    "#...........#.....#.#.......#.#.#.#.#.....#.#.#.#",
    "#.###############.#.#.#####.#.#.#.#.#####.#.#.#.#",
    "#.#...............#.#.#.....#.#.#.#.#.....#.#.#.#",
    "#.#.###############.#.#.#####.#.#.#.#.#####.#.#.#",
    "#.#.....#...........#.#.#.....#.#.#.#.#.....#.#.#",
    "#.##############.####.#.#.#####.#.#.#.#.#####.#.#",
    "#..........#..........#.#.....#.#.#.#.#.#.....#.#",
    "#######################.#####.#.#.#.#.#.#####.#.#",
    "#....#..................#.....#.#.#.#.#.....#.#.#",
    "#.#####################.#.#####.#.#.#######.#.#.#",
    "#.......................#.......#.#.........#....",
    "######..###########.#############...#####...#####",
    "######..###########.##############..######...####",
    "#.....................#.........................#",
    "#.########.######.###.#.#######################.#",
    "#.#......#.#....#.#.#.#.............#...........#",
    "#.#.####.#.#.##.#.#.#.###########...#.#########.#",
    "#.#....#.#.#.#..#...#.#.........#.....#.......#.#",
    "#.####.#.#.#.#.#######.#.#######.##..#.#.####.#.#",
    "#......#...#.#.....#...#.......#.#.#.#.#....#.#.#",
    "###########.#.#####.#########.#.#.#.#.#####.#.#.#",
    "#...........#.....#.#.......#.#.#.#.#.....#.#.#.#",
    "#.###############.#.#.#####.#.#.#.#.#####.#.#.#.#",
    "#.#...............#.#.#.....#.#.#.#.#.....#.#.#.#",
    "#.#.###############.#.#.#####.#.#.#.#.#####.#.#.#",
    "#.#.....#...........#.#.#.....#.#.#.#.#.....#.#.#",
    "#.##############.####.#.#.#####.#.#.#.#.#####.#.#",
    "#..........#..........#.#.....#.#.#.#.#.#.....#.#",
    "#######################.#####.#.#.#.#.#.#####.#.#",
    "#....#..................#.....#.#.#.#.#.....#.#.#",
    "#.#####################.#.#####.#.#.#######.#.#.#",
    "#.......................#.......#.#.........#....",
    "##################################################"
]
    maze = [[1 if ch == "#" else 0 for ch in row] for row in maze_layout]
    ROWS = len(maze)
    COLS = len(maze[0])

    game_screen = pygame.display.set_mode((COLS * TILE_SIZE, ROWS * TILE_SIZE))
    pygame.display.set_caption("Jogo de Labirinto")

    player_x, player_y = 1, 1
    move_delay = 5
    move_count = 0

    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        new_x, new_y = player_x, player_y

        if move_count >= move_delay:
            if keys[pygame.K_LEFT]:
                new_x -= 1
            if keys[pygame.K_RIGHT]:
                new_x += 1
            if keys[pygame.K_UP]:
                new_y -= 1
            if keys[pygame.K_DOWN]:
                new_y += 1

            if maze[new_y][new_x] == 0:
                player_x, player_y = new_x, new_y
            move_count = 0
        else:
            move_count += 1

        for y in range(ROWS):
            for x in range(COLS):
                tile = wall_img if maze[y][x] == 1 else floor_img
                game_screen.blit(tile, (x * TILE_SIZE, y * TILE_SIZE))

        pygame.draw.rect(game_screen, RED, (player_x * TILE_SIZE, player_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        pygame.display.flip()

# === LOOP DO MENU === #
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
                    start_game()  # Inicia o jogo
                    # Volta para o menu ao fechar o jogo
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                elif selected_option == 1:
                    print("Abrir menu de fases!")
                elif selected_option == 2:
                    print("Mostrar créditos!")

    draw_menu()

pygame.quit()
sys.exit()
