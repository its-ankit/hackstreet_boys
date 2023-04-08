# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
# import getpass

# import argparse
# import json
# import csv
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup as bs
# from autoscraper import AutoScraper

# options = webdriver.ChromeOptions()
# # options.headless = True
# options.add_argument('--disable-notifications')
# driver = webdriver.Chrome('C:\\Users\\Shaurya\\Documents\\Lets Start\\Complaint_Filing\chromedriver.exe',options=options)
# driver.get('https://www.facebook.com/')

# driver.find_element(By.NAME, 'email').send_keys('6201560685')
# driver.find_element(By.NAME, 'pass').send_keys('#$hourya17Puru')
# driver.find_element(By.NAME, 'login').send_keys(Keys.ENTER)

# texts=driver.find_element(By.CLASS_NAME, 'x126k92a')
# print(texts)
# time.sleep(40)
# page_source=driver.page_source
# Parse the html file
# soups = bs(page_source, 'html.parser')

# Format the parsed html file
# soup = soups.prettify()
# texts=soups.find_all('div[@class="x11i5rnm xat24cr x1mh8g0r x1vvkbs xdj266r x126k92a"]')
# print(texts)
# fun=open("home.html","w")
# fun.write(page_source)
# fun.close()
# url='home.html'
# lis=["Advertising Tips Sharing Community","I have found a way to increase my ad payment threshold limit, It's great it helps me increase my work efficiency, I share it for everyone to promote the business process together. "]
# texts=driver.find_element(By.CSS_SELECTOR, 'div[id="jsc_c_8k"] div[dir="auto"]').getText()
# print(texts)
# print(page_source)
# scraper=AutoScraper()
# result=scraper.build(url,lis)
# print(strhtm)

# def _extract_post_text(item):
#     actualPosts = item.find_all(attrs={"data-testid": "post_message"})
#     text = ""
#     if actualPosts:
#         for posts in actualPosts:
#             paragraphs = posts.find_all('p')
#             text = ""
#             for index in range(0, len(paragraphs)):
#                 text += paragraphs[index].text
#     return text







# last_height = driver.execute_script('return document.body.scrollHeight')
# i=0
# texts=driver.find_element(By.XPATH, '//h4[@id="jsc_c_56"]//span[@class="xt0psk2"]').getText()
# print(texts)
# while (i<20):
#      driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#      time.sleep(2)
#      new_height = driver.execute_script('return document.body.scrollHeight')
#      try:
#          texts=driver.find_element(By.XPATH, '\\div[contains(@class,"x11i5rnm xat24cr x1mh8g0r x1vvkbs xdj266r x126k92a")]').getText()
#          time.sleep(2)
#          lis.append(texts)
#      except:
#          pass
#      if new_height == last_height:
#          break
#      last_height = new_height
    #  i+=1
# print(lis)
# name_of_user=driver.find_element(By.XPATH, '//div[@class="x11i5rnm xat24cr x1mh8g0r x1vvkbs xdj266r x126k92a"]')
# print(name_of_user)
# time.sleep(30)


# box = driver.find_element(By.XPATH, 'h4[id='jsc_c_ys'] a[role='link'] span')
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


from facebook_page_scraper import Facebook_scraper

page_name="reporting scams"
posts_count=10
browser="chrome"
proxy=""
timeout=600
meta_ai=Facebook_scraper(page_name,posts_count, browser, proxy=proxy, timeout=timeout)
json_data=meta_ai.scrap_to_join()
print(json_data)