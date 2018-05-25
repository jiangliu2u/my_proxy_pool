import sys
sys.path.append('..')

from Util.GetConfig import GetConfig
from Util.Util import Singleton
from DB.Redis import RedisClient

class DBClient(metaclass=Singleton):
    def __init__(self):
        self.config = GetConfig()
        self.__initClient()
    
    def __initClient(self):
        self.client = RedisClient(name=self.config.db_name,host=self.config.db_host,port=self.config.db_port)
        
    def get(self, **kwargs):
        return self.client.get()

    def put(self, key, **kwargs):
        return self.client.put(key)

    def update(self, key, value, **kwargs):
        return self.client.update(key, value)

    def delete(self, key, **kwargs):
        return self.client.delete(key)

    def exists(self, key, **kwargs):
        return self.client.exists(key, **kwargs)

    def pop(self, **kwargs):
        return self.client.pop()

    def getAll(self, **kwargs):
        return self.client.getAll()

    def changeTable(self, name, **kwargs):
        self.client.changeTable(name)

    def getNumber(self):
        return self.client.getNumber()

if __name__ == "__main__":
    account = DBClient('useful_proxy', 'localhost', 6379)
    print(len(account.getAll()))
    print(account.delete('58.255.38.115:9797'))
