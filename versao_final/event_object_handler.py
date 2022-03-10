from game_state import Game_state


class Event_object_handler:
    def __init__(self):
        self.__game_state = Game_state(1)

    def handle_interactions(self):
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
            event = obj.trigger_event()
            # dessa forma, objetos que mudam o game_state não precisam de um game_state
            # mudar para outra classe dps ?
            if isinstance(event, int):
                self.__game_state.change_level(event)
