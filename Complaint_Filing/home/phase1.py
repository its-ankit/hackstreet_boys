from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
# options.headless = True
options.add_argument('--disable-notifications')
driver = webdriver.Chrome('C:\\Users\\Shaurya\\Documents\\Lets Start\\Complaint_Filing\chromedriver.exe',options=options)
driver.get('https://www.facebook.com/')
driver.find_element(By.NAME, 'email').send_keys('6201560685')
driver.find_element(By.NAME, 'pass').send_keys('#$hourya17Puru')
driver.find_element(By.NAME, 'login').send_keys(Keys.ENTER)
time.sleep(30)


# box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
# data="cats images"
# box.send_keys(data)
# box.send_keys(Keys.ENTER)

# driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()


# #Will keep scrolling down the webpage until it cannot scroll no more
# last_height = driver.execute_script('return document.body.scrollHeight')
# while True:
#     driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#     time.sleep(2)
#     new_height = driver.execute_script('return document.body.scrollHeight')
#     try:
#         driver.find_element(By.XPATH, '//*[@id="islrg"]/div/div/div/div/div[5]/input').click()
#         time.sleep(2)
#     except:
#         pass
#     if new_height == last_height:
#         break
#     last_height = new_height

# # getting all image links and storing in the lis
# lis=[]
# for i in range(1, 100):
#     try:
#         link=driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img')
#         img=link.get_attribute("src")
#         lis.append(img)
#     except:
#         pass

# print(lis)

