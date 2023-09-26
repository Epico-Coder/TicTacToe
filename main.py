import pygame
import time

from ai import minimax, get_best_move, load_cache, save_cache
from game import draw_x, draw_o, draw_board, draw_bar
from utils import Position

pygame.init()

# constants
WIDTH, HEIGHT = 1280, 720

BG = pygame.image.load("bg.webp")
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

BOARD_SIZE = 0.75

win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("TicTacToe")

new = Position()

cache = load_cache("cache.pkl")

# re draw ui every frame
def re_draw_win():
    win.blit(BG, (0, 0))

    draw_board(WIDTH // 2 - (BOARD_SIZE * WIDTH) // 2,
               HEIGHT // 2 - (BOARD_SIZE * HEIGHT) // 2,
               BOARD_SIZE * WIDTH,
               BOARD_SIZE * HEIGHT,
               win)

    evaluation = minimax(position=new, depth=0, maximizing_player=new.turn, cache=cache)
    normalized = (evaluation + 10) / 20
    draw_bar(0, 0, WIDTH, 0.1 * HEIGHT, normalized, win)

    for i, row in enumerate(new.position):
        for j, ele in enumerate(row):
            if ele == 1:
                draw_x(i, j, BOARD_SIZE, WIDTH, HEIGHT, win)
            elif ele == -1:
                draw_o(i, j, BOARD_SIZE, WIDTH, HEIGHT, win)

    pygame.display.update()


def main():
    global BG, WIDTH, HEIGHT
    run = True

    clock = pygame.time.Clock()
    clock.tick(30)

    while run:

        # ai's turn if game not over
        if type(new.result) != int:
            if new.turn == -1:
                move = get_best_move(new, new.turn, cache)
                new.make_move(move)

        for event in pygame.event.get():

            # exit
            if event.type == pygame.QUIT:
                run = False

            # resize ui
            if event.type == pygame.WINDOWRESIZED:
                WIDTH = win.get_width()
                HEIGHT = win.get_height()
                BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

            # find row and col, make move
            if event.type == pygame.MOUSEBUTTONDOWN:
                if type(new.result) != int:
                    mouse_x = event.pos[0]
                    mouse_y = event.pos[1]

                    board_x = WIDTH // 2 - (BOARD_SIZE * WIDTH) // 2
                    board_y = HEIGHT // 2 - (BOARD_SIZE * HEIGHT) // 2

                    cell_width = BOARD_SIZE * WIDTH // 3
                    cell_height = BOARD_SIZE * HEIGHT // 3

                    clicked_row = int((mouse_y - board_y) // cell_height)
                    clicked_col = int((mouse_x - board_x) // cell_width)

                    new.make_move((clicked_row, clicked_col))

        re_draw_win()

    # after quit
    else:
        pygame.quit()

        if new.result == 1:
            print("X wins!")
        elif new.result == 0:
            print("Draw!")
        elif new.result == -1:
            print("O wins!")

        evaluated_len = cache.__len__()
        print(f"{evaluated_len} positions stored!")


main()

save_cache(cache, "cache.pkl")
