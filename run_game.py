import argparse
from game_core import GameCore
from player_terminal import PlayerTerminal
from player_rule import PlayerRule
from player_random import PlayerRandom


PLAYER_TERMINAL_KEY = 'terminal'
PLAYER_RULE_KEY = 'rule'
PLAYER_RANDOM_KEY = 'random'
VALID_PLAYERS = [PLAYER_TERMINAL_KEY, PLAYER_RULE_KEY, PLAYER_RANDOM_KEY]



'''
setup and call an argparse object. 
return: args object from evaluating an argparse object (parse_args())
'''
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p1', required=True, choices=VALID_PLAYERS,
        help='The type of player to set as player 1')
    parser.add_argument('-p2', required=True, choices=VALID_PLAYERS,
        help='The type of player to set as player 2')
    return parser.parse_args()



'''
return the proper player type based on the passed string
'''
def create_player(player_type):
    if player_type == PLAYER_TERMINAL_KEY:
        return PlayerTerminal()
    elif player_type == PLAYER_RULE_KEY:
        return PlayerRule()
    elif player_type == PLAYER_RANDOM_KEY:
        return PlayerRandom()
    raise ValueError(f'player_type of value "{player_type}" is not supported')



if __name__ == '__main__':
    args = get_args()
    player_1 = create_player(args.p1)
    player_2 = create_player(args.p2)
    game = GameCore(player_1, player_2)
    game.run()
