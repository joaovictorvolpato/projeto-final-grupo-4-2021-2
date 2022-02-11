import json
from abc import ABC


class DAO(ABC):
    def __init__(self, datasource):
        self.__datasource = datasource
        self.__object_cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            print('db vazia')

    @property
    def datasource(self):
        return self.__datasource

    @property
    def object_cache(self):
        return self.__object_cache

    def __load(self):
        file = open(self.__datasource)
        self.__object_cache = json.load(file)
        file.close()


    def get(self, key):
        try:
            return self.__object_cache[key]
        
        except KeyError:
            print('Chave não disponível')