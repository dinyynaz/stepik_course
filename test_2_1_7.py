import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "  http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    y_element = browser.find_element_by_id('answer')
    y_element.send_keys(y)

    option1 = browser.find_element_by_css_selector("[type='checkbox']")
    option1.click()

    option2 = browser.find_element_by_id('robotsRule')
    option2.click()

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
