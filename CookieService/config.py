"""百度云账号信息"""
BAIDU_ACCOUNT = {
    "API_KEY": "5ojN27kRs1FvbEZNYaadnZa3",
    "SECRET_KEY": "OZDveWQT6xFva40sUVoc1rZPirecg69Z"
}

MYSQL = {
    "MYSQL_HOST": "101.132.192.136",
    "MYSQL_PORT": 3306,
    "MYSQL_USER": "mike",
    "MYSQL_PASSWORD": "123",
    "MYSQL_DB": 'zhihu'
}

REDIS = {
    "REDIS_HOST": "101.132.192.136",
    "REDIS_PORT": 6380,
    "REDIS_DB": 0,

}
REDIS_NAME = {
    "zhihu": {"REDIS_ACCOUNT_KEY_TYPE": "account",
              "REDIS_COOKIE_KEY_TYPE": "cookies"}

}
VALIDATOR_MAP = {
    "zhihu": "ZhihuCookieValidator"
}
GENERATOR_MAP = {
 "zhihu":"ZhiHuService"
}
COOKIE_VALI_URL_MAP = {
    "zhihu": "https://www.zhihu.com/"
}
DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}

GENERATOR_CYCLE = 1000

VALIDATOR_CYCLE = 50