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


def minimax(position: Position, depth=0, alpha=float('-inf'), beta=float('inf'),
            maximizing_player: int = 1, cache=None) -> int:

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
            eval_ = minimax(position=child, depth=depth + 1, alpha=alpha, beta=beta, maximizing_player=-1, cache=cache)

            maxEval = max(maxEval, eval_)
            alpha = max(alpha, eval_)

            if alpha >= beta:
                break

        cache[position.key] = maxEval
        return maxEval

    elif maximizing_player == -1:
        minEval = float('inf')
        for child in position.get_children():
            eval_ = minimax(position=child, depth=depth + 1, alpha=alpha, beta=beta, maximizing_player=1, cache=cache)

            minEval = min(minEval, eval_)
            beta = min(beta, eval_)

            if alpha >= beta:
                break

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
                value = minimax(position=new_position, depth=0, maximizing_player=-maximizing_player, cache=cache)

                if maximizing_player == 1 and value > best_value:
                    best_value = value
                    best_move = (i, j)
                elif maximizing_player == -1 and value < best_value:
                    best_value = value
                    best_move = (i, j)

    return best_move
