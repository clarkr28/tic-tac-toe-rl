from constants import CELL_EMPTY, CELL_PLAYER_1, CELL_PLAYER_2

# Class to store game state and manage the flow of the game
class GameCore:

    # save the players and make an empty board
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = Board()
        self.winner = False 
        self.winning_player = None
        self.player_1_turn = True       # start with player 1 going first

    # exists for basic testing and should be deleted soon
    def dummy_testing(self):
        self.board.board[0][0] = CELL_PLAYER_1
        self.board.board[0][1] = CELL_PLAYER_1
        self.board.board[0][2] = CELL_PLAYER_1
        self.board.print()
        print('winner? ', self.board.winner_check(), '\n')
        self.board.board[0][2] = CELL_PLAYER_2
        self.board.board[1][1] = CELL_PLAYER_2
        self.board.print()
        print('winner? ', self.board.winner_check(), '\n')
        self.board.board[2][0] = CELL_PLAYER_2
        self.board.print()
        print('winner? ', self.board.winner_check(), '\n')
        self.board.board[2][0] = CELL_PLAYER_1
        self.board.print()
        print('winner? ', self.board.winner_check(), '\n')
        self.board.board[1][0] = CELL_PLAYER_1
        self.board.print()
        print('winner? ', self.board.winner_check(), '\n')
        print('empty spaces?', self.board.empty_spaces())
        self.board.board[1][2] = CELL_PLAYER_2
        self.board.board[2][2] = CELL_PLAYER_2
        self.board.board[2][1] = CELL_PLAYER_2
        self.board.print()
        print('winner? ', self.board.winner_check(), '\n')
        print('empty spaces?', self.board.empty_spaces())

    # run the game
    def run(self):
        current_player = None
        current_marker = None
        move = None
        winner_check = None

        while not self.winner and self.board.empty_spaces():
            # get the current player and current marker for this turn
            current_player = self.player_1 if self.player_1_turn else self.player_2
            current_marker = CELL_PLAYER_1 if self.player_1_turn else CELL_PLAYER_2

            # get the next move from the player and keep asking until they pick a spot that
            # has not yet been taken
            while True:
                move = current_player.pick_move(self.board, current_marker)
                if self.board.get_cell(*move) == CELL_EMPTY:
                    self.board.set_cell(move[0], move[1], current_marker)
                    break

            winner_check = self.board.winner_check()
            if winner_check[0]:
                self.winner = True
                self.winning_player = winner_check[1]

            # toggle whose turn it is for the next round
            self.player_1_turn = not self.player_1_turn

        if self.winner:
            winning_marker = CELL_PLAYER_1 if self.winning_player == 1 else CELL_PLAYER_2
            print(f'Player {self.winning_player} ({winning_marker}) wins!')
        else:
            print('draw')



# class to hold the board and provide helpful methods specific to the board
class Board:
    def __init__(self):
        self.board = self.make_empty_board()

    # create a new, empty board
    def make_empty_board(self):
        board = list()
        board.append([CELL_EMPTY, CELL_EMPTY, CELL_EMPTY])
        board.append([CELL_EMPTY, CELL_EMPTY, CELL_EMPTY])
        board.append([CELL_EMPTY, CELL_EMPTY, CELL_EMPTY])
        return board

    def get_cell(self, row, col):
        return self.board[row][col]

    def set_cell(self, row, col, marker):
        self.board[row][col] = marker

    def print(self):
        print('  1 2 3')
        row_headers = ['A', 'B', 'C']
        for row, header in zip(self.board, row_headers):
            print(header + ' ' + ' '.join(row))

    '''
    determine if a player has 3 in a row somewhere on the board
    return: (winner_exists, winner_number) where winner_exists is a boolean and
            winner_number is the number (1 or 2) of the player who won. winner_number
            only exists if there is a winner
    '''
    def winner_check(self):
        # check top row
        if (self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] != CELL_EMPTY):
            winner = 1 if self.board[0][0] == CELL_PLAYER_1 else 2
            return (True, winner)
        # check middle row
        if (self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] != CELL_EMPTY):
            winner = 1 if self.board[1][0] == CELL_PLAYER_1 else 2
            return (True, winner)
        # check bottom row
        if (self.board[2][0] == self.board[2][1] == self.board[2][2] and self.board[2][0] != CELL_EMPTY):
            winner = 1 if self.board[2][0] == CELL_PLAYER_1 else 2
            return (True, winner)
        # check left column
        if (self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] != CELL_EMPTY):
            winner = 1 if self.board[0][0] == CELL_PLAYER_1 else 2
            return (True, winner)
        # check middle column
        if (self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] != CELL_EMPTY):
            winner = 1 if self.board[0][1] == CELL_PLAYER_1 else 2
            return (True, winner)
        # check right column
        if (self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] != CELL_EMPTY):
            winner = 1 if self.board[0][2] == CELL_PLAYER_1 else 2
            return (True, winner)
        # check top-left to bottom-right diag
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != CELL_EMPTY):
            winner = 1 if self.board[0][0] == CELL_PLAYER_1 else 2
            return (True, winner)
        # check bottom-left to top-right diag
        if (self.board[2][0] == self.board[1][1] == self.board[0][2] and self.board[0][2] != CELL_EMPTY):
            winner = 1 if self.board[0][2] == CELL_PLAYER_1 else 2
            return (True, winner)
        # nobody won
        return (False,)
            
    '''
    determine if there are still empty spaces that can be played on
    return: boolean - true if there are still unoccupied spaces
    '''
    def empty_spaces(self):
        for row in self.board:
            for elem in row:
                if elem == CELL_EMPTY:
                    return True
        return False