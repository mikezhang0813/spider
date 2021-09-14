import time

import requests
import json
from config import *
from CookiePool import RedisDB


class BaseValidator:
    def __init__(self, site="default", CYCLE=1000):
        self.site = site
        self.cookie_db = RedisDB("cookies", self.site)
        self.cycle = CYCLE

    def test(self, account, cookie):
        raise NotImplemented

    def run(self):

        for account, cookie in self.cookie_db.all().items():
            # print(account,cookie)
            self.test(account, cookie)



class ZhihuCookieValidator(BaseValidator):

    def __init__(self):
        super(ZhihuCookieValidator, self).__init__("zhihu")

        self.cookies_db = RedisDB("cookies", self.site)
        # self.cookies_db.set("111",'222')
        # self.cycle = CYCLE

    def test(self, account, cookie):
        print("=====cookie 验证开始======")

        try:
            cookies = json.loads(cookie)
        except TypeError:
            print("cookie 类型错误")
            self.cookies_db.delete(account)
            print("cookie for account [{}] deleted as wrong cookie type ".format(account))
            return

        try:
            com_cookie = {}
            for cookie in cookies:
                com_cookie.update(cookie)
            print(com_cookie)
            res = requests.get(COOKIE_VALI_URL_MAP[self.site], cookies=com_cookie, headers=DEFAULT_HEADERS)
            if res.status_code == 200:
                print("cookie for account [{}] valid".format(account))

            else:
                print("cookie for account [{}] invalid".format(account))
                self.cookies_db.delete(account)
                print("cookie for account [{}] deleted as cookie valid".format(account))
        except Exception as e:
            print(e.args)
            pass


if __name__ == "__main__":
    Validator = ZhihuCookieValidator()
    Validator.run()
