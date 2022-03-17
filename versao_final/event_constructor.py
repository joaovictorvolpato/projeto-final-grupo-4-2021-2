from abc_constructor import Constructor
from key import Key


class EventConstructor(Constructor):
    def __init__(self):
        super().__init__(['1', '2'], ['object', 'event'])

    def instantiate(self, x, y, tag):
        self.__init__()
        SIZE = self._config.get('tile-size')
        if tag.isdecimal():
            key = Key(x*SIZE, y*SIZE, SIZE, int(tag))
            self._lists.append('obstacle')
            self._lists.append('request')
            return key
