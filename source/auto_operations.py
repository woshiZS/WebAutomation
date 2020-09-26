from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class MyDriver():
    '''Create a webdriver and finish your task'''
    def __init__(self,PATH):
        # you can add headingless options on your own
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--headless")
        
        # Do not use this port cause it may be banned on your pc.
        # chromeOptions.add_argument("--remote-debugging-port=9222")
        chromeOptions.add_argument('--no-sandbox')
        prefs = {"profile.default_content_setting_values.geolocation" :2}
        chromeOptions.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome(PATH,options=chromeOptions)

    def login(self,name,pwd):
        '''Just for login, you can also use cookies here'''
        self.driver.get("https://healthreport.zju.edu.cn/ncov/wap/default/index")
        elem = self.driver.find_element_by_tag_name('label')
        print(elem.text)
        username = WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.NAME,"username"))
        )
        #login first
        password = self.driver.find_element_by_name("password")
        button = self.driver.find_element_by_id("dl")
        username.clear()
        username.send_keys(name)
        password.clear()
        password.send_keys(pwd)
        button.click()

    def fill_forms(self,item):
        '''filling the forms'''
        WebDriverWait(self.driver,10).until(
        EC.presence_of_element_located((By.XPATH,"//ul/li[18]/div[1]/div[1]/div[1]"))
        ).click()
        print("成功完成登录")

        #是否出入境
        btn = self.driver.find_element_by_xpath("//ul/li[25]/div[1]/div[1]/div[2]/span[1]")
        print(btn.text)
        btn.click()

        #最后填写的是否确认
        btn = self.driver.find_element_by_xpath("//ul/li[37]/div[1]/div[1]/div[1]/span[1]")
        print(btn.text)
        btn.click()

        #redundant code
        # btn = driver.find_element_by_name("sfqrxxss")
        # btn.click()

        #Ip
        area = self.driver.find_element_by_name("area")
        btn = area.find_element_by_tag_name("input")
        btn.click()

        #获取到提示窗体
        confirm = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(
            (By.XPATH,"/html/body/div[4]/div[1]/div[2]/div[1]")
        ))
        confirm.click()

        Ip = self.driver.find_element_by_name("ip")

        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//div[1]/div[1]/select[1]/option[@value='{item[3]}']"))).click()

        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//div[1]/div[1]/select[2]/option[@value='{item[4]}']"))).click()

        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//div[1]/div[1]/select[3]/option[@value='{item[5]}']"))).click()

        # wait for implementation,cause if your location is different from yesterday's. The js will show another form.

        submit = self.driver.find_element_by_link_text("提交信息 Submit information")
        submit.click()

        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//body/div[5]/div[1]/div[2]/div[2]"))).click()
        
        print(f'学号{item[0]}成功完成打卡')


    def quit(self):
        self.driver.quit()