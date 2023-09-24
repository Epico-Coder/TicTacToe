import pygame

from ai import minimax, get_best_move
from game import draw_x, draw_o, draw_board, draw_bar, win, WIDTH, HEIGHT, BOARD_SIZE, BG
from utils import Position

pygame.init()

new = Position()

pygame.display.set_caption("TicTacToe")


def re_draw_win():
    win.blit(BG, (0, 0))

    draw_board(WIDTH // 2 - (BOARD_SIZE * WIDTH) // 2,
               HEIGHT // 2 - (BOARD_SIZE * HEIGHT) // 2,
               BOARD_SIZE * WIDTH,
               BOARD_SIZE * HEIGHT)

    evaluation = minimax(new, 0, new.turn)
    normalized = (evaluation + 10) / 20
    draw_bar(0, 0, WIDTH, 0.1 * HEIGHT, normalized)

    for i, row in enumerate(new.position):
        for j, ele in enumerate(row):
            if ele == 1:
                draw_x(i, j)
            elif ele == -1:
                draw_o(i, j)

    pygame.display.update()


def main():
    global BG, WIDTH, HEIGHT

    while True:

        if type(new.result) != int:
            if new.turn == -1:
                move = get_best_move(new, new.turn)
                new.make_move(move)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.WINDOWRESIZED:
                BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))
                WIDTH = win.get_width()
                HEIGHT = win.get_height()

            if type(new.result) != int:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x = event.pos[0]
                    mouse_y = event.pos[1]

                    board_x = WIDTH // 2 - (BOARD_SIZE * WIDTH) // 2
                    board_y = HEIGHT // 2 - (BOARD_SIZE * HEIGHT) // 2

                    cell_width = BOARD_SIZE * WIDTH // 3
                    cell_height = BOARD_SIZE * HEIGHT // 3

                    clicked_row = int((mouse_y - board_y) // cell_height)
                    clicked_col = int((mouse_x - board_x) // cell_width)

                    new.make_move((clicked_row, clicked_col))
            else:
                if new.result == 1:
                    print("X wins!")
                elif new.result == 0:
                    print("Draw!")
                elif new.result == -1:
                    print("O wins!")

        re_draw_win()


main()
