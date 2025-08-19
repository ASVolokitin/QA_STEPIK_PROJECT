from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
    
    def is_element_present(self, searching_method, target):
        try:
            WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((searching_method, target)))
        except TimeoutException:
            return False
        return True
