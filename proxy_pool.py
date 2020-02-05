import requests
from lxml import etree
import time
import os
url = "https://www.xicidaili.com/nn/"
from fake_useragent import  UserAgent
class  ProxyPoolBuild():
    def __init__(self):
        self.url = "https://www.xicidaili.com/nn/{}"


    def get_html(self,url):
        try:
            headers = {'User-Agent':'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
            res = requests.get(url=url,headers=headers)

            if res.status_code==200:
                html = res.text

                return html
        except Exception:
            print("网页连接错误")


    def re_func(self,regex,html):
        parse_obj = etree.HTML(html)
        target_content = parse_obj.xpath(regex)
        return target_content


    def get_headers(self):
        headers = {"User-Agent":UserAgent().random}
        return headers
    def parse_html(self,html):
        print(html)
        regex="//tr/td[position()>1 and position()<4]/text()"
        content_list = self.re_func(regex,html)
        return content_list
    def check_validity(self,ip_port):
        url = "http://httpbin.org/anything"
        addr1 = "http://{}:{}".format(ip_port[0],ip_port[1])
        addr2 = "http://{}:{}".format(ip_port[0],ip_port[1])
        proxies = {
            'http':addr1,
            'https':addr2
        }
        try:
            res = requests.get(url,proxies=proxies,timeout=5)
            if res.status_code==200:
                return True
            else:
                print(res.text)
        except Exception:
            pass
    def load_into_file(self,ip_port):
        path = "/Users/nancy/Desktop/spider/agentpool/"
        if not os.path.exists(path):
            os.makedirs(path)
        filename = path+"agentpool.txt"
        with open(filename,"a+") as fin:
            fin.write(ip_port)
            fin.write("\n")
            print("写入成功")
    def run(self):
        for number in range(1,4021):
            url = self.url.format(number)
            time.sleep(3)
            html = self.get_html(url)
            content = self.parse_html(html)
            end = len(content)
            for i in range(2,end+1,2):
                ip_port = content[i-2:i]
                if self.check_validity(ip_port):
                    self.load_into_file(":".join(ip_port))







if __name__=="__main__":
    spider = ProxyPoolBuild()
    spider.run()

