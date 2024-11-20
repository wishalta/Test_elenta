import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ElentaTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.wait = WebDriverWait(self.driver, 10)
        self.acceptCookies()

    def acceptCookies(self):
        self.driver.get("https://elenta.lt")
        self.driver.find_element(By.CLASS_NAME, 'fc-cta-consent').click()