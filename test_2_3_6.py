import math
import os

from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

    browser.switch_to.window(browser.window_handles[1]) #переключитьна на вторую вкладку

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
