from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, commands):
        self._commands = commands

    @property
    def commands(self):
        return self._commands

    def change_commands(self, command_changes):
        if isinstance(command_changes, dict):
            for key, value in command_changes.items():
                if key in self._commands.keys():
                    self._commands[key] = value

    @abstractmethod
    def execute_commands(self):
        pass
