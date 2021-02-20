from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
	
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    button = browser.find_element_by_tag_name("button")#запускаем скрипт для проскролливания страницы
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    input2 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    input2.click()
    input3 = browser.find_element_by_css_selector("[for='robotsRule']")
    input3.click()
    button.click()
    assert True
   	
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла