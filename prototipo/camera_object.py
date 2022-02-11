import pygame
class Camera_object:
    def __init__(self, real_object):
        self.__rect = pygame.Rect(real_object.x , real_object.y, real_object.size, real_object.size)
        self.__offset = pygame.math.Vector2()
        self.__color = real_object.color
    
    def draw(self, win, player):
        self.__offset.x = player.rect.centerx - win.get_size()[0] / 2
        print(self.__offset)
        self.__offset.y = player.rect.centery - win.get_size()[1] / 2
        self.__rect.topleft -= self.__offset
        pygame.draw.rect(win, self.__color, self.__rect)

    def update(self, real_object):
        self.__rect = pygame.Rect(int(real_object.x), int(real_object.y), real_object.size, real_object.size)
        