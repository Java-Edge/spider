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

username = driver.find_element(By.XPATH, '//*[@id="username"]')
password = driver.find_element(By.XPATH, '//*[@id="password"]')

ActionChains(driver).click(username).pause(1).send_keys("abcde").pause(0.5).perform()
ActionChains(driver).click(password).pause(1).send_keys("12345").pause(0.5).perform()
time.sleep(1)

div = driver.find_element(By.XPATH, '//*[@id="end"]')
ActionChains(driver).scroll_to_element(div).perform()
time.sleep(1)
ActionChains(driver).scroll_by_amount(0, 200).perform()

time.sleep(1)
driver.quit()