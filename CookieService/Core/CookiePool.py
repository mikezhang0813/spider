import pymysql
import redis
import random
from config import *
class RedisDB:
    def __init__(self,type,site):
        self.type = type
        self.site = site
        self.db = redis.StrictRedis(host=REDIS['REDIS_HOST'], port=REDIS['REDIS_PORT'], db=REDIS['REDIS_DB'],
                                          decode_responses=True)


    def name(self):
        return "{}:{}".format(self.type,self.site)

    def set(self,key,value):
        self.db.hset(self.name(),key,value)

    def get(self,key):
        return self.db.hget(self.name(),key)

    def delete(self,key):
        self.db.hdel(self.name(),key)
        print("删除成功")

    def all(self):
        return self.db.hgetall(self.name())

    def count(self):

        return self.db.hlen(self.name())

    def usernames(self):
        return self.db.hkeys(self.name())

    def random(self):
        return random.choice(self.db.hvals(self.name()))





