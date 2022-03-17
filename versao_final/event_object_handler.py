from game_state import GameState


class EventObjectHandler:
    def __init__(self):
        self.__game_state = GameState(1)

    def handle_events(self):
        for i in self.__game_state.event_objects:
            self.__check_radius(self.__game_state.player, i)

    def __check_radius(self, player, obj):
        # dentro do raio
        # rectx e y dao q posicao do canto superior esquerdo dos obj, por isso o ajuste
        OBJ_X_IN_RADIUS = abs(
            player.rect.x + player.size/2 - (obj.rect.x + obj.size/2)) <= player.interactable_radius
        OBJ_Y_IN_RADIUS = abs(
            player.rect.y + player.size/2 - (obj.rect.y + obj.size/2)) <= player.interactable_radius

        if OBJ_X_IN_RADIUS and OBJ_Y_IN_RADIUS and player.is_interacting:
            obj.trigger_event()
