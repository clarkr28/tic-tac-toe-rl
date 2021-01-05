from player_base import PlayerBase
from constants import CELL_EMPTY
import random

class PlayerRandom(PlayerBase):

    '''
    pick a random move from the remaining slots on the board
    return: (row, col) tuple where row and col are ints of either 0, 1 or 2
    '''
    def pick_move(self, board, marker):
        remaining_moves = []
        for row in range(3):
            for col in range(3):
                if board.get_cell(row, col) == CELL_EMPTY:
                    remaining_moves.append([row, col])
        if len(remaining_moves) == 0:
            raise ValueError("There are no remaining moves")
        return remaining_moves[random.randint(0, len(remaining_moves) - 1)]