from abc_event_object import Event_object
import copy
import pygame

class Key(Event_object):
    def __init__(self, initial_x: int, initial_y: int, size: int, next_level: int):
        super().__init__(initial_x, initial_y, size)
        self.__next_level = next_level
        self.__color = (255, 255, 0)

    def check_player_collisions(self, player):
        if self.rect.colliderect(player.rect):
            return self.trigger_event()

    def trigger_event(self):
        return self.__next_level

    def draw(self, win, offset):
        fake_rect = copy.deepcopy(self.rect)
        fake_rect.topleft -= offset
        pygame.draw.rect(win, self.__color, fake_rect)
