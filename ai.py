from utils import Position
import copy
import pickle


def load_cache(file: str) -> dict:
    try:
        with open(file, 'rb') as f:
            cache = pickle.load(f)
    except FileNotFoundError:
        cache = {}

    return cache


def save_cache(cache, file: str):
    with open(file, 'wb') as f:
        pickle.dump(cache, f)


def minimax(position: Position, depth=0, maximizing_player: int = 1, cache=None) -> int:

    if cache is None:
        cache = {}

    if position.key in cache:
        return cache[position.key]

    outcome = position.result

    if type(outcome) == int:
        return outcome * (10 - depth)

    if maximizing_player == 1:
        maxEval = float('-inf')
        for child in position.get_children():
            eval_ = minimax(child, depth + 1, -1)
            maxEval = max(maxEval, eval_)

        cache[position.key] = maxEval
        return maxEval

    elif maximizing_player == -1:
        minEval = float('inf')
        for child in position.get_children():
            eval_ = minimax(child, depth + 1, 1)
            minEval = min(minEval, eval_)

        cache[position.key] = minEval
        return minEval


def get_best_move(position: Position, maximizing_player: int = 1, cache: dict = None):

    best_value = float('-inf') if maximizing_player == 1 else float('inf')
    best_move = (None, None)

    for i in range(3):
        for j in range(3):
            if position.position[i][j] == 0:
                new_position = copy.deepcopy(position)
                new_position.make_move((i, j))
                value = minimax(new_position, 0, -maximizing_player, cache)

                if maximizing_player == 1 and value > best_value:
                    best_value = value
                    best_move = (i, j)
                elif maximizing_player == -1 and value < best_value:
                    best_value = value
                    best_move = (i, j)

    return best_move
