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
import logging

driver = webdriver.Chrome('C:/Users/HP/Desktop/Oğuz/workfile/driver/chromedriver.exe')
driver.get('https://itveas.tmp.tivibu.com.tr/iptvepg/web/pc/index.jsp')
driver.maximize_window()


def enter():
    giris = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div/div/nav/div/div[2]/div[2]/a/div/span[1]'))).click()
    teksifre =  WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="login"]'))).click()
    username =  WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="inp1"]/input'))).send_keys('oguzhan.alyaz3')
    password =  WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="pwd1"]'))).send_keys('iviac9lE')
    login =  WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="bg_img"]/div/div[1]/div[2]/div[5]/span'))).click()
    #buraya kadar login
    profile =  WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div/section/div[2]/div[2]/div/div[1]/img'))).click()
    profilesifre =  WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="profileListPin2"]'))).send_keys('1111')
    giris = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="profileListForm"]/div'))).click()

enter()

def channel():
    live = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//*[text()='Canlı TV']"))).click()

# Alttaki kısım kanal gezsin diye bir class oluşturulabilir (wanderaround)

    # try:
    #     for i in range(1,20,1):
    #         print(i)
    #         epg =WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//*[local-name()='div'][@title='İzle'])["+'{}'.format(i)+"]"))).click()
    #         sleep(5)
    # except Exception as e:
    #     raise
    kanal=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//div[@class='channel-logo'])[2]"))).click()
    sleep(10)
    datefilter = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='filter ']"))).click()
    changedate=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//div[@class='option'])[3]"))).click()
    sleep(10)
    epg =WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//*[local-name()='div'][@title='İzle'])[3]"))).click()#bu sayfanın yüklenmesini beklemek için
    sleep(10)
    video =WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//video[@id='video-player-true_html5_api'])[1]"))).click()
    sleep(1)
    pause =WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"(//button[@title='Durdur'])[1]"))).click()

channel()

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
