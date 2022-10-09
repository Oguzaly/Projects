from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from openpyxl import Workbook,load_workbook
import pytest
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
        sleep(1)
        self.compare=driver.find_element(by=By.XPATH,value="//div[@id='toast-container']/div/div").text
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
    try:
        gelismis = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[id=details-button]"))).click()
        git = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[id='proceed-link']"))).click()
    except Exception as e:
        pass
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
    TestLogin =checkurl(TestLogin,'***')
enter()
def dealmanagement():
    global TestDealManagement
    element1=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'ATLAS')]"))).click() #Yuhiiiiii buldummm Thank Selenium Ide
    element2=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'VOD Operations')]"))).click()
    element3=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'Deal Management')]"))).click()
    contractelement = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(.,'Contract Management')]")))#Sayfadaki bir element
    TestDealManagement=driver.current_url
    TestDealManagement = checkurl(TestDealManagement,'***')
dealmanagement()
def providermanagement():
    global toasteradd
    global providername
    global country
    name1 = namegenerate()
    Providerelement = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(.,'Provider Management')]"))).click()
    newprovider = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='New']"))).click()
    sleep(0.5)
    providername = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//input[@id='name'])[1]")))
    sleep(0.5)
    providername.send_keys(name1.name)
    sleep(0.5)
    country = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='country']"))).send_keys('Turkey')
    sleep(0.5)
    message = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//textarea[@id='notes'])[1]"))).send_keys('Test Provider 1')
    sleep(0.5)
    buttonadd = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Add']"))).click()
    toasteradd = check()
providermanagement()
def editprovider():
    global toasteredit
    name2 = namegenerate()
    editprovider=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//i[@title='Edit Provider'])[1]"))).click()
    sleep(0.5)
    providername = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//input[@id='name'])[1]"))).clear()
    sleep(0.5)
    providername = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//input[@id='name'])[1]"))).send_keys(name2.name)
    sleep(0.5)
    country = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='country']"))).clear()
    sleep(0.5)
    country = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='country']"))).send_keys('England')
    sleep(0.5)
    message = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//textarea[@id='notes'])[1]"))).clear()
    sleep(0.5)
    message = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//textarea[@id='notes'])[1]"))).send_keys('Test Provider 2')
    sleep(0.5)
    save = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='btn btn-warning !important']"))).click()
    toasteredit = check()
editprovider()

def deleteprovider():
    global deletetoaster
    deleteprovider = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//i[@title='Delete Provider'])[1]"))).click()
    sleep(0.5)
    delete = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Delete']"))).click()
    deletetoaster = check()
deleteprovider()
class TestClass:
    def test_Login(self):
        assert TestLogin
    def test_deal_management(self):
        assert TestDealManagement
    def test_toasteradd(self):
        assert toasteradd
    def test_toasteredir(self):
        assert toasteredit
    def test_deletetoaster(self):
        assert deletetoaster
