from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options=Options()
options.chrome_executable_path="C:\\Users\Harry\Desktop\python-training\chromedriver.exe"

driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.google.com/")
driver.save_screenshot("screenshot-google.png")
driver.get("https://www.ntu.edu.tw/")
driver.save_screenshot("screen-ntu.png")
driver.close()