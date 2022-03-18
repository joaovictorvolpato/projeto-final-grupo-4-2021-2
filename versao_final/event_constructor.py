from abc_constructor import Constructor
from key import Key
from final_key import FinalKey


class EventConstructor(Constructor):
    def __init__(self, level):
        super().__init__(['1', '2', '3', '4', 'fk'],
                         ['object', 'event'], level)

    def instantiate(self, x, y, tag):
        self.__init__(self._level)
        SIZE = self._config.get('tile-size')
        if tag.isdecimal():
            key = Key(x*SIZE, y*SIZE, SIZE, int(tag),
                      f'sprites/lv{self._level}_tiles/k.png')
            self._lists.append('obstacle')
            return key
        if tag == 'fk':
            final_key = FinalKey(x*SIZE, y*SIZE, SIZE)
            self._lists.append('obstacle')
            return final_key
