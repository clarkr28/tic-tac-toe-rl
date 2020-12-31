from player_base import PlayerBase


class PlayerTerminal(PlayerBase):

    '''
    prompt the user to pick their next move by printing the board to the 
    terminal and prompting for their selection
    arguments:
        board: Board - the tic tac toe board
        marker: string - the marker that is assigned to you
    return: (row, col) tuple where row and col are ints of either 0, 1 or 2
    '''
    def pick_move(self, board, marker):
        board.print()
        valid = False
        while not valid:
            move = input(f'You are {marker}, pick your move: ')
            if len(move) == 2:
                if move[0] in 'abcABC' and move[1] in '123':
                    valid = True
        row = ord(move[0].upper()) - ord('A')
        col = int(move[1]) - 1
        return (row, col) 