# element = WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.ID, "myDynamicElement")) )




import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from trio import sleep_until

driver = webdriver.Chrome()

driver.get("https://store.steampowered.com/app/275850/No_Mans_Sky/")

Gabe=driver.find_element(By.CSS_SELECTOR,".apphub_AppName")
print(Gabe.text)

Cid=driver.find_element(By.CLASS_NAME,"price")
print(Cid.text)

Stars=driver.find_element(By.CSS_SELECTOR,".user_reviews_summary_row")
Stars.click()

time.sleep(2)

# Brawl=driver.find_element(By.CSS_SELECTOR,"._1Ovww-oSMFGzdKcmAmYwyG")
# Brawl.click()

Yop_Yan=driver.find_elements(By.CSS_SELECTOR,"._1zbKizfCRpoX2D_zOLQes0")
print(len(Yop_Yan))

for yop in Yop_Yan:
    print(yop.text)

Mairs=driver.find_element(By.CSS_SELECTOR,".game_header_image_full")
print(Mairs.get_attribute("src"))

# Warhammer=driver.find_element(By.CLASS_NAME,"_1zbKizfCRpoX2D_zOLQes0")
# print(Warhammer.text)

time.sleep(600)

