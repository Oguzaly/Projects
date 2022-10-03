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
    login.send_keys('TestUser')
    password.send_keys('TestUser')
    gitlogin = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[class='btn btn-primary btn-block']")))
    gitlogin.click()
    try:
        loginalready = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(.,"Login")]'))).click()
    except Exception as e:
        pass
    #firstelement = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"span[class='font-weight-semibold font-size-14']")))
    element1=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'ATLAS')]")))
    TestLogin=driver.current_url #Giriş yaptıktan sonra gelen dashboard sayfas
    TestLogin =checkurl(TestLogin,'https://172.27.0.228/atlasui/atlas/cms/dashboard')

enter()
def dealmanagement():
    global TestDealManagement
    element1=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'ATLAS')]"))).click() #Yuhiiiiii buldummm Thank Selenium Ide
    element2=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'VOD Operations')]"))).click()
    element3=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'Deal Management')]"))).click()
    contractelement = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(.,'Contract Management')]")))#Sayfadaki bir element
    TestDealManagement = driver.current_url
    TestDealManagement = checkurl(TestDealManagement,'https://172.27.0.228/atlasui/atlas/cms/dealing/contract')
dealmanagement()

def contentmanagement():
    global toasteradd
    isim1=namegenerate()
    contentmanagementtab=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(.,'Content Management')]"))).click()
    newcontent=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(.,'New Content ')]"))).click()
    contentname = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='contentName']"))).send_keys(isim1.name)
    year = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='year']"))).send_keys('2022')
    sleep(0.5)
    contenttype = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='contenType']/span/input")))
    dropdown(contenttype,'Film')
    format = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Content Format']")))
    dropdown(format,'HD')
    driver.implicitly_wait(2)
    #element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='type']")))
    # actionChains = ActionChains(driver)
    # actionChains.move_to_element(element).click().perform()
    # actionChains.move_to_element(element).send_keys("Test",Keys.RETURN).perform()
    type = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='type']/span/input")))
    dropdown(type,'MOVIE')
    addbutton = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(.,' Add ')]"))).click()
    #toasteradd=driver.find_element(by=By.XPATH,value="//div[@id='toast-container']/div/div").text#çıktısı 400 200 gibi değerler
    toasteradd = check()
contentmanagement()

def EditContent():
    global toastersave
    isim2 = namegenerate()
    contentmanagementtab=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(.,'Content Management')]"))).click()
    editcontent = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH ,"//tr[1]/td[10]/div/div[2]/a/i"))).click()
    contentname=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='name']")))
    sleep(1)
    contentname.clear()
    sleep(1)
    contentname.send_keys(isim2.name)#isim2.name
    savebutton = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(.,'Save')]"))).click()
    # toastersave=driver.find_element(by=By.XPATH,value="//div[@id='toast-container']/div/div").text
    toastersave = check()
EditContent()

def deletecontent():
    global deletecontent
    deletecontent =WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//tr[1]/td[10]/div/div[3]/a/i"))).click()
    deletebutton = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(.,'Delete')]"))).click()
    deletecontent = check()
deletecontent()
class TestClass:
    def test_Login(self):
        assert TestLogin
    def test_dealmanagement(self):
        assert TestDealManagement
    def test_toasteradd(self):
        assert toasteradd
    def test_save(self):
        assert toastersave
    def test_deletecontent(self):
        assert deletecontent
