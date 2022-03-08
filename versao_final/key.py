from abc_event_object import Event_object


class Key(Event_object):
    def __init__(self, initial_x: int, initial_y: int, size: int, next_level: int):
        super().__init__(initial_x, initial_y, size, (255, 255, 0))
        self._next_level = next_level

    def check_player_collisions(self, player):
        if self.rect.colliderect(player.rect):
            return self.trigger_event()

    def trigger_event(self):
        return self._next_level
