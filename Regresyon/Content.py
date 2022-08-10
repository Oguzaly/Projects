from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from openpyxl import Workbook,load_workbook
import pytest
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome('C:/Users/HP/Desktop/Oğuz/workfile/driver/chromedriver.exe')
driver.get('https://172.27.0.228/atlasui/login')
driver.maximize_window()

def enter():
    global TestLogin
    gelismis = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[id=details-button]"))).click()
    git = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[id='proceed-link']"))).click()
    login = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[placeholder='Username']")))
    password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[placeholder='Password']")))
    login.send_keys('TestUser')
    password.send_keys('TestUser')
    gitlogin = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[class='btn btn-primary btn-block']")))
    gitlogin.click()
    loginalready = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(.,"Login")]'))).click()
    #firstelement = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"span[class='font-weight-semibold font-size-14']")))
    element1=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'ATLAS')]")))
    TestLogin=driver.current_url #Giriş yaptıktan sonra gelen dashboard sayfas
    if TestLogin in 'https://172.27.0.228/atlasui/atlas/cms/dashboard':
        TestLogin = True
    else:
        TestLogin = False
        sleep(2)
        driver.quit()

enter()
def dealmanagement():
    global TestDealManagement
    element1=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'ATLAS')]"))).click() #Yuhiiiiii buldummm Thank Selenium Ide
    element2=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'VOD Operations')]"))).click()
    element3=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'Deal Management')]"))).click()
    contractelement = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(.,'Contract Management')]")))#Sayfadaki bir element
    TestDealManagement = driver.current_url
    if TestDealManagement in 'https://172.27.0.228/atlasui/atlas/cms/dealing/contract':
        TestDealManagement = True
    else:
        TestDealManagement = False
        sleep(2)
        driver.quit()

dealmanagement()

def contentmanagement():
    global toasteradd
    wp = load_workbook('C:/Users/HP/Desktop/playground/Regresyon/DummyData/content.xlsx')
    ws = wp.active
    for i in range(2,3):
        contentmanagementtab=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(.,'Content Management')]"))).click()
        newcontent=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(.,'New Content ')]"))).click()
        contentname = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='contentName']"))).send_keys(ws['A{}'.format(i)].value)
        year = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='year']"))).send_keys(ws['B{}'.format(i)].value)
        sleep(1)
        contenttype = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='contenType']/span/input"))).send_keys('film',Keys.TAB,Keys.TAB,Keys.TAB)
        sleep(1)
        format = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Content Format']"))).send_keys('HD')
        sleep(1)
        format = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Content Format']"))).send_keys(Keys.DOWN,Keys.ENTER)
        driver.implicitly_wait(2)
        #element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='type']")))
        # actionChains = ActionChains(driver)
        # actionChains.move_to_element(element).click().perform()
        # actionChains.move_to_element(element).send_keys("Test",Keys.RETURN).perform()
        type = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='type']/span/input"))).send_keys('MOVIE',Keys.TAB)
        sleep(1)
        addbutton = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(.,' Add ')]"))).click()
        toasteradd=driver.find_element(by=By.XPATH,value="//div[@id='toast-container']/div/div").text #çıktısı 400 200 gibi değerler
        if toasteradd in '200':
            toasteradd = True
        else:
            toasteradd = False
            sleep(2)
            driver.quit()
        sleep(1)

#        xpath=//div[@id='toast-container']/div/div
contentmanagement()
class TestClass:
    def test_Login(self):
        assert TestLogin
    def test_dealmanagement(self):
        assert TestDealManagement
    def test_toasteradd(self):
        assert toasteradd
