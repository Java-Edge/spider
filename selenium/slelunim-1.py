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

try:
    h1 = driver.find_element(By.XPATH, "//h1")
    print(type(h1))
    print(h1.text)
    print(driver.current_url)
except Exception as e:
    print(e)

time.sleep(1)
driver.quit()