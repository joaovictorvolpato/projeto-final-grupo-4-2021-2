
from turtle import st
import pygame
import os
from system import System

system = System(600, 'teste', 60)

pygame.font.init()
pygame.init()
mainClock = pygame.time.Clock()

WIDTH = 700
HEIGHT = 700
res = (700,700)
WHITE = (255, 255, 255)
MENU_COLOR = (100, 100, 100)
BLACK = (0, 0, 0)
BTN_UNCLICKED_COLOR = (200,200,200)
BTN_CLICKED_COLOR = (150,150,150)

screen_menu = pygame.display.set_mode(res)
pygame.display.set_caption("MENU")

FONT = pygame.font.SysFont(None, 40)

START_BTN_IMG = pygame.image.load(os.path.join("sprites", "start.png"))
START_BTN_IMG1 = pygame.transform.scale(START_BTN_IMG, (100, 40))
QUIT_BTN_IMG = pygame.image.load(os.path.join("sprites", "exit.png"))
QUIT_BTN_IMG1 = pygame.transform.scale(QUIT_BTN_IMG,(100,40))

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw_button(self):
        screen_menu.blit(self.image, (self.rect.x, self.rect.y))




def draw_text(text, color, x, y):
    text_to_draw = FONT.render(text, 1, color)
    text_rect = text_to_draw.get_rect()
    text_rect.topleft = (x, y)
    screen_menu.blit(text_to_draw, text_rect)



def main_menu():


    while True:
        screen_menu.fill(MENU_COLOR)

        draw_text("MAIN MENU", WHITE, 20, 20)


        start_button = Button(WIDTH/2,HEIGHT/2, START_BTN_IMG1)
        exit_button = Button(WIDTH/2,HEIGHT/2+100, QUIT_BTN_IMG1)

        start_button.draw_button()
        exit_button.draw_button()


        mx, my = pygame.mouse.get_pos()
        
        if start_button.rect.collidepoint(mx, my):
            if click:
                system.initialize()

        if exit_button.rect.collidepoint(mx, my):
            if click:
                pygame.quit()

        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        pygame.display.update()
        mainClock.tick(60)
        

main_menu()

    
    

    

