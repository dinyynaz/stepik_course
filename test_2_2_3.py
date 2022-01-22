import select
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('num1')
    x = x_element.text
    y_element = browser.find_element_by_id('num2')
    y = y_element.text
    sum1 = str(str(int(x) + int(y)))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum1)

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
