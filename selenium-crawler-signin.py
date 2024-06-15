from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options=Options()
options.chrome_executable_path="C:\\Users\Harry\Desktop\python-training\chromedriver.exe"

driver=webdriver.Chrome(options=options)
driver.get("https://leetcode.com/accounts/login/")




#driver.close()