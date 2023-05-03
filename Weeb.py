from script import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def switch_frame(element):
    driver.switch_to.default_content()
    driver.switch_to.frame(element)
    

driver = webdriver.Chrome()
driver.get("https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query")

MyID_path = driver.find_element(By.ID,"pid")
MyID_path.send_keys(MyID)
Start_Station_path = driver.find_element(By.ID,"startStation")
Start_Station_path.send_keys(Start_Station)
End_Station_path = driver.find_element(By.ID,"endStation")
End_Station_path.send_keys(End_Station)
Button_bytime = driver.find_element(By.XPATH,"//*[@id='"'queryForm'"']/div[1]/div[1]/div[6]/div[2]/label[2]")
Button_bytime.click()

Start_time_path = driver.find_element(By.ID,"startTime1")
Start_time_path.send_keys(Start_time)
End_time_path = driver.find_element(By.ID,"endTime1")
End_time_path.send_keys(End_time)

Traintype = driver.find_element(By.CLASS_NAME,"trainType")
Traintype_list = Traintype.find_elements(By.CLASS_NAME,"btn.btn-lg.btn-linear")
for i in range(len(Traintype_list)):
    Traintype_list[i].click()
#小小機器人
Captcha_frame = driver.find_element(By.XPATH,"//*[@id='"'recaptcha'"']/div/div/div/iframe")
switch_frame(Captcha_frame)
Captcha_check = driver.find_element(By.XPATH,"//*[@id='"'recaptcha-anchor'"']/div[1]")
Captcha_check.click()

time.sleep(3)
driver.close() 