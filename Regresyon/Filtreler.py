from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from openpyxl import Workbook,load_workbook
import pytest
import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

driver = webdriver.Chrome('C:/Users/HP/Desktop/Oğuz/workfile/driver/chromedriver.exe')
driver.get('http://10.98.228.146/atlasui/login')
driver.maximize_window()


def enter():
    global url
    #gelismis = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[id=details-button]"))).click()
    #git = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[id='proceed-link']"))).click()
    login = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[placeholder='Username']")))
    password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[placeholder='Password']")))
    login.send_keys('TestUser')
    password.send_keys('TestUser')
    gitlogin = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[class='btn btn-primary btn-block']")))
    gitlogin.click()
    #Loginalready = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(.,"Login")]')))
    print(WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(.,"Login")]'))).is_displayed())
    try:
        if WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(.,"Login")]'))).is_displayed() :
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(.,"Login")]'))).click()
    except TimeoutException as e:
        pass

    element1=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'ATLAS')]")))
    url=driver.current_url #Giriş yaptıktan sonra gelen dashboard sayfası
#    print(url)
enter()
def dealmanagement():
    global url2
    element1=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'ATLAS')]"))).click() #Yuhiiiiii buldummm Thank Selenium Ide
    element2=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'VOD Operations')]"))).click()
    element3=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//span[contains(.,'Deal Management')]"))).click()
    contractelement = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(.,'Contract Management')]")))#Sayfadaki bir element
    url2=driver.current_url
dealmanagement()

def contract():
    global page
    cntname=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='contractName']"))) #Yuhiiiiii buldummm Thank Selenium Ide
    cntname.click()
    cntname.send_keys('Test')
    sleep(0.5)
    search=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(.,'Filter')]"))).click()
    page = urllib.request.urlopen('http://10.98.228.146/atlasui/cms/dealing/contract').read()


contract()

def Beautifull():
    sleep(1)
    soup = bs(page,'html.parser')
    print(soup.body.findAll('app-root'))
    print('############################')
    print(soup)
    #names= soup.body.findAll('')
    # fuction_name = re.findall('scope="row"',str(names))
    # print(fuction_name)
    # # function_usage =[]
    #
    # for item in names :
    #     item = item.text
    #     function_usage.append(item)
    #
    # print(function_usage)
Beautifull()
