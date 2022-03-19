from game_state import GameState


class RequestAnalyser:
    def __init__(self):
        self.__game_state = GameState(1)
        self.__gs_dict = {'obstacles': self.__game_state.obstacles,
                          'player': self.__game_state.player,
                          'interactables': self.__game_state.interactables,
                          'objects': self.__game_state.objects,
                          'kinetic_objects': self.__game_state.kinetic_objects,
                          'command_objects': self.__game_state.command_objects,
                          'event_objects': self.__game_state.event_objects,
                          'request_objects': self.__game_state.request_objects}

    @property
    def game_state(self):
        return self.__game_state

    def handle_requests(self):
        self.__update_dict()
        self.__handle_read()
        # self.__handle_write()

    def __handle_read(self):
        for obj in self.__game_state.request_objects:
            requests = []
            for list_name, list in self.__gs_dict.items():
                if list_name in obj.request:
                    requests.append(list)
            obj.use_request(requests)

    def __update_dict(self):
        self.__gs_dict = {'obstacles': self.__game_state.obstacles,
                          'player': self.__game_state.player,
                          'interactables': self.__game_state.interactables,
                          'objects': self.__game_state.objects,
                          'kinetic_objects': self.__game_state.kinetic_objects,
                          'command_objects': self.__game_state.command_objects,
                          'event_objects': self.__game_state.event_objects,
                          'request_objects': self.__game_state.request_objects}
