import numpy as np


# CONSTANTS
CELL_EMPTY = 0
CELL_PLAYER_1 = 1
CELL_PLAYER_2 = 2

CELL_EMPTY_PRINT = ' '
CELL_PLAYER_1_PRINT = 'X'
CELL_PLAYER_2_PRINT = 'O'

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

WIN_OPTIONS_NP = [ 
    np.array([[0,0,0],[0,1,2]]),    # top row
    np.array([[1,1,1],[0,1,2]]),    # middle row
    np.array([[2,2,2],[0,1,2]]),    # bottom row
    np.array([[0,1,2],[0,0,0]]),    # left column
    np.array([[0,1,2],[1,1,1]]),    # middle column
    np.array([[0,1,2],[2,2,2]]),    # right column
    np.array([[0,1,2],[0,1,2]]),    # top-left to bottom-right diag
    np.array([[0,1,2],[2,1,0]]),    # top-right to bottom-left diag
]