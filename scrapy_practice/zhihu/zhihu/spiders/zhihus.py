import scrapy
import re
import json
from zhihu.zhihu.items import ZhihuItem
import hashlib
class ZhihusSpider(scrapy.Spider):
    name = 'zhihus'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']

    def parse(self, response):
        result = response.xpath("//script[@id='js-initialData']/text()").get()
        json_data = json.loads(result)
        answers = json_data['initialState']["entities"]
        for answer in answers:
            item = ZhihuItem()

            question_id = answer['answers']



