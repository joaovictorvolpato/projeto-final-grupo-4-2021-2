from dao import DAO
class Level_dao(DAO):
    def __init__(self, datasource, level: int):
        super().__init__(datasource)
        self._level = level
    
    def get(self, key):
        for i in self.object_cache:
            if i['id'] == self._level:
                return i[key]
    

        

    
