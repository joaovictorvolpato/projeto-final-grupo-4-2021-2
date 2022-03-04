import json
from abc import ABC


class DAO(ABC):
    def __init__(self, datasource):
        self._datasource = datasource
        self._object_cache = {}
        try:
            self._load()
        except FileNotFoundError:
            print('db vazia')

    @property
    def datasource(self):
        return self._datasource

    @property
    def object_cache(self):
        return self._object_cache

    def _load(self):
        file = open(self._datasource)
        self._object_cache = json.load(file)
        file.close()

    def get(self, key):
        try:
            return self._object_cache[key]

        except KeyError:
            print('Chave não disponível')
