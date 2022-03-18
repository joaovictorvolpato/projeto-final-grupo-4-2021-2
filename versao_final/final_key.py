from abc_event_object import EventObject
from abc_request_object import AbcRequestObject



class FinalKey(EventObject, AbcRequestObject):
    def __init__(self, initial_x: int, initial_y: int, size: int):
        super().__init__(initial_x, initial_y, size, 'sprites/placeholder.png')
        self._request = []
        self._change_level = False
        self._won_game = False

    def trigger_event(self):
        self._won_game = True

    def use_request(self, requested: list):
        return super().use_request(requested)

    def request_to_gs(self):
        if self._won_game == True:
            return {'won-game': self._won_game}

    @property
    def won_game(self):
        return self.__won_game
