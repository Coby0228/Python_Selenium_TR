from script import *
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

# def get_question_id_by_target_name(target_name):
#     logger.debug(f'try to get question id by {target_name}')
#     question_id = CAPTCHA_TARGET_NAME_QUESTION_ID_MAPPING.get(target_name)
#     logger.debug(f'question_id {question_id}')
#     return question_id

#chrome setting    
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches',['enable-automation'])
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query")

MyID_path = driver.find_element(By.ID,"pid")
MyID_path.send_keys(MyID)
Start_Station_path = driver.find_element(By.ID,"startStation")
Start_Station_path.send_keys(Start_Station)
End_Station_path = driver.find_element(By.ID,"endStation")
End_Station_path.send_keys(End_Station)
Button_bytime = driver.find_element(By.XPATH,"//*[@id='"'queryForm'"']/div[1]/div[1]/div[6]/div[2]/label[2]")
Button_bytime.click()

Start_time_path = Select(driver.find_element(By.ID,"startTime1"))
Start_time_path.select_by_value(Start_time)
End_time_path = Select(driver.find_element(By.ID,"endTime1"))
End_time_path.select_by_value(End_time)

Traintype = driver.find_element(By.CLASS_NAME,"trainType")
Traintype_list = Traintype.find_elements(By.CLASS_NAME,"btn.btn-lg.btn-linear")
for i in range(len(Traintype_list)):
    Traintype_list[i].click()
#小小機器人 1
Captcha_frame = driver.find_element(By.XPATH,"//*[@id='"'recaptcha'"']/div/div/div/iframe")
driver.switch_to.default_content()
driver.switch_to.frame(Captcha_frame)
Captcha_check = driver.find_element(By.XPATH,"//*[@id='"'recaptcha-anchor'"']/div[1]")
Captcha_check.click()
time.sleep(2)
#小小機器人 2
driver.switch_to.default_content()
Captcha_inner_frame = driver.find_element(By.XPATH,"/html/body/div[8]/div[4]/iframe")
driver.switch_to.frame(Captcha_inner_frame)
#Label
AI_type = driver.find_element(By.XPATH,"//*[@id='"'rc-imageselect'"']/div[2]/div[1]/div[1]/div/strong").text
img_width = driver.find_element(By.CLASS_NAME,"rc-image-tile-33").get_attribute("naturalWidth")
img_element_url = driver.find_element(By.CLASS_NAME,"rc-image-tile-33").get_attribute("src")
with open("test.jpeg","wb") as f:
    f.write(requests.get(img_element_url).content)

time.sleep(6)
driver.close() 