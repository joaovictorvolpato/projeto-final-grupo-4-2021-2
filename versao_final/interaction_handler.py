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
            self.__exec_action(actions)

    def __exec_action(self, actions: dict):
        for name, value in actions.items():
            if name == 'hit':
                if self.__game_state.player.hit_stun <= 0:
                    self.__deal_player_dmg(value)
                    self.__knockback(value)
                    self.__game_state.player.hit_stun = 40
            elif name == 'slow':
                self.__slow_player_down(value)

    def __knockback(self, value):
        # arrumar dps
        vel = (self.__game_state.player.velX, self.__game_state.player.velY)
        formula = 1 + value/20
        knockback_force = (vel[0] * formula, vel[1] * formula)
        self.__game_state.player.rect.x += knockback_force[0]
        self.__game_state.player.rect.y += knockback_force[1]

    def __deal_player_dmg(self, value):
        if self.__game_state.player.hit_stun <= 0:
            self.__game_state.player.current_health -= value

    def __slow_player_down(self, value):
        self.__game_state.player.freezed = value
