from game_state import Game_state
import pygame

# dividir em duas classes depois ? SRP


class Movement_handler:
    def __init__(self):
        self.__game_state = Game_state()

    def move(self):
        for i in self.__game_state.kinetic_objects:
            self.__handle_movement(i, i.move_request())

    def __handle_movement(self, game_obj, mov_req):
        X = mov_req[0]
        Y = mov_req[1]
        game_obj.rect.x += X
        self.__handle_collision(game_obj, 'horizontal', X, Y)
        game_obj.rect.y += Y
        self.__handle_collision(game_obj, 'vertical', X, Y)

    def __handle_collision(self, game_obj, direction, X, Y):
        if direction == 'horizontal':
            for obstacle in self.__game_state.obstacles:
                if obstacle.rect.colliderect(game_obj.rect):
                    # avisa objeto que acabou de colidir
                    game_obj.handle_collision('horizontal')

                    if X > 0:  # direita
                        game_obj.rect.right = obstacle.rect.left
                    elif X < 0:  # esquerda
                        game_obj.rect.left = obstacle.rect.right

        if direction == 'vertical':
            for obstacle in self.__game_state.obstacles:
                if obstacle.rect.colliderect(game_obj.rect):
                    # avisa objeto que acabou de colidir
                    game_obj.handle_collision('vertical')

                    if Y > 0:  # baixo
                        game_obj.rect.bottom = obstacle.rect.top
                    elif Y < 0:  # cima
                        game_obj.rect.top = obstacle.rect.bottom
