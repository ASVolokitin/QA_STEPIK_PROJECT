from .base_page import BasePage
from ..locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_products_in_basket(self) -> None:
        assert not self.is_element_present(*BasketPageLocators.BASKET_ITEMS)
    
    def should_be_empty_basket_message(self) -> None:
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE)