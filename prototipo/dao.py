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
    # def __dump(self):
    #     pickle.dump(self.objectCache, open(self.datasource, 'wb'))

    @property
    def datasource(self):
        return self.__datasource

    @property
    def object_cache(self):
        return self.__object_cache

    def __load(self):
        self.__object_cache = json.load(open(self.__datasource))
        print(self.__object_cache)


    def get(self, key):
        print('pai')
        try:
            return self.__object_cache[key]
        
        except KeyError:
            print('Chave não disponível')