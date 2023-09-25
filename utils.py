import copy


class Position:
    def __init__(self):
        self.position = [[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]]
        self.corresponding = {1: 'X', 0: '-', -1: 'O'}
        self.turn = 1
        self.result = False
        self.key = ''.join(''.join(map(str, row)) for row in self.position) + str(self.turn)

    def print_table(self):
        horizontal_line = '+' + '---+' * 3
        print(horizontal_line)
        for row in self.position:
            row_str = '|'
            for col in row:
                row_str += ' ' + self.corresponding[col] + ' |'
            print(row_str)
            print(horizontal_line)

    def make_move(self, move: tuple = (None, None)):
        if move == (None, None):
            self.print_table()

            player_to_move = 'X' if self.turn == 1 else 'O'
            print(player_to_move, "to move!")
            move = (int(input("Row: ")), int(input("Column: ")))

        try:
            if self.position[move[0]][move[1]] == 0:
                self.position[move[0]][move[1]] = self.turn
                self.update()
        except IndexError:
            pass

    def update(self):
        self.turn = -self.turn
        self.key = ''.join(''.join(map(str, row)) for row in self.position) + str(self.turn)
        self.check_result()

    def check_result(self):
        possible_players = [-1, 1]

        # Check horizontals
        for player in possible_players:
            for row in self.position:
                if all(cell == player for cell in row):
                    self.result = player
                    return self.result

        # Check verticals
        for player in possible_players:
            for col in range(3):
                if all(row[col] == player for row in self.position):
                    self.result = player
                    return self.result

        # Check diagonals
        for player in possible_players:
            if all(self.position[i][i] == player for i in range(3)) or \
                    all(self.position[i][2 - i] == player for i in range(3)):
                self.result = player
                return self.result

        # Check fully filled
        if all(cell != 0 for row in self.position for cell in row):
            self.result = 0
            return self.result

        # Else
        self.result = False
        return self.result

    def get_children(self):
        children = []
        for row in range(len(self.position)):
            for col in range(len(self.position[row])):
                if self.position[row][col] == 0:
                    child_position = copy.deepcopy(self)
                    child_position.make_move((row, col))
                    children.append(child_position)
        return children
