import time
import pytest

from .utils.pages.product_page import ProductPage
from .utils.pages.login_page import LoginPage
from .utils.constants import CODERS_AT_WORK_PRODUCT_PAGE, THE_CITY_AND_THE_STARS_PRODUCT_PAGE

# @pytest.mark.parametrize('offer_number', [x for x in range(0, 7)] + [pytest.param(7, marks=pytest.mark.xfail(reason="Bug in alert"))] + [x for x in range(8, 10)])
def test_guest_can_add_item_to_cart(browser):
    link = CODERS_AT_WORK_PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = THE_CITY_AND_THE_STARS_PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.xfail(reason="Success messages appear after adding product to basket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = CODERS_AT_WORK_PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_show_success_messages()

def test_guest_cant_see_success_message(browser):
    link = CODERS_AT_WORK_PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.should_not_show_success_messages()

def test_guest_should_see_login_link_on_product_page(browser):
    link = THE_CITY_AND_THE_STARS_PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    time.sleep(5)

@pytest.mark.xfail(reason="Success messages do not dissappear")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = CODERS_AT_WORK_PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_disappear_success_messages()
