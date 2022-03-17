from dao import DAO


class ConfigDao(DAO):
    def __init__(self):
        super().__init__('config.json')

    def get(self, key):
        return self._object_cache[key]
