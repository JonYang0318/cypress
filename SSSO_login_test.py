from sre_parse import FLAGS
from this import d
from xmlrpc.client import Fault
from click import option
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
import allure
from selenium.webdriver.support.ui import Select
import pickle
import time
from selenium.webdriver.chrome.options import Options
import requests as req
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import pymysql
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
db_setting={
 "host": "192.168.90.45",
    "port": 30037,
    "user": "teconsole",
    "password": "teconsole!",
    "db": "TE_SSO",
    "charset": "utf8"
}

@allure.title('更改嚴謹/簡訊登入')
@pytest.mark.run(order=1)
def test_update_setting(): 
      
 conn = pymysql.connect(**db_setting)
 with conn.cursor() as cursor:

    mem ="UPDATE telligent_member.company_setting SET login_type = '2',terms_policy_type = '1' WHERE (id = '73efafaa-609e-11ed-aad0-0242ac170004');"
    cursor.execute(mem)
    conn.commit()
  


  
@allure.testcase('https://tpp07026.atlassian.net/wiki/spaces/APITEST/pages/8978433')
@allure.title('安裝瀏覽器')
@pytest.mark.run(order=2)
def test_setUp(): 
        global driver
        chrome_options = Options()
        chrome_options.page_load_strategy = 'eager'
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
        driver.set_window_size(1920,1000)
        pass
    #執行TestCase腳本
@allure.story('進入SSO頁面')
@pytest.mark.run(order=3)
def test_Visit():
       
        driver.get("https://qa.telli.cc/consumer/oauth2/login?ReturnUrl=%2Fconsumer%2Foauth2%2Fconnect%2Fauthorize%3Fclient_id%3Dauthorization-code-client%26redirect_uri%3Dhttps%253A%252F%252Fqa.telli.cc%252Fconsumer%252Fmember%252Fcallback%26response_type%3Dcode%26scope%3D%2520%26state%3D3e390076cc644b3788ed41ed39f2d69d%26code_challenge%3DIlR89jtBkm3IK3MQ4GEat-rfLQAIfsyZ8pRaw_nYbkg%26code_challenge_method%3DS256%26response_mode%3Dquery%26companyId%3D97d288ac-5f17-11ed-afa6-00ffaf2156c9")
        time.sleep(3)
        x = driver.title 
        assert x =="簡訊登入"
        # visit=driver.get_screenshot_as_png()
        # allure.attach(visit, '截圖', allure.attachment_type.PNG)
       

@allure.story('登入頁面輸入手機號碼')    
@pytest.mark.run(order=4)
def test_Login():
        time.sleep(5)
        search =driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/div/div/div[1]/form/label")
        search.send_keys("0966548485")
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/main/div/div[2]/div/div/div[1]/form/button').click()
        time.sleep(5)
        
        

@allure.story('確認驗證碼能是否正常/並且確認')
@pytest.mark.run(order=5)
def test_DB_link():

 conn = pymysql.connect(**db_setting)
 with conn.cursor() as cursor:

    command ="select code From telligent_member.member_captcha ORDER BY expired_time desc LIMIT 1;"
    cursor.execute(command)
    result =cursor.fetchone()
    print(result) 
 driver.find_element(By.XPATH,'/html/body/div[1]/div/div/main/div/div[2]/div/div/div[1]/form/div/label/div/div[1]/div/input').send_keys(result)

          
        

@allure.story('彈跳視窗確認')   
@pytest.mark.run(order=6)
def test_messgaeConfirm():
        time.sleep(8)
      
        
        btn=driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/button[2]/span[2]/span')
        ActionChains(driver).double_click(btn).perform()
        time.sleep(2)
        popup=driver.get_screenshot_as_png()
        allure.attach(popup, '確認輸入驗證碼', allure.attachment_type.PNG)



@allure.story('嚴謹條款確認')   
@pytest.mark.run(order=7)
def test_checkMemberBargain():
        
        #移動至底部
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        #qusar動態套件點選方法
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/footer/div[1]/div[1]/div[2]")))
        driver.find_element(By.XPATH,'/html/body/div[1]/div/footer/div[1]/div[1]/div[2]').click()
        driver.find_element(By.XPATH,'/html/body/div[1]/div/footer/div[1]/div[2]/div/button[2]/span[2]').click()
        time.sleep(10)
        # popup=driver.get_screenshot_as_png()
        # allure.attach(popup, '跳轉畫面驗證', allure.attachment_type.PNG)
        # driver.find_element(By.XPATH,'/html/body/div[1]/div/footer/div[1]/div[2]/div/button[2]/span[2]').click()
         
@allure.story('信箱和姓名填寫')   
@pytest.mark.run(order=8)
def test_MemberAccount():
        #姓名/信箱
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/main/div/div[2]/div/div/div/form/label[2]/div/div[1]/div/input').send_keys('王小明')
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/main/div/div[2]/div/div/div/form/label[3]/div/div[1]/div/input').send_keys('sele@55.com')
        #日期選擇
        time.sleep(5)
@allure.story('選擇日期')   
@pytest.mark.run(order=9)
def test_MemberClander():
        #打開日歷
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/main/div/div[2]/div/div/div/form/label[4]/div/div[1]/div[1]/i').click()
        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div/div[1]/div/div[3]/div/div[9]/button/span[2]/span")))
        driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div[1]/div/div[3]/div/div[9]/button/span[2]/span').click()
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div/button/span[2]/span")))
        driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div[2]/div/button/span[2]/span').click()
        time.sleep(1)

        
@allure.story('確定註冊')   
@pytest.mark.run(order=10)
def test_register():
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/main/div/div[2]/div/div/div/form/div[3]/div[4]/label/div/div[1]/div[2]/i').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/div[2]/div")))
    driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[1]/div[2]/div').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/main/div/div[2]/div/div/div/form/button/span[2]').click()



@allure.story('執行結束關閉瀏覽器')   
@pytest.mark.run(order=11)
def test_ShoutDown():
   
        driver.close()



@allure.story('DletMember')
def test_deleteMember():
 
 conn = pymysql.connect(**db_setting)
 with conn.cursor() as cursor:

    mem ="DELETE From telligent_member.member ORDER BY registration_time desc LIMIT 1;"
    cursor.execute(mem)
    conn.commit()
   

@allure.story('DleAco')
def test_deleteAccount():

 conn = pymysql.connect(**db_setting)
 with conn.cursor() as cursor:

    aco ="DELETE FROM `telligent_member`.`member_account` ORDER BY creation_time desc LIMIT 1;"
    cursor.execute(aco)
    conn.commit()
    data = cursor.fetchall()
    print(data)
    


@allure.story('Dlepro')
def test_deleteProfile():
 conn = pymysql.connect(**db_setting)
 with conn.cursor() as cursor:

    pf ="DELETE From telligent_member.member_profile_basic ORDER BY creation_time desc LIMIT 1;"
    cursor.execute(pf)
    conn.commit()
    data = cursor.fetchall()
    print(data)
    

@allure.story('DleTE')
def test_deleteETProfile():
 conn = pymysql.connect(**db_setting)
 with conn.cursor() as cursor:

    ext ="DELETE From telligent_member.member_extended_profile ORDER BY creation_time desc LIMIT 1;"
    cursor.execute(ext)
    conn.commit()
    data = cursor.fetchall()
    print(data)
    conn.close()


#reading report  pytest SSSO_login_test.py --alluredir ./result
#create report  allure serve SSSO_login_test.py ./result