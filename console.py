from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from openpyxl import Workbook,load_workbook
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest

dc = DesiredCapabilities.CHROME
dc['goog:loggingPrefs'] = { 'browser':'ALL' }

driver = webdriver.Chrome(executable_path="C:/Users/HP/Desktop/Oğuz/workfile/driver/chromedriver.exe",desired_capabilities=dc)
driver.get('https://172.27.0.228/atlasui/login')

def enter():
    global url
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
    url=driver.current_url #Giriş yaptıktan sonra gelen dashboard sayfası

enter()

def errormessage():
    element1=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'ATLAS')]"))).click() #Yuhiiiiii buldummm Thank Selenium Ide
#    go= WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'Trailer Workflow')]"))).click()
    go= WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'VFO Dashboard')]"))).click()
    dc = DesiredCapabilities.CHROME
    dc['goog:loggingPrefs'] = { 'browser':'ALL' }

    print(driver.get_log('browser'))

    for e in driver.get_log('browser'):
        print(e)


errormessage()
