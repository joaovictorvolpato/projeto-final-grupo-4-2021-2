from abc_event_object import EventObject
from abc_request_object import AbcRequestObject


class FinalKey(EventObject):
    def __init__(self, initial_x: int, initial_y: int, size: int):
        super().__init__(initial_x, initial_y, size, 'sprites/fk.png')

    def trigger_event(self):
        return {'change_state': 'win'}
