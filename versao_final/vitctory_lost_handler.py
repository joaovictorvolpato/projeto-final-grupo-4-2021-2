from game_state import GameState

class VictoryLostHandler:
        def __init__(self):
            self.__game_state = GameState(1)

        def check_if_won(self):
            if self.__game_state.player.has_won == True:
                return True

        def check_if_lost(self):
            if self.__game_state.player.has_lost == True:
                return True
