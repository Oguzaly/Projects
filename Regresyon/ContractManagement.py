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
driver.get('http://***')
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
        sleep(0.5)
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
    # try:
    #     gelismis = WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[id=details-button]"))).click()
    #     git = WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[id='proceed-link']"))).click()
    # except Exception as e:
    #     pass
    login = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[placeholder='Username']")))
    password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[placeholder='Password']")))
    login.send_keys('***')
    password.send_keys('***')
    gitlogin = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[class='btn btn-primary btn-block']")))
    gitlogin.click()
    try:
        loginalready = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(.,"Login")]'))).click()
    except Exception as e:
        pass
    #firstelement = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"span[class='font-weight-semibold font-size-14']")))
    element1=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'ATLAS')]")))
    TestLogin=driver.current_url #Giriş yaptıktan sonra gelen dashboard sayfas
    TestLogin =checkurl(TestLogin,'http://***')

enter()
def dealmanagement():
    global TestDealManagement
    element1=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'ATLAS')]"))).click() 
    element2=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'VOD Operations')]"))).click()
    element3=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'Deal Management')]"))).click()
    contractelement = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(.,'Contract Management')]")))#Sayfadaki bir element
    TestDealManagement = driver.current_url
    TestDealManagement = checkurl(TestDealManagement,'http://***')
dealmanagement()

def newcontractmanagement():
    global newcontractaddtoaster
    name3 = namegenerate()
    New=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='New Contract']"))).click() #Yuhiiiiii buldummm Thank Selenium Ide
    sleep(0.5)
    name=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//input[@id='name'])[1]"))).send_keys(name3.name,Keys.TAB)
    sleep(0.5)
    startDate=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//input[@name='startDate'])[2]"))).send_keys('25.05.2021',Keys.TAB)
    sleep(0.5)
    enddate=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//input[@name='endDate'])[2]"))).send_keys('25.06.2023',Keys.TAB)
    sleep(0.5)
    provider=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//input[@placeholder='Provider'])[2]")))
    dropdown(provider,'Provided By Oğuz')
    sleep(0.5)
    paymentType=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//select[@id='paymentType'])[1]")))
    sleep(0.5)
    paymentType=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//select[@id='paymentType'])[1]"))).send_keys(Keys.DOWN,Keys.TAB,Keys.TAB)
    sleep(0.5)
    textbox =WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//textarea[@name='comment'])[1]"))).send_keys('Test tastermessage 1')
    sleep(0.5)
    add=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Add']"))).click()
    toastercontractaddmessage = check()
newcontractmanagement()

# def editcontractmanagement():
#     global newcontractedittoaster
#     name3 = namegenerate()
#     New=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//i[@class='fa fa-edit fa-2x'])[1]"))).click() #Yuhiiiiii buldummm Thank Selenium Ide
#     sleep(0.5)
#     name=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='//input[@id='name']']"))).clear()
#     sleep(0.5)
#     name=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='//input[@id='name']']"))).send_keys(name3.name)
#     sleep(0.5)
#     startdate=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//input[@class='ng-tns-c9-61 ui-inputtext ui-widget ui-state-default ui-corner-all ng-star-inserted'])[1]"))).clear()
#     sleep(0.5)
#     startdate=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//input[@class='ng-tns-c9-61 ui-inputtext ui-widget ui-state-default ui-corner-all ng-star-inserted'])[1]"))).send_keys('25.06.2021')
#     sleep(0.5)
#     Enddate=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//input[@class='ng-tns-c9-62 ui-inputtext ui-widget ui-state-default ui-corner-all ng-star-inserted'])[1]"))).clear()
#     sleep(0.5)
#     Enddate=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//input[@class='ng-tns-c9-62 ui-inputtext ui-widget ui-state-default ui-corner-all ng-star-inserted'])[1]"))).send_keys('25.06.2023')
#     sleep(0.5)
#     provider=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//input[@class='ng-tns-c5-63 ui-inputtext ui-widget ui-state-default ui-corner-all ui-autocomplete-input ng-star-inserted'])[1]"))).clear()
#     sleep(0.5)
#     provider=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//input[@class='ng-tns-c5-63 ui-inputtext ui-widget ui-state-default ui-corner-all ui-autocomplete-input ng-star-inserted'])[1]"))).send_keys('Oğuzhan')
#     sleep(0.5)
#     paymentType=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//select[@id='paymentType'])[1]")))
#     dropdown(paymentType,'c')
#     textbox =WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//textarea[@name='comment'])[1]")))
#     sleep(0.5)
#     textbox =WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//textarea[@name='comment'])[1]"))).send_keys('Test tastermessage 1')
#     add=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//button[@class='btn btn-warning !important'])[1]"))).click()
#     newcontractedittoaster = check()
# editcontractmanagement()



class TestClass:
    def test_Login(self):
        assert TestLogin
    def test_dealmanagement(self):
        assert TestDealManagement
    def test_toasteradd(self):
        assert toastercontractaddmessage
    def test_toasteredit(self):
        assert newcontractedittoaster
    # def test_save(self):
    #     assert toastersave
    # def test_deletecontent(self):
    #     assert deletecontent
