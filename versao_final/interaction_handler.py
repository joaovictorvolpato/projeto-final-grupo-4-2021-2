from game_state import GameState


class InteractionHandler:
    def __init__(self):
        self.__game_state = GameState(1)

    def handle_interaction(self):
        for i in self.__game_state.interactables:
            self.__check_colision(self.__game_state.player, i)

    def __check_colision(self, player, interactable_obj):
        if player.rect.colliderect(interactable_obj.rect):
            interactable_obj.on_contact()

    # def __give_hit(self, dano):
    #     self.__game_state.player.health -= dano
    #     print(self.__game_state.player.health)
