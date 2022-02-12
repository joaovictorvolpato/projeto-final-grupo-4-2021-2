import pygame, sys
import math
import copy
from abc_command_object import Command_object
from abc_kinetic_object import Kinetic_object
class Player(Kinetic_object, Command_object):
    def __init__(self, initial_x: int, initial_y: int, size: int, speed: int):
        super().__init__(initial_x, initial_y, size, speed)
        #sprites
        self.__x = initial_x
        self.__y = initial_y
        self.__size = size
        self.__color = (250, 160, 60)
        self.__speed = speed
        self.__commands = {'up': False, 'down': False, 'right': False, 'left': False}
        self.__rect = pygame.Rect(self.__x, self.__y, size, size)
        self.__velX = 0
        self.__velY = 0

    @property
    def rect(self):
        return self.__rect
    
    @property
    def velX(self):
        return self.__velX
    
    @property
    def velY(self):
        return self.__velY
    
    @property
    def commands(self):
        return self.__commands

    @property
    def size(self):
        return self.__size

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def color(self):
        return self.__color


    @commands.setter
    def commands(self, new_commands: dict):
        self.__commands = new_commands
    
    # usar para normalizar os vetores de velocidade, caso contrario, anda mais rápido nas diagonais
    def normalize(self):
        if self.__velX != 0 and self.__velY != 0:
            self.__velX *=  1/math.sqrt(2)
            self.__velY *= 1/math.sqrt(2)
    
    # desenha um retangulo com offset para cameta
    def draw(self, win, offset):
        fake_rect = copy.deepcopy(self.__rect)
        fake_rect.topleft -= offset
        pygame.draw.rect(win, self.__color, fake_rect)
    # faz a logica das colisoes e retorna uma bool pra caso houve colisao
    def check_collisions(self, obstacles: list):
        def get_hit_list(obstacles):
            hit = []
            for obstacle in obstacles:
                if self.__rect.colliderect(obstacle.rect):
                    hit.append(obstacle)
            return hit
    
        hits = get_hit_list(obstacles)
        if len(hits) != 0:
            OBSTACLE = hits[0].rect
            PLAYER = self.__rect
            COLLISION_TOLLERANCE = 10
            COLLISION_BOTTOM = abs(OBSTACLE.top - PLAYER.bottom)
            COLLISION_UP = abs(OBSTACLE.bottom - PLAYER.top)
            COLLISION_LEFT = abs(OBSTACLE.right - PLAYER.left) 
            COLLISION_RIGHT = abs(OBSTACLE.left - PLAYER.right)
            if COLLISION_UP < COLLISION_TOLLERANCE:
                self.__y += COLLISION_UP
            if COLLISION_BOTTOM < COLLISION_TOLLERANCE:
                self.__y -= COLLISION_BOTTOM
            if COLLISION_RIGHT < COLLISION_TOLLERANCE:
                self.__x -= COLLISION_RIGHT
            if COLLISION_LEFT < COLLISION_TOLLERANCE:
                self.__x += COLLISION_LEFT
            return True
        return False

    def execute_commands(self):
        self.__velX = 0
        self.__velY = 0
        if self.__commands['left'] and not self.__commands['right']:
            self.__velX = -self.__speed
        if self.__commands['right'] and not self.__commands['left']:
            self.__velX = self.__speed
        if self.__commands['up'] and not self.__commands['down']:
            self.__velY = -self.__speed
        if self.__commands['down'] and not self.__commands['up']:
            self.__velY = self.__speed
        
        self.normalize()
        self.__x += self.__velX
        self.__y += self.__velY 

    def update(self):
        self.__rect = pygame.Rect(int(self.__x), int(self.__y), self.__size, self.__size)

    


