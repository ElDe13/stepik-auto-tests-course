from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
	
    x = browser.find_element_by_css_selector("#num1")
    x = x.text
    num1 = int(x)
    y = browser.find_element_by_css_selector("#num2")
    y = y.text
    num2 = int(y)
    sum_el = num1 + num2
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text('%s' % sum_el) 
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
   	
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла