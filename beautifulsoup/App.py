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
import bs4
import pandas

driver = webdriver.Chrome('C:/Users/HP/Desktop/Oğuz/workfile/driver/chromedriver.exe')
driver.get('***')
driver.maximize_window()
try:
    gelismis = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[id=details-button]"))).click()
    git = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[id='proceed-link']"))).click()
except Exception as e:
    pass

print('Excelini alacağın sayfaya git')
value = input("To Continue press 1 \n")

if (value == '1'):

    print('1 e bastın')
    print('Burada labelların listesini çekip excele yazacak kısım yazılacak')

else :
    print('1 den başka birşeye bastın')
    print('burada farklı bir sayı girilirse browser kapatılacak ')
print('Devam ediyor')
