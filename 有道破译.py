"""
有道翻译破解
请求参数
    i: hand      #单词
    from: AUTO   输入语言
    to: AUTO     输出语言
    smartresult: dict     结果返回形式
    client: fanyideskweb     客户端固定
    salt: 16034192393252     时间戳加 0-9之间的随机数
    sign: 2cd0ec27be88dee373077770d82aab0b  “fanyideskweb+单词+salt+ "]BjuETDhU)zqSxf-=B#7m") md5加密
    lts: 1603419239325           时间戳
    bv: 8269b35cc1594b7635631cdd3a301112
    doctype: json
    version: 2.1
    keyfrom: fanyi.web
    action: FY_BY_REALTlME
"""
import time
import random
import hashlib
import requests
target_url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
headers = {
    # "Accept": "application/json, text/javascript, */*; q=0.01",
    # "Accept-Encoding": "gzip, deflate",
    # "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
    # "Connection": "keep-alive",
    # "Content-Length": "238",
    # "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "OUTFOX_SEARCH_USER_ID=31139982@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=863130346.7375027; _ntes_nnid=9b04e9f9d0ee34105a0131f10eece846,1603097397637; JSESSIONID=aaaSRbYWYm_uPhnZYntvx; ___rl__test__cookies=1603419239323",
    # "Host": "fanyi.youdao.com",
    # "Origin": "http://fanyi.youdao.com",
    "Referer": "http://fanyi.youdao.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    # "X-Requested-With": "XMLHttpRequest"
}
word = input('输入单词')
ts = str(int(time.time()*1000))
salt = ts+str(random.randint(int(random.random()*10),9))
# “fanyideskweb+单词+salt+ "]BjuETDhU)zqSxf-=B#7m") md5加密
m = hashlib.md5()
value = "fanyideskweb"+word+salt+"]BjuETDhU)zqSxf-=B#7m"
m.update(value.encode('utf8'))
sign = m.hexdigest()
print(sign)
data = {
"i": word,
"from": "AUTO",
"to": "AUTO",
"smartresult": "dict",
"client": "fanyideskweb",
"salt": salt,
"sign": sign,
"lts": ts,
"bv": "8269b35cc1594b7635631cdd3a301112",
"doctype": "json",
"version": "2.1",
"keyfrom": "fanyi.web",
"action": "FY_BY_REALTlME",
}
res = requests.post(url = target_url,headers=headers,data=data )
print(res.status_code)
print(res.json())