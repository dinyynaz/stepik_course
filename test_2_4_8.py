import math
import os
from selenium.webdriver.support import expected_conditions as EC


from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # время ожидания работы счетчика, id кнопки на котурую надо кликнуть и значение для сравнения
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_id('book')
    button.click()

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text  # взять элемент x
    y = calc(x)  # у это решение функции от x
    y_element = browser.find_element_by_id('answer')
    y_element.send_keys(y)

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()  # Решение функции и отправка овета


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

