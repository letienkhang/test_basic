import logging
import time
import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver
from pages.same_price.locator import ParityPriceLocators


class SamePricePage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    def click_search(self):
        self.elementClick(ParityPriceLocators.INPUT_SEARCH_BUTTON, locatorType="xpath")

    def enter_search(self, product_code):
        self.sendKeysNotEnter(data=product_code, locator=ParityPriceLocators.INPUT_SEARCH, locatorType="xpath")

    def choose_item_first(self):
        self.elementClick(ParityPriceLocators.FIRST_PRODUCT, locatorType="xpath")

    def getPrice_of_product(self):
        code_text = self.getText(ParityPriceLocators.CODE_PRODUCT_ELEMENT, locatorType="xpath")
        price_text = self.getText(ParityPriceLocators.GET_PRICE_PRODUCT_ELEMENT, locatorType="xpath")
        compare_at_price_text = self.getText(ParityPriceLocators.COMPARE_AT_PRICE_ELEMENT,locatorType="xpath") if self.isElementPresent(
            ParityPriceLocators.COMPARE_AT_PRICE_ELEMENT, locatorType="xpath") else "-"
        discount_text = self.getText(ParityPriceLocators.DISCOUNT_ELEMENT,
                                     locatorType="xpath") if self.isElementPresent(
            ParityPriceLocators.DISCOUNT_ELEMENT, locatorType="xpath") else "-"
        return code_text, price_text, compare_at_price_text, discount_text

    def close_popup_if_present(self):
        if self.isElementPresent(ParityPriceLocators.POPUP, locatorType="xpath"):
            self.elementClick(ParityPriceLocators.POPUP_CLOSE_BUTTON, locatorType="xpath")
            self.log.info("Closed the popup")

    def search_same_price(self, product_code, log_data):
        self.log.info(f"Starting search for product code: {product_code}")
        self.close_popup_if_present()  # Close popup if it appears
        self.click_search()
        time.sleep(4)
        self.enter_search(product_code=product_code)
        self.close_popup_if_present()  # Close popup if it appears
        time.sleep(5)
        self.choose_item_first()
        self.close_popup_if_present()  # Close popup if it appears
        time.sleep(4)
        code_text, price_text, compare_at_price_text, discount_text = self.getPrice_of_product()
        log_data.append([product_code, code_text, price_text, compare_at_price_text, discount_text])
