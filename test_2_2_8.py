import os

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    name = browser.find_element_by_xpath("//input[@placeholder='Enter first name']")
    name.send_keys("Diana")
    last = browser.find_element_by_xpath("//input[@placeholder='Enter last name']")
    last.send_keys("Malysheva")
    email = browser.find_element_by_xpath("//input[@placeholder='Enter email']")
    email.send_keys("diny.naz96@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
