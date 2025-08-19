from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser: webdriver, url: str, timeout:5) -> None:
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.browser.implicitly_wait(timeout)

    def open(self) -> None:
        self.browser.get(self.url)
    
    def is_element_present(self, searching_method: By, target: str) -> bool:
        try:
            WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((searching_method, target)))
        except TimeoutException:
            return False
        return True
