from Web.Util import Singleton

class DBClient(metaclass=Singleton):
    def __init__(self,client):
        self.client = client()