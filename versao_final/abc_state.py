from abc import ABC, abstractmethod


class AbcState(ABC):
    def __init__(self, name):
        self._name = name
        self._next_state = None

    @property
    def name(self):
        return self._name

    @property
    def next_state(self):
        return self._next_state

    @abstractmethod
    def state_routine(self):
        pass
