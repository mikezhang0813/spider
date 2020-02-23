"""
百度图片爬取
author Koala Zhang
datetime 2020-02-23
"""

import  requests
import re
import os
import sys
from urllib.request import  urlretrieve
from lxml import etree
import hashlib
from fake_useragent import  UserAgent

import dbhelper

START_URLS = 'http://image.baidu.com/search/index?tn=baiduimage&word=%E5%AE%A0%E7%89%A9'
db = dbhelper.DbHelper(database='beauty')
def get_useragent():
  """
  获取user-agent
  :return: 若fakeuser调用出错，则返回默认的User-Agent
  """
  ua = UserAgent()
  try:
    useragent = ua.random
    return useragent
  except Exception as e:
    print("获取UsesAgent中")
  finally:
    return "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"


def get_html(url=None,para=None,headers = None):
  """
  获取网页响应
  :param url: 目标url
  :return: 响应response对象
  """
  if headers is None:
    headers = {'User-Agent':get_useragent()
               }
  try:
    if url is None:
      url = START_URLS
    res = requests.get(url = url,headers=headers,params=para)
  except Exception as e:
    print('***********')
    print('[error]',e)
    print('***********')
  else:
    print('访问成功')
    if res.status_code == 200:

      return res
    else:
      return None
def parse_html():
  res = get_html('http://image.baidu.com/search/acjson')
  pattern = r'"thumbURL":\s*"(.*?)"'
  reuslt = re.findall(pattern,res.text)
  print(reuslt)
def download_img(url):
  """
  下载图片，
  :param url: 图片地址
  :return: 图片存入地址
  """
  header = {
              "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
              "Accept-Encoding":"gzip, deflate",
              "Accept-Language":"zh-CN,zh;q=0.9",
              "Cache-Control":"no-cache",
              "Connection":"keep-alive",
              "Host":"img1.imgtn.bdimg.com",
              "Pragma":"no-cache",
              "Upgrade-Insecure-Requests":"1",
              "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
  }
  res = get_html(url,headers=header)
  save_img(res.content)
  print("存入成功")

def get_finger(url):
  url_finger = encry_with_md5(url)
  save_finger(url_finger)


def encry_with_md5(url):
  m5 = hashlib.md5()
  m5.update(url.encode())
  url_finger = m5.hexdigest()
  return url_finger


def check_finger(url):
  finger = encry_with_md5(url)
  result = db.get('fingers',[('fingers',finger)])
  print(result)
  return None


def save_finger(finger):
  db.insert([('fingers',finger)],finger)




def save_img(img):


   path = '/Volumes/koala/pet/'
   if not os.path.exists(path):

      os.makedirs(path)
   filename = path+'img'+str(len(os.listdir(path))+1)+'.jpg'
   with open(filename,'wb') as fin:
     fin.write(img)
     print('写入成功')


def main():
  for i in range(0,1000,30):
    pn = i
    para = {
      "tn":"resultjson_com",
      "ipn":"rj",
      "ct":"201326592",
      "is":"",
      "fp":"result",
      "queryWord":" 宠物",
      "cl":"",
      "lm":"",
      "ie":"utf-8",
      "oe":"utf-8",
      "adpicid":"",
      "st":"",
      "z":"",
      "ic":"",
      "hd":"",
      "latest":"",
      "copyright":"",
      "word":"宠物",
      "s":"",
      "se":"",
      "tab":"",
      "width":"",
      "height":"",
      "face":"",
      "istype":"",
      "qc":"",
      "nc":"",
      "fr":"",
      "expermode":"",
      "force":"",
      "pn":pn,
      "rn":"30",
      "gsm":"186",
      "1582439040258":""
}
    res = get_html('http://image.baidu.com/search/acjson',para=para)
    if not res:
      print("响应为空")
      continue
    try:
      json_data = res.json()['data']
      for item in json_data:
        if 'adType' in item and item['adType'] == '0':
          url = item['thumbURL']
          if not check_finger(url):
            download_img(url)
    except Exception:
      continue






if __name__ == "__main__":
  main()



