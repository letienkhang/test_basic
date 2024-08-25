import logging
import time

import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver
from pages.check_stock.locator import CheckStockLocators


class CheckStockAuto(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    def update_quality_plus(self):
        self.elementClick(CheckStockLocators.QUALITY_PLUS_BUTTON, locatorType="xpath")

    def add_to_cart(self):
        self.elementClick(CheckStockLocators.ADD_TO_CART, locatorType="xpath")

    def add_buy_now(self):
        self.elementClick(CheckStockLocators.BUY_NOW_BUTTON, locatorType="xpath")

    def button_checkout(self):
        self.elementClick(CheckStockLocators.CHECKOUT_BUTTON, locatorType="xpath")

    def fill_info_customer(self):
        self.sendKeysNotEnter(data=CheckStockLocators.DATANAME, locator=CheckStockLocators.FILLNAME_CUSTOMER, locatorType="xpath")
        self.sendKeysNotEnter(data=CheckStockLocators.DATAPHONE, locator=CheckStockLocators.FILLPHONECUSTOMER, locatorType="xpath")

    def payment(self):
        self.elementClick(CheckStockLocators.PAYMENT_BUTTON, locatorType="xpath")

    def fill_address_customer(self):
        self.elementClick(CheckStockLocators.ADDRESS_CUS, locatorType="xpath")
        self.sendKeysNotEnter(data="An giang", locator=CheckStockLocators.ADDRESS_CITY, locatorType="xpath")
        self.elementClick(CheckStockLocators.CHOOSE_CITY, locatorType="xpath")
        time.sleep(3)
        self.sendKeysNotEnter(data="Châu Thành", locator=CheckStockLocators.ADDRESS_CITY, locatorType="xpath")
        self.elementClick(locator=CheckStockLocators.CHOOSE_CITY, locatorType="xpath")
        time.sleep(3)
        self.sendKeysNotEnter(data="Thị trấn An Châu", locator=CheckStockLocators.ADDRESS_CITY, locatorType="xpath")
        self.elementClick(locator=CheckStockLocators.CHOOSE_CITY, locatorType="xpath")
        time.sleep(3)
        self.sendKeysNotEnter(data=CheckStockLocators.DATA_ADDRESS, locator=CheckStockLocators.DETAIL_CUSTOMER, locatorType="xpath")
        self.sendKeysNotEnter(data="Test Đơn web", locator=CheckStockLocators.NOTE_ORDER, locatorType="xpath")

    def buy_1st(self):
        self.update_quality_plus()
        time.sleep(2)
        self.add_to_cart()

    def buy_2nd(self):
        self.update_quality_plus()
        time.sleep(2)
        self.add_buy_now()
        time.sleep(2)
        self.button_checkout()
        time.sleep(2)
        self.fill_info_customer()
        time.sleep(2)
        self.fill_address_customer()
        time.sleep(2)
        self.payment()
