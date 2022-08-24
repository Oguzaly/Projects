from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from openpyxl import Workbook,load_workbook
import pytest
from selenium.webdriver.common.action_chains import ActionChains
import random

driver = webdriver.Chrome('C:/Users/HP/Desktop/Oğuz/workfile/driver/chromedriver.exe')
driver.get('https://172.27.0.228/atlasui/login')
driver.maximize_window()

class namegenerate:
    # Aynı ismin birden fazla kullanılmasına izin verilmediği zaman bu kullanılabilir
    def __init__(self):
            name_length = 32
            characters ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
            name =""
            for index in range(name_length):
                name  = name + random.choice(characters)
            self.name = 'Test - ' + name
class check:
    #tastermessage da(sağ alt taraftaki) 200 olup olmadığına bakar
    def __init__(self):
        self.compare=driver.find_element(by=By.XPATH,value="//div[@id='toast-container']/div/div").text
        sleep(1)
        if self.compare in '200':
            self.compare = True
        else:
            self.compare = False
            sleep(2)
            driver.quit()
        self.donecompare=driver.find_element(by=By.XPATH,value="//div[@id='toast-container']/div/div").click()
        sleep(2.5)
class checkurl:
    #Sayfa Geçişlerinde url e bakar
    def __init__(self,element,url):
        self.element=element
        self.url=url
        sleep(1)
        if self.element in self.url:
            self.compare = True
        else:
            self.compare = False
            sleep(2)
            driver.quit()
        sleep(1)
class dropdown:
    def __init__(self,element,text):
        self.element = element
        self.text = text
        sleep(0.5)
        self.element.send_keys(self.text)
        sleep(0.5)
        self.element.send_keys(Keys.DOWN,Keys.ENTER)
        sleep(0.5)

def enter():
    global TestLogin
    global login
    gelismis = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[id=details-button]"))).click()
    git = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[id='proceed-link']"))).click()
    login = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[placeholder='Username']")))
    password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[placeholder='Password']")))
    login.send_keys('TestUser')
    password.send_keys('TestUser1')
    gitlogin = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[class='btn btn-primary btn-block']")))
    gitlogin.click()
    #loginalready = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(.,"Login")]'))).click()
    # #firstelement = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"span[class='font-weight-semibold font-size-14']")))
    # element1=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'ATLAS')]")))
    # TestLogin=driver.current_url #Giriş yaptıktan sonra gelen dashboard sayfas
    # TestLogin =checkurl(TestLogin,'https://172.27.0.228/atlasui/atlas/cms/dashboard')
    login=check()

enter()

class TestClass:
    def test_dealmanagement(self):
        assert login
