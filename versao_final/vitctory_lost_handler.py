from game_state import GameState

class VictoryLostHandler:
        def __init__(self):
            self.__game_state = GameState(1)

        def check_situation(self):
            if self.__game_state.next_state != None:
                return self.__game_state.next_state
