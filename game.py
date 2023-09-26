import pygame


def draw_x(i, j, board_size, width, height, win):
    board_x = width // 2 - (board_size * width) // 2
    board_y = height // 2 - (board_size * height) // 2

    cell_width = board_size * width // 3
    cell_height = board_size * height // 3

    size = int(0.8 * min(cell_width, cell_height))

    x = (board_x + (j * cell_width) + (cell_width // 2)) - (size / 2)
    y = (board_y + (i * cell_height) + (cell_height // 2)) - (size / 2)

    line_color = (255, 255, 255)
    border_color = (0, 0, 0)
    border_thickness = 2

    pygame.draw.line(win, border_color, (x, y), (x + size, y + size), size // 3)
    pygame.draw.line(win, line_color, (x, y), (x + size, y + size), size // 3 - border_thickness)

    pygame.draw.line(win, border_color, (x, y + size), (x + size, y), size // 3)
    pygame.draw.line(win, line_color, (x, y + size), (x + size, y), size // 3 - border_thickness)


def draw_o(i, j, board_size, width, height, win):
    board_x = width // 2 - (board_size * width) // 2
    board_y = height // 2 - (board_size * height) // 2

    cell_width = board_size * width // 3
    cell_height = board_size * height // 3

    size = int(0.8 * min(cell_width, cell_height))

    x = (board_x + (j * cell_width) + (cell_width // 2)) - (size / 2)
    y = (board_y + (i * cell_height) + (cell_height // 2)) - (size / 2)

    border_color = (0, 0, 0)
    circle_color = (255, 255, 255)
    border_thickness = 2

    pygame.draw.circle(win, border_color, (x + size // 2, y + size // 2), size // 2, size // 8)
    pygame.draw.circle(win, circle_color, (x + size // 2, y + size // 2), size // 2 - border_thickness,
                       size // 8 - border_thickness)


def draw_board(x, y, width, height, win):
    line_color = (255, 255, 255)
    border_color = (255, 0, 0)
    border_thickness = 5

    cell_width = width // 3
    cell_height = height // 3

    for i in range(1, 3):
        pygame.draw.line(win, line_color, (x + i * cell_width, y), (x + i * cell_width, y + height), 2)

    for i in range(1, 3):
        pygame.draw.line(win, line_color, (x, y + i * cell_height), (x + width, y + i * cell_height), 2)

    pygame.draw.rect(win, border_color, (x, y, width, height), border_thickness)


def draw_bar(x, y, width, height, value, win):
    white_color = (255, 255, 255)
    black_color = (0, 0, 0)
    separator_color = (150, 150, 150)

    white_width = value * width

    pygame.draw.rect(win, white_color, (x, y, white_width, height))
    pygame.draw.rect(win, black_color, (x + white_width, y, width - white_width, height))
    pygame.draw.line(win, separator_color, (x + white_width, y), (x + white_width, y + height), 3)
