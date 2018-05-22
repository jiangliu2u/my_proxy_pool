from Web.Util import Singleton
from DB.Redis import RedisClient


class DBClient(metaclass=Singleton):
    def __init__(self, name, host, port):
        self.client = RedisClient(name, host, port)

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

#
# if __name__ == "__main__":
#     account = DBClient('proxy', 'localhost', 6379)
#     print(account.getAll())
