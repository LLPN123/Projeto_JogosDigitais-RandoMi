import pygame
import sys

# Inicializar pygame
pygame.init()

# Tamanho da tela do menu
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RadoMi - Seleção de Nível")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

# Fontes
title_font = pygame.font.SysFont('Arial', 64, bold=True)
menu_font = pygame.font.SysFont('Arial', 48)
selected_font = pygame.font.SysFont('Arial', 48, bold=True)
font = pygame.font.SysFont('Arial', 28)

# Menu de níveis
menu_options = ["Fácil", "Médio", "Difícil"]
selected_option = 0

# Tile settings
TILE_SIZE = 40

# Carregar imagens de fundo para o menu
floor_img_menu = pygame.image.load("C:/Users/tadeu/Downloads/grama.jpeg")
floor_img_menu = pygame.transform.scale(floor_img_menu, (TILE_SIZE, TILE_SIZE))

wall_img_menu = pygame.image.load("C:/Users/tadeu/Downloads/gramaBranca.jpeg")
wall_img_menu = pygame.transform.scale(wall_img_menu, (TILE_SIZE, TILE_SIZE))

# Mapa de fundo do menu
tilemap = [
    "....................",
    ".##################.",
    ".##################.",
    ".##################.",
    ".##################.",
    ".##################.",
    ".#######....#######.",
    "....................",
    ".#######....#######.",
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

    title = title_font.render("Escolha o Nível", True, BLACK)
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

# Função que inicia o jogo com base no nível
def start_game(level):
    TILE_SIZE = 20
    RED = (255, 0, 0)

    # Carregar e redimensionar imagens para o jogo
    floor_img = pygame.image.load("C:/Users/tadeu/Downloads/grama.jpeg")
    wall_img = pygame.image.load("C:/Users/tadeu/Downloads/gramaBranca.jpeg")
    fim_img = pygame.image.load("C:/Users/tadeu/Downloads/rede.jpg")
    fim_img = pygame.transform.scale(fim_img, (TILE_SIZE, TILE_SIZE))
    floor_img = pygame.transform.scale(floor_img, (TILE_SIZE, TILE_SIZE))
    wall_img = pygame.transform.scale(wall_img, (TILE_SIZE, TILE_SIZE))

    # Labirintos para cada nível
    if level == 0:  # Fácil
        maze_layout = [
        "#################################################",
        "#...#.......................#.........#.........#",
        "#.#.#.#####.#####.#.#######.#.#######.#.#######.#",
        "#.#.#.#...#.#.....#.#.....#.#.#.....#.#.......#.#",
        "#.#.#.#.#.#.#.#####.#.###.#.#.#.###.#.#######.#.#",
        "#.#.#...#.#.#.....#...#...#.#.#.#...#.....#...#.#",
        "#.#.#####.#.#####.#####.###.#.#.#.#######.#.###.#",
        "#.#.#.....#.#...#.....#.....#.#.#.#.....#.#.#...#",
        "#.#.#.#####.#.#.#####.#######.#.#.#.#.#.#.#.#.###",
        "#.#.#.....#.#.#.#...#.#.......#.#.#.#.#.#.#.#...#",
        "#.#.#####.#.#.#.#.#.#.#.#######.#.#.#.#.#.#.###.#",
        "#.#.#...#.#.#.#.#.#.#.#.....#...#.#.#.#.#.#.....#",
        "#.#.#.#.#.#.#.#.#.#.#.#####.#.###.#.#.#.#.#####.#",
        "#.#.#.#...#.#.#.#.#.#.#.....#.....#.#.#.#.....#.#",
        "#.#.#.#####.#.#.#.#.#.#.###########.#.#.#####.#.#",
        "#.#.#.#.....#.#.#.#.#.#.............#.#.....#.#.#",
        "#.#.#.#.#####.#.#.#.#.###############.#####.#.#.#",
        "#.#.#.#.#.....#.#.#.#.#...............#...#.#.#.#",
        "#.#.#.#.#.#####.#.#.#.#.##########.####.#.#.#.#.#",
        "#.#.#.#.#.....#.#.#.#.#.#...............#.#.#.#.#",
        "#.#.#.#.#####.#.#.#.#.#.#.###############.#.#.#.#",
        "#.#.#.#.....#.#.#.#.#.#.#.#...............#.#.#.#",
        "#.#.#.#####.#.#.#.#.#.#.#.#.###############.#.#.!",
        "#.#.#.....#.#.#.#.#.#.#.#.#.#...............#.#.#",
        "#.#.#####.#.#.#.#.#.#.#.#.#.#.###############.#.#",
        "#.#.......#.#.#.#.#.#.#.#.#.#.#...............#.#",
        "#.#.#.#####.#.#.#.#.#.#.#.#.#.#.###############.#",
        "#.#.#.....#.#.#.#.#.#.#.#.#.#.#.................#",
        "#.#.#####.#.#.#.#.#.#.#.#.#.#####################",
        "#.#.....#.#.#.#.#.#.#.#.........................#",
        "#.#####.#.#.#.#.#.#.#.#########################.#",
        "#.#.....#.#.#.#.#.#.....................#.....#.#",
        "#.#.#####.#.#.#.#######################.#.###.#.#",
        "#.#.#.....#.#.#.#.......................#.#...#.#",
        "#.#.#.#####.#.#.#########################.#.###.#",
        "#.#.#.#.....#.#.#.........................#.....#",
        "#.#.#.#.#####.#.#.###############################",
        "#.#.#.#.....#.#.#...............................#",
        "#.#.#.#####.#.#.###############################.#",
        "#.#.#.......#.#...............................#.#",
        "#.#.#######.#.#.#############################.#.#",
        "#...............................................#",
        "#################################################"
        ]
    elif level == 1:  # Médio
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
    elif level == 2:  # Difícil
        maze_layout = [
            "#################################################",
        "#...........#.................#.......#.........#",
        "#.#######.#.#.#######.#######.#.#####.#.#######.#",
        "#.#.....#.#.#.#.....#.#.....#.#.#...#.#.#.....#.#",
        "#.#.###.#.#.#.#.###.#.#.###.#.#.#.#.#.#.#.###.#.#",
        "#.#.#...#.#.#...#...#.#.#...#.#.#.#.#.#...#...#.#",
        "#.#.#.###.#.#####.###.#.#.###.#.#.#.#.#####.###.#",
        "#.#.#...#.#.......#...#.#...#.#.#.#.#.#.....#...#",
        "#.#.###.#.#########.###.#.#.#.#.#.#.#.#.#####.###",
        "#.#.#...#.........#...#.#.#.#.#.#.#.#.#.....#...#",
        "#.#.#.###########.###.#.#.#.#.#.#.#.#.#####.###.#",
        "#.#.#.#.........#...#.#.#.#.#.#.#.#.#.....#.#...#",
        "#.#.#.#.#######.###.#.#.#.#.#.#.#.#.#####.#.#.###",
        "#.#.#.#.#.....#.....#.#.#.#.#.#.#.#.....#.#.#...#",
        "#.#.#.#.#.###.#######.#.#.#.#.#.#.#####.#.#.###.#",
        "#.#.#.#.#.#...#.....#.#.#.#.#.#.#.#.....#.#.#...#",
        "#.#.#.#.#.#.###.###.#.#.#.#.#.#.#.#.#######.#.###",
        "#.#.#.#.#.#...#.#...#.#.#.#.#.#.#.#.........#...#",
        "#.#.#.#.#.###.#.#.###.#.#.#.#.#.#.#############.#",
        "#.#.#.#.#.#...#.#...#.#.#.#.#.#.#...............#",
        "#.#.#.#.#.#.###.###.#.#.#.#.#.###################",
        "#.#.#.#.#.#...#...#.#.#.#.#.#.#.................#",
        "#.#.#.#.#.###.#.#.#.#.#.#.#.#.###############.###",
        "#.#.#.#.#...#.#.#.#.#.#.#.#.#.#.............#.#.#",
        "#.#.#.###.#.#.#.#.#.#.#.#.#.#.#.###########.#.#.#",
        "#.#.#.....#.#.#.#.#.#.#.#.#.#.#.#...........#.#.#",
        "#.#.#######.#.#.#.#.#.#.#.#.#.#.#.###########.#.#",
        "#.#.........#.#.#.#.#.#.#.#.#.#.#.#...........#.#",
        "#.###########.#.#.#.#.#.#.#.#.#.#.#.###########.#",
        "#.............#.#.#.#.#.#.#.#.#.#.#.#...........#",
        "###############.#.#.#.#.#.#.#.#.#.#.#.###########",
        "#...............#.#.#.#.#.#.#.#.#.#.#...........#",
        "#.###############.#.#.#.#.#.#.#.#.#.###########.#",
        "#.#...............#.#.#.#.#.#.#.#.#.............#",
        "#.#.###############.#.#.#.#.#.#.#.###############",
        "#.#.................#.#.#.#.#.#.#...............#",
        "#.###################.#.#.#.#.#.###############.#",
        "#.....................#.#.#.#.#.................#",
        "#######################.#.#.#.###################",
        "#.......................#.#.#...................#",
        "#################################################"
        ]

    # Converter o layout para matriz de inteiros
    maze = [[1 if ch == "#" else 0 for ch in row] for row in maze_layout]
    ROWS = len(maze)
    COLS = len(maze[0])

    game_screen = pygame.display.set_mode((COLS * TILE_SIZE, ROWS * TILE_SIZE))
    pygame.display.set_caption("RadoMi - Labirinto")

    player_x, player_y = 1, 1
    move_delay = 5
    move_count = 0
    clock = pygame.time.Clock()
    running = True

    # Início do cronômetro
    start_ticks = pygame.time.get_ticks()

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

        game_screen.fill(BLACK)

        # Verifica se chegou no "!"
        if maze_layout[player_y][player_x] == "!":
            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # em segundos

            # Mostrar mensagem de missão cumprida
            overlay = pygame.Surface((COLS * TILE_SIZE, ROWS * TILE_SIZE))
            overlay.set_alpha(220)
            overlay.fill(BLACK)
            game_screen.blit(overlay, (0, 0))

            msg1 = font.render("Missão Cumprida Craque - Gol marcado", True, WHITE)
            msg2 = font.render(f"Tempo: {elapsed_time:.2f} segundos", True, WHITE)
            game_screen.blit(msg1, (40, ROWS * TILE_SIZE // 2 - 20))
            game_screen.blit(msg2, (40, ROWS * TILE_SIZE // 2 + 10))
            pygame.display.flip()

            # Espera até o jogador pressionar qualquer tecla
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        waiting = False
            return  # Volta ao menu principal

        # Desenhar labirinto
        for y in range(ROWS):
            for x in range(COLS):
                char = maze_layout[y][x]
                if char == "#":
                    game_screen.blit(wall_img, (x * TILE_SIZE, y * TILE_SIZE))
                elif char == "!":
                    game_screen.blit(floor_img, (x * TILE_SIZE, y * TILE_SIZE))
                    game_screen.blit(fim_img, (x * TILE_SIZE, y * TILE_SIZE))
                else:
                    game_screen.blit(floor_img, (x * TILE_SIZE, y * TILE_SIZE))

        pygame.draw.rect(game_screen, RED, (player_x * TILE_SIZE, player_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        pygame.display.flip()

# === Loop do menu principal === #
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
                if selected_option in [0, 1, 2]:
                    start_game(selected_option)
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    draw_menu()

pygame.quit()
sys.exit()
