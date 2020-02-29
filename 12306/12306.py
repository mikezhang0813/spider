
# coding: utf-8

# In[51]:


import requests
from hashlib import md5
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from io import BytesIO
from PIL import Image
import time
import os

from chaojiying import Chaojiying_Client


# In[14]:


SOFT_ID = '903396'
USER_NAME = 'zhangdada'
PASSWORD = 'zyw08135932'
site_username = '991256338@qq.com'
site_password = 'zyw08135932'
URL = 'https://kyfw.12306.cn/otn/resources/login.html'


# In[72]:


class CrackTrain():

    def __init__(self, username, password, soft_id):
        """初始化获得浏览器对象和"""
        self.browser = webdriver.Chrome()
        self.browser.get(URL)
        self.wait = WebDriverWait(self.browser,20)
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }
        self.chaoying = Chaojiying_Client(self.username,self.password,self.soft_id)
    def get_account_login(self):
        """选择为密码登陆"""
        a_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.login-hd-account a')))
        
        a_link.click()
    def login_para_fill(self):
        """填入用户名密码"""
        self.get_account_login()
        time.sleep(2)
        username_area = self.wait.until(EC.presence_of_element_located((By.ID,'J-userName')))
        password = self.wait.until(EC.presence_of_element_located((By.ID,'J-password')))
        
        username_area.send_keys(site_username)
        password.send_keys(site_password)
        
    def get_img_position(self):
        """获取验证码图片位置"""
        img = self.wait.until(EC.presence_of_element_located((By.ID,'J-loginImg')))
        location = img.location       
        size = img.size
        top,bottom,left,right = location['y'],location['y']+size['height'],location['x'],location['x']+size['width']
        return  (top,bottom,left,right) 
        
    def get_screen_shot(self):
        """截取整个页面图片"""
        
        screen_shot = self.browser.get_screenshot_as_png()
        screen_shot = Image.open(BytesIO(screen_shot))
        screen_shot.show()
        return screen_shot
    def get_img(self):
        imgcode = self.wait.until(EC.presence_of_element_located((By.ID,'J-loginImg')))
        imgcode.screenshot('imgcode.png')
        with open('imgcode.png','rb') as fout:
            content = fout.read()
        return content
    def get_result(self):
        """获取超级鹰验证结果"""
        img = self.get_img()
        # path ='/Users/nancy/Desktop/spider/12306/'
        # if not os.path.exists(path):
        #     os.makedirs(path)
        # filename =path+ str(len(os.listdir(path))+1)+'.PNG'       
        # byte_array = BytesIO()
        # img.show()
        # img.save(byte_array,format="PNG")
        print(type(img))
        result = self.PostPic(img,9005)
        print(result)
        return result
    def get_coordinates(self):
        print('验证中....')
        result = self.get_result()
        location = [[int(number) for number in group.split(',')] for group in result['pic_str'].split('|')]
        
        return location
    def touch_img(self):
        locations = self.get_coordinates()
        for location in locations:
            ActionChains(self.browser).move_to_element_with_offset(self.get_element(),location[0],location[1]).click().perform()
            time.sleep(1)
        self.login_submit()
    def login_submit(self):
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'login-btn')))
        button.click()
    def get_element(self):
        element  = self.wait.until(EC.presence_of_element_located((By.ID,'J-loginImg')))
        
        return element
    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()
    def run(self):
        
        self.login_para_fill()
        self.get_img()
        self.touch_img()


if __name__ == '__main__':
    cracker = CrackTrain(USER_NAME,PASSWORD,SOFT_ID)
    cracker.run()
    
   
    


# In[70]:




