
# CONSTANTS
CELL_EMPTY = ' '
CELL_PLAYER_1 = 'X'
CELL_PLAYER_2 = 'O'

WIN_OPTIONS = [
    [[0,0], [0,1], [0,2]],  # top row
    [[1,0], [1,1], [1,2]],  # middle row
    [[2,0], [2,1], [2,2]],  # bottom row
    [[0,0], [1,0], [2,0]],  # left column
    [[0,1], [1,1], [2,1]],  # middle column
    [[0,2], [1,2], [2,2]],  # right column
    [[0,0], [1,1], [2,2]],  # top-left to bottom-right diag
    [[0,2], [1,1], [2,0]]   # top-right to bottom-left diag
]