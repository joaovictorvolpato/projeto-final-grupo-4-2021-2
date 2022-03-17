from dao import DAO


class LevelDao(DAO):
    def __init__(self, level: int):
        super().__init__('levels.json')
        self._level = level

    def get(self, key):
        for i in self.object_cache:
            if i['level'] == self._level:
                return i[key]
