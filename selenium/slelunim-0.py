from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import cv2
import requests

# service = Service(executable_path='./resources/chromedriver')
# driver = webdriver.Chrome(service=service)

driver = webdriver.Chrome()
driver.get("http://www.cheshi.com/")

print(driver.current_url)

# 存取当前网站的 HTML
with open("cheshilogin4.html", "w") as f:
    f.write(driver.page_source)

time.sleep(1)
driver.quit()