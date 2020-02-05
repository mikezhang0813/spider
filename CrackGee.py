
# coding: utf-8

# In[29]:


import selenium
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


# In[27]:


import time
from PIL import Image
from io import BytesIO


# In[3]:


EMAIL  = 'zyw01050813@163.com'
PASSWORD = 'zyw08135932'


# In[34]:


class CrackGee():
    def __init__(self):
        self.url = 'https://auth.geetest.com/login'
        self.browser = webdriver.Chrome()
        self.browser.get(self.url)
        self.wait = WebDriverWait(self.browser,20)     
        self.email = EMAIL
        self.password = PASSWORD
    def input_para(self):
        email = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'[placeholder="请输入邮箱"]')))
        password = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'[placeholder="请输入密码"]')))
        email.send_keys(self.email)
        password.send_keys(self.password)
    def get_button(self):
        self.input_para()            
        button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.geetest_radar_tip')))
        return button
    
    def get_img_location(self):
        """
        获取图片位置
        """       
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_canvas_img')))
        location = img.location
        size = img.size
        top,bottom,left,right = location['y'],location['y']+size['height'],location['x'],location['x']+size['width']
        print(top,bottom,left,right)
        return top,bottom,left,right
    def get_screen_shot(self):
        screen_shot = self.browser.get_screenshot_as_png()
        screen_shot = Image.open(BytesIO(screen_shot))
        return screen_shot
    def get_geetest_img(self,name='captcha.png'):        
        top,bottom,left,right = self.get_img_location()
        print('验证码位置',(top,bottom,left,right))
        screen_shot = self.get_screen_shot()
        captcha = screen_shot.crop((left,top,right,bottom))
        return captcha
    def get_slider(self):
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_slider_button')))
        return slider 
    def is_pixel_equal(self,image1,image2,x,y):
        """
        判断两张照片相同位置的rgb三原色的值是否相等
        """
        pixel1 = image1.load()[x,y]
        pixel2 = image2.load()[x,y]
        """设定阈值"""
        threshold = 60
        if abs(pixel1[0]-pixel2[0])<threshold and abs(pixel1[1]-pixel2[1])<threshold and         abs(pixel1[2]-pixel2[2])<threshold :
            return True
        else:
            return False
        
    def get_gap(self,image1,image2):
        """获取缺口偏移量"""
        left = 60
        for i  in range(left,image1.size[0]):
            """从滑块右边开始依次向右判断像素值"""
            for j in range(image2.size[1]):
                if not self.is_pixel_equal(image1,image2,i,j):
                    left = i
                    return left
                
        return left
    
    def get_tracks(self,distance):
        """获取移动轨迹,通过设置相同时间间隔，获取滑块的位移"""
        """distance 缺口偏移量"""
        current = 0 #当前位置
        mid = distance*0.8 #设置开始减速点
        v0 = 0 #设置初速度
        t = 0.2 #时间间隔
        tracks = []#记录轨迹
        while current < distance:
            if current < mid:
                a = 2
            else:
                a = -3
            v0 = v
            v = v0+a*t
            #移动距离
            move = v0*t+1/2*a*t*t
            #当前位移
            current += move
            tracks.append(round(move))
        return tracks
    def move_slider(self,slider,tracks):
        ActionChains(self.browser).click_and_hold(slider).perform()
        for i in tracks:
            ActionChains(self.browser).move_by_offset(xoffset=i,yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()
    def run(self):
        
        button = self.get_button()
        button.click()
        image1 = self.get_geetest_img()
        slider = self.get_slider()
        slider.click()
        image2 = self.get_geetest_img()
        distance = self.get_gap(image1,image2)
        track = self.get_tracks(distance)
        self.move_slider(slider,track)
        


# In[35]:


cracker = CrackGee()
cracker.run()

