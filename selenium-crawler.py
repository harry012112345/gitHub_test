from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#options=Options()
options = webdriver.ChromeOptions()
options.chrome_executable_path="C:\\Users\Harry\Desktop\python-training\chromedriver.exe"
driver=webdriver.Chrome(options=options)
driver.get("https://www.ptt.cc/bbs/Stock/index.html")
