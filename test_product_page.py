import time
import pytest

from .utils.pages.product_page import ProductPage
from .utils.constants import PRODUCT_PAGE_TEST_LINK

# @pytest.mark.parametrize('offer_number', [x for x in range(0, 7)] + [pytest.param(7, marks=pytest.mark.xfail(reason="Bug in alert"))] + [x for x in range(8, 10)])
def test_guest_can_add_item_to_cart(browser):
    link = PRODUCT_PAGE_TEST_LINK
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()

@pytest.mark.xfail(reason="Success messages appear after adding product to basket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = PRODUCT_PAGE_TEST_LINK
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_show_success_messages()

def test_guest_cant_see_success_message(browser):
    link = PRODUCT_PAGE_TEST_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_not_show_success_messages()

@pytest.mark.xfail(reason="Success messages do not dissappear")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = PRODUCT_PAGE_TEST_LINK
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_disappear_success_messages()
