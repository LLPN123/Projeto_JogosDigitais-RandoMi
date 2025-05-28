import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 1720, 880
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RadoMi - Seleção de Nível")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
YEL = (194, 255, 126)
RED = (255, 0 , 5)
title_font = pygame.font.SysFont('Arial', 64, bold=True)
menu_font = pygame.font.SysFont('Arial', 48)
selected_font = pygame.font.SysFont('Arial', 48, bold=True)
font = pygame.font.SysFont('Arial', 28)

menu_options = ["Fácil", "Médio", "Difícil"]
selected_option = 0

menu_background_img = pygame.image.load("RANDOMI.png").convert_alpha()
menu_background_img = pygame.transform.scale(menu_background_img, (WIDTH, HEIGHT))

def draw_menu():
    screen.blit(menu_background_img, (0, 0))
    for i, option in enumerate(menu_options):
        text_y_position = HEIGHT // 2 + i * 100
        if i == selected_option:
            text_surface = selected_font.render(option, True, YEL)
        else:
            text_surface = menu_font.render(option, True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, text_y_position))

        padding_x = 40  
        padding_y = 15  
        border_width = 3 # Largura da borda branca

        rect_for_option = pygame.Rect(
            text_rect.left - padding_x - border_width,
            text_rect.top - padding_y - border_width,
            text_rect.width + 2 * padding_x + 2 * border_width,
            text_rect.height + 2 * padding_y + 2 * border_width
        )

        pygame.draw.rect(screen, WHITE, rect_for_option, border_width, 10) 
        pygame.draw.rect(screen, RED, (rect_for_option.left + border_width, rect_for_option.top + border_width, rect_for_option.width - 2 * border_width, rect_for_option.height - 2 * border_width), 0, 10)
        screen.blit(text_surface, text_rect)

    pygame.display.flip()


def pause_menu(game_screen, level_name, elapsed_time):
    pause_font = pygame.font.SysFont('Arial', 36, bold=True)
    small_font = pygame.font.SysFont('Arial', 24)
    width, height = game_screen.get_size()

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "quit"
                # M para voltar ao jogo
                elif event.key == pygame.K_m:
                    paused = False

        overlay = pygame.Surface((width, height))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        game_screen.blit(overlay, (0, 0))
        title_text = pause_font.render("Jogo Pausado", True, WHITE)
        level_text = small_font.render(f"Nível: {level_name}", True, WHITE)
        time_text = small_font.render(f"Tempo: {elapsed_time:.2f} segundos", True, WHITE)
        instruction1 = small_font.render("Pressione M para continuar", True, WHITE)
        instruction2 = small_font.render("Pressione ESC para voltar ao menu principal", True, WHITE)
        game_screen.blit(title_text, title_text.get_rect(center=(width//2, height//2 - 100)))
        game_screen.blit(level_text, level_text.get_rect(center=(width//2, height//2 - 40)))
        game_screen.blit(time_text, time_text.get_rect(center=(width//2, height//2)))
        game_screen.blit(instruction1, instruction1.get_rect(center=(width//2, height//2 + 60)))
        game_screen.blit(instruction2, instruction2.get_rect(center=(width//2, height//2 + 100)))

        pygame.display.flip()
def start_game(level):
    TILE_SIZE = 20
    RED = (255, 0, 0)


    floor_img = pygame.image.load("grama.jpeg")
    wall_img = pygame.image.load("gramaBranca.jpeg")
    fim_img = pygame.image.load("rede.jpg")
    fim_img = pygame.transform.scale(fim_img, (TILE_SIZE, TILE_SIZE))
    floor_img = pygame.transform.scale(floor_img, (TILE_SIZE, TILE_SIZE))
    wall_img = pygame.transform.scale(wall_img, (TILE_SIZE, TILE_SIZE))


    if level == 0:  
        maze_layout = [
        "#################################################",
        "#...............................................#",
        "#.########.######.###.#.#######################.#",
        "#.#......#.#....#.#.#.#.............#...........#",
        "#.#.####.#.#.##.#.#.#.###########...#.#########.#",
        "#.#....#.#.#.#..#...#.#.........#.....#.......#.#",
        "#.####.#.#.#.#.#######.#.#######.##...##.####.#.#",
        "#......#...#.#.........#.......#.#.....#....#.#.#",
        "##########.....####.#########.#.#.#.#.#####.#.#.#",
        "#..........##.....#.........#.#.#.#.#.....#.#.#.#",
        "#.###############.#.#.#####.#.#.#.#.#####.#.#.#.#",
        "#.#...............#.#.#.....#.#.#.#.#.....#.#.#.#",
        "#.#.###############.#.#.#####.#.#.#.#.#####.#.#.#",
        "#.#.................#.#.#.....#.#.#.#.#.....#.#.#",
        "#.##############.####.#.#.#####.#.#.#.#.#####.#.#",
        "#..........#..........#.#.....#.#.#.#.#.#.....#.#",
        "#######################.#####.#.#.#.#.#.#####.#.#",
        "#....#..................#.....#.#.#.#.#.....#.#.#",
        "#.#####################.#.#####.#.#.#######.#.#.#",
        "#.......................#.......#.#.........#...#",
        "######..###########.###.##.####.#...#####...#.###",
        "#.....................#.##.####################.!",
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
    elif level == 1: 
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
    elif level == 2:  
        maze_layout = [
        "#################################################",
        "#...........#.................#.................#",
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
        "#.#.#.#.#.###.#.#.###.#.#.#.#.#.#.###############",
        "#.#.#.#.#.#...#.#...#.#.#.#.#...#...............!",
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
        "#.#############.#.#.#.#.#.#.#.#.#.#.#.###########",
        "#...............#.#.#.#.#.#.#.#.#.#.#...........#",
        "#.###############.#.#.#.#.#.#.#.#.#.###########.#",
        "#.#...............#...#.#.#.#.#.#.#.............#",
        "#.#.###############.#.#.#.#.#.#.#.###############",
        "#.#.................#.#.#.#.#.#.#...............#",
        "#.###################.#.#.#.#.#.###############.#",
        "#.....................#.#.#.#.#.................#",
        "#######################.#.#.#.###################",
        "#.......................#.#.#...................#",
        "#################################################"
        ]

    maze = [[1 if ch == "#" else 0 for ch in row] for row in maze_layout]
    ROWS = len(maze)
    COLS = len(maze[0])

    game_screen = pygame.display.set_mode((COLS * TILE_SIZE, ROWS * TILE_SIZE))
    pygame.display.set_caption(f"RadoMi - Labirinto {menu_options[level]}")
    try:
        floor_img = pygame.image.load("grama.jpeg")
        floor_img = pygame.transform.scale(floor_img, (TILE_SIZE, TILE_SIZE))
        wall_img = pygame.image.load("gramaBranca.jpeg")
        wall_img = pygame.transform.scale(wall_img, (TILE_SIZE, TILE_SIZE))
        fim_img = pygame.image.load("rede.jpg")
        fim_img = pygame.transform.scale(fim_img, (TILE_SIZE, TILE_SIZE))
    except pygame.error as e:
        print(f"Erro ao carregar imagens do jogo: {e}")
        print("Verifique se os caminhos das imagens estão corretos.")
        return 

    player_x, player_y = 1, 1 
    end_x, end_y = -1, -1

    for r_idx, row in enumerate(maze_layout):
        for c_idx, char in enumerate(row):
            if char == '.': 
                player_x, player_y = c_idx, r_idx
                break
        if maze_layout[player_y][player_x] == '.': 
            break
    
    for r_idx, row in enumerate(maze_layout):
        for c_idx, char in enumerate(row):
            if char == '!':
                end_x, end_y = c_idx, r_idx
                break
        if end_x != -1:
            break

    move_delay = 5 
    move_count = 0
    clock = pygame.time.Clock()
    running = True

  
    start_ticks = pygame.time.get_ticks()

    while running:
        clock.tick(60) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                   
                    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
                    result = pause_menu(game_screen, menu_options[level], elapsed_time)
                    if result == "quit":
                        return  

        keys = pygame.key.get_pressed()
        new_x, new_y = player_x, player_y

        if move_count >= move_delay:
            if keys[pygame.K_LEFT]:
                new_x -= 1
            elif keys[pygame.K_RIGHT]: 
                new_x += 1
            elif keys[pygame.K_UP]:
                new_y -= 1
            elif keys[pygame.K_DOWN]:
                new_y += 1

            if 0 <= new_x < COLS and 0 <= new_y < ROWS and maze[new_y][new_x] == 0:
                player_x, player_y = new_x, new_y
            move_count = 0
        else:
            move_count += 1

        game_screen.fill(BLACK) 

       
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

        
        if maze_layout[player_y][player_x] == "!":
            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 

            overlay = pygame.Surface((COLS * TILE_SIZE, ROWS * TILE_SIZE), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 220))
            game_screen.blit(overlay, (0, 0))

            msg1 = font.render("Missão Cumprida Craque - Gol marcado", True, WHITE)
            msg2 = font.render(f"Tempo: {elapsed_time:.2f} segundos", True, WHITE)
            msg1_rect = msg1.get_rect(center=(COLS * TILE_SIZE // 2, ROWS * TILE_SIZE // 2 - 20))
            msg2_rect = msg2.get_rect(center=(COLS * TILE_SIZE // 2, ROWS * TILE_SIZE // 2 + 10))
            
            game_screen.blit(msg1, msg1_rect)
            game_screen.blit(msg2, msg2_rect)
            pygame.display.flip()

            
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        waiting = False
            return  


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
                    pygame.display.set_caption("RadoMi - Seleção de Nível")

    draw_menu()

pygame.quit()
sys.exit()
