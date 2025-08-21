import time

from .utils.pages.product_page import ProductPage


def test_guest_can_add_item_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()