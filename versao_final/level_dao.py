from dao import DAO
class Level_dao(DAO):
    def __init__(self, datasource, level: int):
        super().__init__(datasource)
        self.__level = level
    
    def get(self, key):
        for i in self.object_cache:
            if i['id'] == self.__level:
                return i[key]
    

        

    
