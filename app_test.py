from appium import webdriver
import time
import allure
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import pymysql
import pytest
from appium.webdriver.common.touch_action import TouchAction
desired_caps ={
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "deviceName": "SM-G965N",
  "noReset": True,
  "autoGrantPermissions ": True,
  "appPackage":"com.android.launcher3",
  "appActivity":".launcher3.Launcher",
  'unicodeKeyboard': True,
  'resetKeyboard': True
}

db_setting={
 "host": "192.168.90.45",
    "port": 30037,
    "user": "teconsole",
    "password": "teconsole!",
    "db": "TE_SSO",
    "charset": "utf8"
}
@allure.title('更改寬鬆/一般註冊')
@pytest.mark.run(order=1)
def test_update_setting(): 
      
 conn = pymysql.connect(**db_setting)
 with conn.cursor() as cursor:

    mem ="UPDATE telligent_member.company_setting SET login_type = '2',terms_policy_type = '1' WHERE (id = '73efafaa-609e-11ed-aad0-0242ac170004');"
    cursor.execute(mem)
    conn.commit()
    
@pytest.mark.run(order=1)
def setup():
  
  global driver
  driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
  driver.start_activity("com.android.chrome","com.google.android.apps.chrome.Main")


@pytest.mark.run(order=2)
def test_running_test():
#driver.background_app(5)
  driver.find_element(by=AppiumBy.ID,value='com.android.chrome:id/home_button').click()
  time.sleep(3)
  el=driver.find_element(by=AppiumBy.ID, value="com.android.chrome:id/search_box_text")
  el.send_keys('https://qa.telli.cc/consumer/oauth2/login?ReturnUrl=%2Fconsumer%2Foauth2%2Fconnect%2Fauthorize%3Fclient_id%3Dauthorization-code-client%26redirect_uri%3Dhttps%253A%252F%252Fqa.telli.cc%252Fconsumer%252Fmember%252Fcallback%26response_type%3Dcode%26scope%3D%2520%26state%3D3e390076cc644b3788ed41ed39f2d69d%26code_challenge%3DIlR89jtBkm3IK3MQ4GEat-rfLQAIfsyZ8pRaw_nYbkg%26code_challenge_method%3DS256%26response_mode%3Dquery%26companyId%3D97d288ac-5f17-11ed-afa6-00ffaf2156c9')
  time.sleep(3)
  popup=driver.get_screenshot_as_png()
  allure.attach(popup, '確認進入SSO登入頁', allure.attachment_type.PNG)
  driver.find_element(by=AppiumBy.ID, value="com.android.chrome:id/line_1").click()
  time.sleep(3)


@pytest.mark.run(order=3)
def test_input():

  driver.find_element(AppiumBy.CLASS_NAME,'android.widget.EditText').send_keys('0966548485')
 
  tel=driver.get_screenshot_as_png()
  allure.attach(tel,'輸入電話號碼', allure.attachment_type.PNG)
  driver.find_element(AppiumBy.CLASS_NAME,'android.widget.Button').click()

@pytest.mark.run(order=4)
def test_vertify():
 time.sleep(5)
 conn = pymysql.connect(**db_setting)
 with conn.cursor() as cursor:

    command ="select code From telligent_member.member_captcha ORDER BY expired_time desc LIMIT 1;"
    cursor.execute(command)
    result =cursor.fetchone()
    print(result) 
 time.sleep(3)
 driver.find_element(AppiumBy.CLASS_NAME,'android.widget.EditText').send_keys(result)
 time.sleep(3)

@pytest.mark.run(order=5)
def test_messgaeConfirm():
        time.sleep(4)
        driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.Button[3]').click()
        size = driver.get_window_size()
        print("裝置螢幕大小：", size)
        time.sleep(3)
        start_x = 1152
        start_y = 500
        end_x = 1185
        end_y = 182
        driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
        driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
        driver.swipe(start_x, start_y, end_x, end_y, duration=200)
        driver.swipe(start_x, start_y, end_x, end_y, duration=200)
        driver.swipe(start_x, start_y, end_x, end_y, duration=200)
        # s= driver.find_element(AppiumBy.CLASS_NAME,'android.widget.TextView')
        # m= driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.widget.TextView')
        # driver.scroll(s,m)

        driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]/android.widget.CheckBox/android.view.View/android.widget.TextView').click()
        time.sleep(2)
        btnClk=driver.get_screenshot_as_png()
        allure.attach(btnClk,'輸入電話號碼', allure.attachment_type.PNG)
        driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[3]/android.widget.Button[2]').click()

@pytest.mark.run(order=6)
def test_prfile():
      driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.widget.EditText').send_keys('jimmy')
      driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.view.View[1]/android.widget.TextView').click()
      time.sleep(2)
      #打開月曆
      driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.view.View[10]/android.view.View/android.view.View[8]/android.widget.Button').click()
      driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View/android.widget.Button').click()
      time.sleep(1)
      #往下滑動
      start_x = 1152
      start_y = 500
      end_x = 1185
      end_y = 182
      driver.swipe(start_x, start_y, end_x, end_y, duration=100)
      time.sleep(3)
      driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[7]/android.view.View/android.view.View/android.view.View').click()
      time.sleep(1)
      #旅遊地區選擇
      driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.widget.ListView/android.view.View/android.view.View[1]/android.widget.TextView[2]').click()
    
      time.sleep(2)
      driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.TextView').click()
      #送出
      driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button').click()
      reSlut=driver.get_screenshot_as_png()
      allure.attach(reSlut,'輸入電話號碼', allure.attachment_type.PNG)


      

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


##reading report  pytest app_test.py --alluredir ./result
#create report  allure serve app_test.py ./result