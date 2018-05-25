import os 
from configparser import ConfigParser

class GetConfig:
    def __init__(self):
        self.pwd = os.path.split(os.path.realpath(__file__))[0]
        self.config_file = os.path.join(os.path.split(self.pwd)[0],'config.ini')
        self.cf = ConfigParser()
        self.cf.read(self.config_file)
        
    @property
    def db_host(self):
        return self.cf.get('DB','host')
    
    @property
    def db_port(self):
        return self.cf.getint('DB','port')
    
    @property
    def db_name(self):
        return self.cf.get('DB','name')