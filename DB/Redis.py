import redis
import sys
import random
import json


class RedisClient:
    def __init__(self, name, host, port):
        self.name = name
        self.__conn = redis.Redis(host=host, port=port)

    def get(self):
        key = self.__conn.hgetall(name=self.name)
        rkey = random.choice(list(key.keys())) if key else None
        if isinstance(rkey, bytes):
            return rkey.decode('utf-8')
        else:
            return rkey

    def put(self, key):
        key = json.dumps(key) if isinstance(key, (dict, list)) else key
        return self.__conn.hincrby(self.name, key, 1)

    def getvalue(self, key):
        value = self.__conn.hget(self.name, key)
        return value if value else None

    def update(self, key, value):
        self.__conn.hincrby(self.name, key, value)

    def exists(self, key):
        return self.__conn.exists(key)

    def pop(self):
        key = self.get()
        if key:
            self.__conn.hdel(self.name, key)
        return key

    def delete(self, key):
        self.__conn.hdel(self.name, key)

    def inckey(self, key, value):
        self.__conn.hincrby(self.name, key, value)

    def getAll(self):
        return [key.decode('utf-8') for key in self.__conn.hgetall(self.name).keys()]

    def get_status(self):
        return self.__conn.hlen(self.name)

    def changeTable(self, name):
        self.name = name


# if __name__ == '__main__':
#     redis_con = RedisClient('proxy', 'localhost', 6379)
#     # redis_con.put('abc')
#     # redis_con.put('123')
#     # redis_con.put('123.115.235.221:8800')
#     # redis_con.put(['123', '115', '235.221:8800'])
#     # print(redis_con.getAll())
#     # redis_con.delete('abc')
#     print(redis_con.get())
