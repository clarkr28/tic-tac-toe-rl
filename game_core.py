import numpy as np
from constants import CELL_EMPTY, CELL_PLAYER_1, CELL_PLAYER_2, WIN_OPTIONS_NP


# Class to store game state and manage the flow of the game
class GameCore:

    # save the players and make an empty board
    def __init__(self, player_1, player_2, print_result):
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = Board()
        self.winner = False 
        self.winning_player = None
        self.player_1_turn = True       # start with player 1 going first
        self.print_result = print_result

    # run the game
    def run(self):
        current_player = None
        current_marker = None
        move = None
        winner_check = None

        while not self.winner and self.board.empty_spaces():
            # get the current player and current marker for this turn
            current_player = self.player_1 if self.player_1_turn else self.player_2
            current_marker = 1 if self.player_1_turn else 2

            # get the next move from the player and keep asking until they pick a spot that
            # has not yet been taken
            while True:
                move = current_player.pick_move(self.board, current_marker)
                if self.board.get_cell(*move) == CELL_EMPTY:
                    self.board.set_cell(move[0], move[1], current_marker)
                    break

            # used primarily for the reward processing of the RL player
            current_player.post_move(self.board, current_marker)

            winner_check = self.board.winner_check()
            if winner_check[0]:
                self.winner = True
                self.winning_player = winner_check[1]

            # toggle whose turn it is for the next round
            self.player_1_turn = not self.player_1_turn

        # print the board at the end of the game
        if self.print_result:
            self.board.print()
            if self.winner:
                winning_marker = CELL_PLAYER_1 if self.winning_player == 1 else CELL_PLAYER_2
                print(f'Player {self.winning_player} ({winning_marker}) wins!')
            else:
                print('draw')



# class to hold the board and provide helpful methods specific to the board
class Board:
    def __init__(self):
        self.board = self.make_empty_board()
        self.history = []

    # create a new, empty board
    def make_empty_board(self):
        return np.zeros((3,3), dtype=int)

    def get_cell(self, row, col):
        return self.board[row,col]

    def set_cell(self, row, col, marker):
        self.board[row,col] = marker
        self.history.append([self.quantify(), [row, col]])

    def print(self):
        print('  1 2 3')
        row_headers = ['A', 'B', 'C']
        for row, header in enumerate(row_headers):
            print(header + ' ', end='')
            for col in range(3):
                if self.board[row,col] == 0:
                    print(CELL_EMPTY, end='')
                elif self.board[row,col] == 1:
                    print(CELL_PLAYER_1, end='')
                else:
                    print(CELL_PLAYER_2, end='')
            print()


    '''
    return: (int) length of history
    '''
    def history_length(self):
        return len(self.history)

    def get_history_at_index(self, index):
        return self.history[index]

    '''
    quantify the state of board - return an integer unique to the state
    of the board and which marker is for the current player
    param: curr_marker (int) the marker in the board for the current player
    return: int 
    '''
    def quantify(self, curr_marker):
        # convert the board into a 9 digit base 3 number that represents the 
        # 9 cells of the board 
        flat_board = self.board.reshape(9)
        multiplier = 1
        cell_value = None
        total = 0
        for i in range(9):
            if flat_board[i] == 0:
                cell_value = 0
            elif flat_board[i] == curr_marker:
                cell_value = 1
            else:
                cell_value = 2
            total += cell_value * multiplier
            multiplier *= 3
        return total


    '''
    determine if a player has 3 in a row somewhere on the board
    return: (winner_exists, winner_number) where winner_exists is a boolean and
            winner_number is the number (1 or 2) of the player who won. winner_number
            only exists if there is a winner
    '''
    def winner_check(self):
        for inds in WIN_OPTIONS_NP:
            if np.all(self.board[inds[0],inds[1]] == 1):
                return (True, 1)    # player 1 won
            elif np.all(self.board[inds[0],inds[1]] == 2):
                return (True, 2)    # player 2 won
        # nobody won
        return (False,)
            
    '''
    determine if there are still empty spaces that can be played on
    return: boolean - true if there are still unoccupied spaces
    '''
    def empty_spaces(self):
        return np.any(self.board == 0)