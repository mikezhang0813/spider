import time
from multiprocessing import Process

from CookieValidator import ZhihuCookieValidator
from CookiePool import RedisDB
import pymysql
from api import *
from Service.ZhihuService import  *
class Scheduler:
    def __init__(self):

        self.mysql_db = pymysql.connect(host=MYSQL['MYSQL_HOST'],port=MYSQL['MYSQL_PORT'],
                                        user=MYSQL['MYSQL_USER'],password=MYSQL['MYSQL_PASSWORD'],db=MYSQL['MYSQL_DB'],cursorclass=pymysql.cursors.DictCursor)

        self.cursor = self.mysql_db.cursor()
        self.load_account()
    def load_account(self):
        sql = "select account,password,site from account"
        self.db_map = {}
        self.site_loaded = set([])
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for result in results:
                site = result['site']
                account = result['account']
                password = result['password']
                if site not in self.site_loaded:
                    print(f"site {site} 创建 db_map")
                    account_ab = RedisDB('account',site)
                    account_ab.set(account,password)
                    self.db_map[site] = {}
                    self.db_map[site]['account_db'] = account_ab
                    self.site_loaded.add(site)
                else:
                    self.db_map[site]['account_db'].set(account,password)
            print("\n".join(["[*] {} : {} accounts loaded ".format(site,dbs['account_db'].count()) for site,dbs in self.db_map.items()]))

        except Exception as e:
            print(e)


    @staticmethod
    def generator(cycle=GENERATOR_CYCLE):
        print("cookie 生成服务开始")
        while True:
            for site,cls in GENERATOR_MAP.items():
                generator = eval(cls+"()")
                # print(generator)
                generator.run()

            time.sleep(cycle)

    @staticmethod
    def validator(cycle=VALIDATOR_CYCLE):
        print("cookie 验证服务开始")
        while True:

            for site, cls in VALIDATOR_MAP.items():
                validator = eval(cls+"()")
                # print(validator)
                validator.run()
            time.sleep(cycle)
    def run(self):
        gene_pro = Process(target=Scheduler.generator)
        gene_pro.start()

        validator = Process(target=Scheduler.validator)
        validator.start()
        app.run()
if __name__ == "__main__":
    sche = Scheduler()
    sche.run()



