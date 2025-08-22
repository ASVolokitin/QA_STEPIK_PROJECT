import time
import pytest
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from ..locators import ProductPageLocators
from ..regular_expressions import COST_REGEX


class ProductPage(BasePage):

    def add_to_cart(self) -> None:
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()
        self.should_be_added_to_cart()
        self.should_be_updated_price()
    
    def should_be_added_to_cart(self) -> None:
        if not self.is_element_present(*ProductPageLocators.PRODUCT_CARD_BOOK_TITLE):
            pytest.fail("Book title in product card was not found")
        
        if not self.is_element_present(*ProductPageLocators.POPUP_ADDED_TO_CART_BOOK_TITLE):
            pytest.fail("Book title in 'added to cart' popup was not found")
        
        product_card_book_title = self.browser.find_element(*ProductPageLocators.PRODUCT_CARD_BOOK_TITLE).text
        alert_added_to_card_book_title = self.browser.find_element(*ProductPageLocators.POPUP_ADDED_TO_CART_BOOK_TITLE).text
        assert product_card_book_title == alert_added_to_card_book_title, f"according to popup, added {alert_added_to_card_book_title}, expected {product_card_book_title}"
        
    def should_be_updated_price(self) -> None:

        if not self.is_element_present(*ProductPageLocators.HEADER_BASKET_TOTAL):
            pytest.fail("Basket total price was not found in header")
        
        if not self.is_element_present(*ProductPageLocators.POPUP_BASKET_TOTAL):
            pytest.fail("Basket total price was not found in popup")

        header_basket_total_text = self.browser.find_element(*ProductPageLocators.HEADER_BASKET_TOTAL).text
        header_basket_total_price = re.findall(COST_REGEX, header_basket_total_text)[0]

        popup_basket_total_text = self.browser.find_element(*ProductPageLocators.POPUP_BASKET_TOTAL).text
        popup_basket_total_price = re.findall(COST_REGEX, popup_basket_total_text)[0]

        assert header_basket_total_price == popup_basket_total_price, f"different total basket prices in header and popup (in header: {header_basket_total_price}, in popup: {popup_basket_total_price})"
    
    def should_not_show_success_messages(self) -> None:
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES), f"success messages should not appear, found {len(self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES))}"
    
    def should_disappear_success_messages(self) -> None:
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), f"success_messages should disappear, found {len(self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES))}"