from re import I, X
import pygame
import copy
import random
from abc_kinetic_object import Kinetic_object

COLIDED = pygame.USEREVENT + 1
COLIDED_BOTTOM = pygame.USEREVENT + 2
COLIDED_TOP = pygame.USEREVENT + 3
COLIDED_LEFT = pygame.USEREVENT + 4
COLIDED_RIGHT = pygame.USEREVENT + 5


class Enemy(Kinetic_object):
    def __init__(self, initial_x: int, initial_y: int, size: int,speed:int, dano:int):
        super().__init__(initial_x, initial_y, size,speed)
        self.__dano = dano
        self.__x = initial_x
        self.__y = initial_y
        self.__size = size
        self.__color = (255, 0,0)
        self.__speedx = speed
        self.__speedy = speed
        self.__rect = pygame.Rect(self.__x, self.__y, size, size)


    def draw(self, win, offset):
        fake_rect = copy.deepcopy(self.__rect)
        fake_rect.topleft -= offset
        pygame.draw.rect(win, self.__color, fake_rect)
    
    def check_colisions(self, obstacles: list):
        for obstacle in obstacles:
            colison_tolerance = 10
            if self.__rect.colliderect(obstacle.rect):
                pygame.event.post(pygame.event.Event(COLIDED))
                if abs(self.__rect.top - obstacle.rect.bottom) < colison_tolerance:
                    self.__speedy *= -1
                    pygame.event.post(pygame.event.Event(COLIDED_TOP))
                if abs(self.__rect.bottom - obstacle.rect.top) < colison_tolerance:
                    self.__speedy *= -1
                    pygame.event.post(pygame.event.Event(COLIDED_BOTTOM))
                if abs(self.__rect.right - obstacle.rect.left) < colison_tolerance:
                    self.__speedx *= -1
                    pygame.event.post(pygame.event.Event(COLIDED_RIGHT))
                if abs(self.__rect.left - obstacle.rect.right) < colison_tolerance:
                    self.__speedx *= -1
                    pygame.event.post(pygame.event.Event(COLIDED_LEFT))

        '''def get_hit_list(obstacles):
            hit = []
            for obstacle in obstacles:
                if self.__rect.colliderect(obstacle.rect):
                    hit.append(obstacle)
            return hit
    
        hits = get_hit_list(obstacles)
        if len(hits) != 0:
            OBSTACLE = hits[0].rect
            ENEMY = self.__rect
            COLLISION_TOLLERANCE = 10
            COLLISION_BOTTOM = abs(OBSTACLE.top - ENEMY.bottom)
            COLLISION_UP = abs(OBSTACLE.bottom - ENEMY.top)
            COLLISION_LEFT = abs(OBSTACLE.right - ENEMY.left) 
            COLLISION_RIGHT = abs(OBSTACLE.left - ENEMY.right)
            if COLLISION_UP < COLLISION_TOLLERANCE:
                self.__y += COLLISION_UP
            if COLLISION_BOTTOM < COLLISION_TOLLERANCE:
                self.__y -= COLLISION_BOTTOM
            if COLLISION_RIGHT < COLLISION_TOLLERANCE:
                self.__x -= COLLISION_RIGHT
            if COLLISION_LEFT < COLLISION_TOLLERANCE:
                self.__x += COLLISION_LEFT
            return True
        return False'''


    def update(self):
        self.__y += self.__speedy
        self.__x += self.__speedx
        '''for event in pygame.event.get():
            if event.type == COLIDED_TOP:
                self.__speedy *= -1'''


        self.__rect = pygame.Rect(int(self.__x), int(self.__y), self.__size, self.__size)
