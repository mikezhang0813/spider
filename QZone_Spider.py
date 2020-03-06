"""
QQ空间照片批量下载
author:zhangdada
Time:2020-03-06
"""
import requests
import json
import execjs
import re
#想要抓取的QQ号
TARGET_NUMBER = "784284326"
SELF_QQ = "991256338"


def get_para():
    """
    获取请求参数
    :return:g_tk,t
    """
    with open('/Users/koala/Documents/qqSpider/qqzone.js', 'r') as fin:
        script = fin.read()
    compile_script = execjs.compile(script)
    g_tk = compile_script.eval('token(url)')

    t = compile_script.eval('t()')
    # print(g_tk,t)
    return g_tk,t

# browser = webdriver.Chrome()
# browser.get('https://user.qzone.qq.com')

COOKIE_PATH = "/Users/koala/Documents/qqSpider/cookie.txt"
def get_cookie():
    with open(COOKIE_PATH,'r') as fin:
        cookie = fin.read().strip()
    return cookie
COOKIE = get_cookie()
#相册首页链接
def get_pic_index(target_qq_number=TARGET_NUMBER):

    """获取相册ID"""
    """parameter     target_qq_number     想要爬取的QQ号相册"""
    """手动登录后拷贝的cookie"""

    url = 'https://user.qzone.qq.com/proxy/domain/photo.qzone.qq.com/fcgi-bin/fcg_list_album_v3'
    header = {
            "accept":"text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
            "accept-encoding":"gzip, deflate, br",
            "accept-language":"zh-CN,zh;q=0.9",
            "cookie":COOKIE,
            "referer":"https://user.qzone.qq.com/proxy/domain/qzs.qq.com/qzone/photo/v7/page/photo.html?init=photo.v7/module/albumList/index&g_iframeUser=1",
            "sec-fetch-dest":"empty",
            "sec-fetch-mode":"cors",
            "sec-fetch-site":"same-origin",
            "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
            "x-requested-with":"XMLHttpRequest",
}


    g_tk,t = get_para()
    para = {
            "g_tk":g_tk,
            "callback":"shine0_Callback",
            "t":t,
            "hostUin":target_qq_number,
            "uin":SELF_QQ,
            "appid":"4",
            "inCharset":"utf-8",
            "outCharset":"utf-8",
            "source":"qzone",
            "plat":"qzone",
            "format":"jsonp",
            "notice":"0",
            "filter":"1",
            "handset":"4",
            "pageNumModeSort":"40",
            "pageNumModeClass":"15",
            "needUserInfo":"1",
            "idcNum":"4",
            "callbackFun":"shine0",
            "_":"1583410530071",
        
    }

    res = requests.get(url=url,params=para,headers=header)
    print(res.status_code,res.url)
    if res.status_code == 200:
        print(res.text)
        html = res.text

        # data = json.loads(res.text)
        
        ids = re.findall(r'"id"\s*?:\s+"(.*?)"',html,re.S|re.M)
        #匹配相册id
        print('ids',ids)
        return list(filter(lambda id:id!='',ids))

def get_cookie(path):
    with open(path,'r') as fin:
        cookie = fin.read()
    return cookie
ids = get_pic_index()


def get_photo_url(topicId,target_number=TARGET_NUMBER):
    url3 = 'https://h5.qzone.qq.com/proxy/domain/photo.qzone.qq.com/fcgi-bin/cgi_list_photo'
    headers = {
            "accept":"*/*",
            "accept-encoding":"gzip, deflate, br",
            "accept-language":"zh-CN,zh;q=0.9",
            "cookie":COOKIE,
            "referer":"https://user.qzone.qq.com/proxy/domain/qzs.qq.com/qzone/photo/v7/page/photo.html?init=photo.v7/module/photoList2/index&navBar=1&normal=1&aid=76e85859-469b-4504-8150-f25e&g_iframeUser=1",
            "sec-fetch-dest":"script",
            "sec-fetch-mode":"no-cors",
            "sec-fetch-site":"same-site",
            "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",

        }
    g_tk, t = get_para()
    para = {
       "g_tk":g_tk,#参数更改
        "callback":"shine0_Callback",
        "t":t,#参数更改   get_sign
        "mode":"0",
        "idcNum":"4",
        "hostUin":target_number,
        "topicId":topicId,
        "noTopic":"0",
        "uin":SELF_QQ,
        "pageStart":"0",
        "pageNum":"30",
        "skipCmtCount":"0",
        "singleurl":"1",
        "batchId":"",
        "notice":"0",
        "appid":"4",
        "inCharset":"utf-8",
        "outCharset":"utf-8",
        "source":"qzone",
        "plat":"qzone",
        "outstyle":"json",
        "format":"jsonp",
        "json_esc":"1",
        "question":"",
        "answer":"",
        "callbackFun":"shine0",
        # "_":"1583411366942",#参数更改
    }
    res1 = requests.get(url3,headers=headers,params=para)
    print("status_code:",res1.status_code)

    if res1.status_code == 200:
        html = res1.text

        photo_url = list(filter(lambda url:url !='',re.findall(r'"url"\s+:\s+"(.*?)"',html,re.S|re.M)))
        print(photo_url)

for id in ids:
    get_photo_url(id)

