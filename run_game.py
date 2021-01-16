import argparse
from game_core import GameCore
from player_terminal import PlayerTerminal
from player_rule import PlayerRule
from player_random import PlayerRandom
from player_rl import PlayerRL


PLAYER_TERMINAL_KEY = 'terminal'
PLAYER_RULE_KEY = 'rule'
PLAYER_RANDOM_KEY = 'random'
PLAYER_RL_KEY = 'rl'
VALID_PLAYERS = [PLAYER_TERMINAL_KEY, PLAYER_RULE_KEY, PLAYER_RANDOM_KEY, PLAYER_RL_KEY] 



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
    parser.add_argument('-r', '--rounds', type=int, default=1, 
        help='number of rounds to play (int). Default is 1. ' + 
            'Log will not be saved if default is used.')
    parser.add_argument('-l', '--learn', action='store_true',
        help='indicate if the RL agent should learn')
    parser.add_argument('-e', '--explore', type=float, default=0.2,
        help='explore parameter for the RL agent')
    return parser.parse_args()



'''
params:
    player_type: (string) the player type to create
    args: argparse params that can be passed to players
return the proper player type based on the passed string
'''
def create_player(player_type, args):
    if player_type == PLAYER_TERMINAL_KEY:
        return PlayerTerminal()
    elif player_type == PLAYER_RULE_KEY:
        return PlayerRule()
    elif player_type == PLAYER_RANDOM_KEY:
        return PlayerRandom()
    elif player_type == PLAYER_RL_KEY:
        return PlayerRL(args.learn, args.explore)
    raise ValueError(f'player_type of value "{player_type}" is not supported')



if __name__ == '__main__':
    args = get_args()
    player_1 = None
    player_2 = None
    if args.p1 == args.p2:
        # use the same player instance if they are the same type
        player_1 = create_player(args.p1, args)
        player_2 = player_1 
    else:
        player_1 = create_player(args.p1, args)
        player_2 = create_player(args.p2, args)
    
    # TODO add loading of existing Q function
    
    game = None
    for i in range(args.rounds):
        game = GameCore(player_1, player_2)
        game.run()

    # TODO log arguments (pickle)
    # TODO add saving of Q function
