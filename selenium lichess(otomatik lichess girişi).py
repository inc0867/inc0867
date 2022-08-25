from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#note :  pip install selenium , install driver chrome,Edge or Etc. 

url = "https://lichess.org/login?referrer=/"


browser = webdriver.Edge()


browser.get(url)

time.sleep(3)


kullanci = browser.find_element(By.XPATH,"//*[@id='form3-username']")


kullanci.send_keys("USERNAME")





sifre = browser.find_element(By.XPATH,"//*[@id='form3-password']")

sifre.send_keys("PASSWORD")

gir = browser.find_element(By.XPATH,"//*[@id='main-wrap']/main/form/div[1]/button")

gir.click()
time.sleep(3)


oyunlar = browser.find_element(By.XPATH,"//*[@id='main-wrap']/main/div[2]/div[2]/div[1]")
oyunlar.click()



time.sleep(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

browser.close()







