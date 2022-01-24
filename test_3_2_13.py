from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_registration1(self):
        link = " http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        name = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        name.send_keys("Diana")
        last = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        last.send_keys("Malysheva")
        email = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        email.send_keys("Mail")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, msg="error")

    def test_registration2(self):
        link = " http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        name = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        name.send_keys("Diana")
        last = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        last.send_keys("Malysheva")
        email = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        email.send_keys("Mail")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, msg="error")


if __name__ == "__main__":
    unittest.main()
