import time
import pytest

from .utils.pages.product_page import ProductPage

@pytest.mark.parametrize('offer_number', [x for x in range(0, 7)] + [pytest.param(7, marks=pytest.mark.xfail(reason="Bug in alert"))] + [x for x in range(8, 10)])
def test_guest_can_add_item_to_cart(browser, offer_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()