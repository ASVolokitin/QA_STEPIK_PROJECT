from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.XPATH, "//*[contains(@href, 'basket')]")

class BasketPageLocators():
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_CARD_BOOK_TITLE = (By.CSS_SELECTOR, '.product_main > h1')
    POPUP_ADDED_TO_CART_BOOK_TITLE = (By.XPATH, "//*[@id='messages']//strong[1]")
    HEADER_BASKET_TOTAL = (By.XPATH, "//header[contains(@class, 'header')]//div[contains(@class, 'basket')]")
    POPUP_BASKET_TOTAL = (By.CSS_SELECTOR, '#messages > div:nth-child(3) .alertinner')
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, '#messages .alert-success')
