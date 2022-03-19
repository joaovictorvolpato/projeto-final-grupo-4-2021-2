from game_state import GameState


class InteractionHandler:
    def __init__(self):
        self.__game_state = GameState(1)

    def handle_interaction(self):
        for i in self.__game_state.interactables:
            self.__check_colision(self.__game_state.player, i)

    def __check_colision(self, player, interactable_obj):
        if player.rect.colliderect(interactable_obj.rect):
            actions = interactable_obj.on_contact()
            if not actions is None:
                self.__exec_action(actions)

    def __exec_action(self, actions: dict):
        for name, value in actions.items():
            if name == 'hit':
                if self.__game_state.player.hit_stun <= 0:
                    self.__deal_player_dmg(value)
                    self.__game_state.player.hit_stun = 40
            elif name == 'slow':
                self.__slow_player_down(value)
            elif name == 'heal':
                self.__heal_player(value)

    def __deal_player_dmg(self, value):
        if self.__game_state.player.hit_stun <= 0:
            self.__game_state.player.current_health -= value
            if self.__game_state.player.current_health == 0:
                self.__game_state.next_state = ['menu', 'lost']

    def __slow_player_down(self, value):
        self.__game_state.player.freezed = value

    def __heal_player(self, value):
        self.__game_state.player.current_health
        self.__game_state.player.current_health += value
        MAX_HEALTH = self.__game_state.player.max_health
        if self.__game_state.player.current_health > MAX_HEALTH:
            self.__game_state.player.current_health = MAX_HEALTH
