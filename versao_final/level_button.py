from os.path import join
import pygame


class LevelButton:
    """
    Represents a button on the level selection menu.
    """
    def __init__(
            self,
            level_number: int,
            x: int,
            y: int):
        self.__destination = "level_" + str(level_number)
        
        image_filename = self.__destination + "_selection_button.png"
        image_path = join("images", image_filename)
        self.__img = pygame.image.load(image_path)
        
        self.__rect = self.__img.get_rect()
        self.__rect.topleft = (x, y)

    @property
    def destination(self):
        return self.__destination

    @property
    def img(self):
        return self.__img

    @property
    def rect(self):
        return self.__rect

