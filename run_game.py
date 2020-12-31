from game_core import GameCore
from player_terminal import PlayerTerminal

if __name__ == '__main__':
    player_1 = PlayerTerminal()
    player_2 = PlayerTerminal()
    game = GameCore(player_1, player_2)
    game.run()