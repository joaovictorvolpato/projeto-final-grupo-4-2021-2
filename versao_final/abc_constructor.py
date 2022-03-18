from abc import ABC, abstractmethod
from config_dao import ConfigDao


class Constructor(ABC):
    def __init__(self, tags: list, lists: list, lv: str):
        self._config = ConfigDao()
        self._tags = tags
        # fala em qual lista ele devera ser colocado
        self._lists = lists
        self._level = lv

    @property
    def tags(self):
        return self._tags

    @property
    def lists(self):
        return self._lists

    @abstractmethod
    def instantiate(self, x, y, tag):
        pass
