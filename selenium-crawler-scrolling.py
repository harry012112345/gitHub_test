from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
options=Options()
options.chrome_executable_path="C:\\Users\Harry\Desktop\python-training\chromedriver.exe"

driver=webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0")

n=0
while n<3:
 driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 time.sleep(3)
 n+=1
titleTags=driver.find_elements(By.CLASS_NAME, "base-search-card__title")
for titleTag in titleTags:
    print(titleTag.text)
driver.close()