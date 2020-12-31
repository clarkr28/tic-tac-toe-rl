from player_base import PlayerBase
from constants import CELL_EMPTY

class PlayerRule(PlayerBase):

    '''
    pick the first available slot on the board
    arguments:
        board: Board - the tic tac toe board
        marker: string - the marker that is assigned to this player
    return: (row, col) tuple where row and col are ints of either 0, 1 or 2
    '''
    def pick_move(self, board, marker):
        for row in range(3):
            for col in range(3):
                if board.get_cell(row, col) == CELL_EMPTY:
                    return (row, col)
