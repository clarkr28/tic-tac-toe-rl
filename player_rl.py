import copy
import random
import numpy as np
from game_core import Board
from player_base import PlayerBase
from constants import CELL_EMPTY, WIN_OPTIONS, CELL_PLAYER_1, CELL_PLAYER_2

Q_FNAME_KEY = 'q_fname'
LEARNING_RATE_KEY = 'learning_rate'
GAMMA_KEY = 'gamma_key'



'''
param:
    board (Board) the board to calculate a reward for
    marker (string) your marker on the board
return: (float) reward for the passed board
'''
def reward(board, marker):
    # constants used in this function
    win_reward = 100.0
    lose_reward = -100.0
    # determine what the marker of the opponent is
    opp_marker = CELL_PLAYER_2 if marker == CELL_PLAYER_1 else CELL_PLAYER_1
    reward = 0
    my_count = 0
    opp_count = 0
    for inds_1, inds_2, inds_3 in WIN_OPTIONS:
        my_count = 0
        opp_count = 0
        cell_values = list()
        cell_values.append(board.get_cell(*inds_1))
        cell_values.append(board.get_cell(*inds_2))
        cell_values.append(board.get_cell(*inds_3))
        for value in cell_values:
            if value == CELL_EMPTY:
                continue
            elif value == marker:
                my_count += 1
            elif value == opp_marker:
                opp_count += 1
        if opp_count == 3:
            # the opponent has won
            return lose_reward
        if my_count == 3:
            # you have won
            return win_reward
        reward += my_count**2
    return reward



class PlayerRL(PlayerBase):
    '''
    params: 
        learn: (bool) if true, update the Q function as the game is played
        explore: (float) probability of random exploration. 
    '''
    def __init__(self, learn, explore):
        self.learn = learn
        self.explore = explore
        self.q = np.zeros(3**9)
        self.lr = 0.01       # learning rate
        self.gamma = 0.9    # discount factor


    def save_to_log_obj(self, log_obj, fname):
        log_obj[LEARNING_RATE_KEY] = self.lr
        log_obj[GAMMA_KEY] = self.gamma
        # remove .json from fname and add .npz
        npz_file = fname.split('.')[0] + '.npz'
        log_obj[Q_FNAME_KEY] = npz_file
        np.savez(npz_file, q=self.q)


    def load_from_log_obj(self, log_obj):
        npz_fname = log_obj[Q_FNAME_KEY]
        with np.load(npz_fname) as npz_file:
            self.q = npz_file['q']


    '''
    if exploit mode - pick the move that should return the highest reward
    if explore mode - pick a random move
    '''
    def pick_move(self, board, marker):
        move = None # the move to return
        # get all remaining moves
        remaining_moves = []
        for row in range(3):
            for col in range(3):
                if board.get_cell(row, col) == CELL_EMPTY:
                    remaining_moves.append([row, col])
        if len(remaining_moves) == 0:
            raise ValueError('There are no remaining moves')

        if random.random() < self.explore:
            # explore mode - pick a random move
            move = remaining_moves[random.randint(0, len(remaining_moves) - 1)]
        else:
            # exploit mode
            temp_board = copy.deepcopy(board)
            expected_rewards = []
            for i in range(len(remaining_moves)):
                # see what the expected reward would be for each move
                row, col = remaining_moves[i]
                temp_board.set_cell(row, col, marker)
                quantified_state = temp_board.quantify(marker)
                expected_rewards.append(self.q[quantified_state])
                # undo the move on the board for the next iteration
                temp_board.set_cell(row, col, CELL_EMPTY)
            # pick the move with the highest expected reward
            best_move = [remaining_moves[0]]
            best_move_index = 0
            for i in range(1,len(remaining_moves)):
                if expected_rewards[i] == expected_rewards[best_move_index]:
                    best_move.append(remaining_moves[i])
                elif expected_rewards[i] > expected_rewards[best_move_index]:
                    best_move = [remaining_moves[i]]
                    best_move_index = i
            # if multiple with the same highest reward, pick one randomly
            if len(best_move) == 1:
                move = best_move[0]
            else:
                move = best_move[random.randint(0, len(best_move) - 1)]
        return move


    '''
    update q values
    '''
    # TODO: update to use a numpy based q function and new quantify function
    def post_move(self, board, marker):
        r = reward(board, marker)
        move_count = board.history_length()
        if move_count < 2:
            return
        previous_state = board.get_history_at_index(move_count - 2)
        quantified_state = previous_state[0]
        self.q[quantified_state] = self.q[quantified_state] + self.lr * (r + 
            self.gamma * self.q[board.quantify(marker)] - self.q[quantified_state])



if __name__ == '__main__':
    board = Board()
    print(f'Reward for empty board: {reward(board, CELL_PLAYER_1)}')