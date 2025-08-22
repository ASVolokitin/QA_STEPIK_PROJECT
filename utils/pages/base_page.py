import math
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

from ..locators import BasePageLocators


class BasePage():
    def __init__(self, browser: WebDriver, url: str, timeout=5) -> None:
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def go_to_login_page(self) -> None:
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
    
    def is_disappeared(self, searching_method: str, target: str, timeout=4) -> bool:
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((searching_method, target)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, searching_method: str, target: str, timeout=5) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((searching_method, target)))
        except TimeoutException:
            return False
        return True
    
    def open(self) -> None:
        self.browser.get(self.url)
    
    
    def should_be_login_link(self) -> None:
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
