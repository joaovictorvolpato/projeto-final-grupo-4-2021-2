from abc_menu import AbcMenu
import pygame
from game_controller import Game_controller
import sys
# fazer menu rendered dps
# fazer eventhandler para menus


class MainMenu(AbcMenu):
    def __init__(self, screen_size: int):
        super().__init__(screen_size,
                         {'start': pygame.Rect(50, 100, 200, 50),
                          'options': pygame.Rect(50, 200, 200, 50)})
        self.__game_controller = Game_controller(screen_size)
        self._font = pygame.font.SysFont('arial', 20)

    def execute_menu_routine(self):
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        self._win.fill((0, 0, 0))
        self._draw_text('main menu', (255, 255, 255), 20, 20)

        mx, my = pygame.mouse.get_pos()

        if self._buttons['start'].collidepoint((mx, my)):
            if click:
                self.__game_controller.game_loop()

        if self._buttons['options'].collidepoint((mx, my)):
            if click:
                print('clickou em options')

        pygame.draw.rect(self._win, (255, 0, 0), self._buttons['start'])
        pygame.draw.rect(self._win, (255, 0, 0), self._buttons['options'])
