from abc_event_object import EventObject
from abc_request_object import AbcRequestObject


class Key(EventObject):
    def __init__(self, initial_x: int, initial_y: int, size: int, next_level: int, sprite: str):
        super().__init__(initial_x, initial_y, size, sprite)
        self._next_level = next_level

    def trigger_event(self):
        return {'change-lv': self._next_level}

    # def use_request(self, requested: list):
    #     return super().use_request(requested)

    # def request_to_gs(self):
    #     if self._change_level == True:
    #         return {'change-lv': self._next_level}
    #         self._change_level = False
    #     return {}
