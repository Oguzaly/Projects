from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#set browser log
dc = DesiredCapabilities.CHROME
dc['goog:loggingPrefs'] = { 'browser':'ALL' }
driver = webdriver.Chrome(executable_path="C:/Users/HP/Desktop/Oğuz/workfile/driver/chromedriver.exe",
desired_capabilities=dc)
#launch browser
driver.get ("https://www.tutorialspoint.com/index.htm")
#obtain with get_log()
for e in driver.get_log('browser'):
   print(e)
