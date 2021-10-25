import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

PATH="C:/Program Files (x86)/chromedriver.exe"

driver=webdriver.Chrome(PATH)

driver.maximize_window()
driver.get('https://web.whatsapp.com')

action=ActionChains(driver)

time.sleep(7)


myDict={}

i=1

xyz=driver.find_elements(By.CLASS_NAME,"zoWT4")
for x in xyz:
    myDict[str(i)]=x.text
    i=i+1

for keys in myDict:
    print(keys,myDict[keys])

choice=input("Enter your choice : ")

#Click on chat
driver.find_element(By.XPATH,f"//span[@title='{myDict[choice]}']").click()
time.sleep(2)
#For selecting emojis pannel
driver.find_element(By.CLASS_NAME,"l9Mer").click()
time.sleep(2)
#For selecting stickers
driver.find_element(By.CLASS_NAME,"_1Eec4").click()
time.sleep(2)
#For opening Fav pannel
select_fav=driver.find_elements(By.CLASS_NAME,"_3hl6E")[1].click()
time.sleep(2)



# Sticker spam
while True:
    # Enter sticker number(0 indexed) in [] you want to spam
    driver.find_elements(By.CLASS_NAME,"_2elZc")[0].click()

#Text spam(Glitch)
# while True:
#     xyz=driver.find_element(By.CLASS_NAME,"p3_M1")
#     xyz.send_keys("It this shit working?")
#     xyz.send_keys(Keys.RETURN)
#     time.sleep(1)


#Text spam ezzzz
# import pyautogui 
# import webbrowser as wb
# import time
# wb.open("https://web.whatsapp.com/")
# time.sleep(15)
# for i in range(40): 
#     pyautogui.write("hahaha")
#     pyautogui.press("enter")