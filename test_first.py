from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

def calc(x):
   return str(math.log(abs(12 * math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    
    PriceHouse = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), '$100')
        )
    
    Button1 = browser.find_element(By.CSS_SELECTOR, "#book")
    Button1.click()

    button2 = browser.find_element(By.CSS_SELECTOR, "#solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)

    num1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    num1 = num1.text
    num1 = calc(num1)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(num1)

    button2.click()


    time.sleep(1)

finally:

    time.sleep(20)
    browser.quit()
