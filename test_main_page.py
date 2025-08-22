import pytest
import time

from .utils.pages.main_page import MainPage
from .utils.pages.login_page import LoginPage
from .utils.pages.basket_page import BasketPage
from .utils.constants import MAIN_PAGE_LINK


@pytest.mark.skip()
def test_guest_can_go_to_login_page(browser):
    link = MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket_message()
    basket_page.should_not_be_products_in_basket()


@pytest.mark.skip()
def test_guest_should_see_login_link(browser):
    link = MAIN_PAGE_LINK
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()