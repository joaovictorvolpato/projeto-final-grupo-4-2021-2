from abc_event_object import EventObject


class Key(EventObject):
    def __init__(self, initial_x: int, initial_y: int, size: int, next_level: int, sprite: str):
        super().__init__(initial_x, initial_y, size, sprite)
        self._next_level = next_level

    def trigger_event(self):
        return {'change-lv': self._next_level}
