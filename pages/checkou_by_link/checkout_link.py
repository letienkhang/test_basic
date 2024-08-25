import logging
import time
import sys
import utilities.custom_logger as cl
from selenium import webdriver
from base.selenium_driver import SeleniumDriver
from pages.checkou_by_link.locator import CheckoutLinkLocators


class CheckoutLinkBasic(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)


    def button_checkout(self):
        self.elementClick(CheckoutLinkLocators.BuyNowButton, locatorType="xpath")

    def buy_now(self):
        self.elementClick(CheckoutLinkLocators.ButtonBuyNowPDP, locatorType="xpath")

    def fill_info_customer(self):
        self.sendKeysNotEnter(data=CheckoutLinkLocators.DataName, locator=CheckoutLinkLocators.FillNameCus, locatorType="xpath")
        self.sendKeysNotEnter(data=CheckoutLinkLocators.DataPhone, locator=CheckoutLinkLocators.FillNumberCus, locatorType="xpath")

    def fill_address_customer(self):
        self.elementClick(CheckoutLinkLocators.AddressCus, locatorType="xpath")
        time.sleep(1)
        self.sendKeysNotEnter(data="An giang", locator=CheckoutLinkLocators.AddressCity, locatorType="xpath")
        time.sleep(1)
        self.elementClick(CheckoutLinkLocators.ChooseCity, locatorType="xpath")
        time.sleep(1)
        self.sendKeysNotEnter(data="Châu Thành", locator=CheckoutLinkLocators.AttributeError, locatorType="xpath")
        time.sleep(1)
        self.elementClick(locator=CheckoutLinkLocators.ChooseProvince, locatorType="xpath")
        time.sleep(1)
        self.sendKeysNotEnter(data="Thị trấn An Châu", locator=CheckoutLinkLocators.AttributeError, locatorType="xpath")
        time.sleep(1)
        self.elementClick(locator=CheckoutLinkLocators.ChooseProvince, locatorType="xpath")
        time.sleep(1)

        self.sendKeysNotEnter(data=CheckoutLinkLocators.DataDetailAddress, locator=CheckoutLinkLocators.DetailAddress, locatorType="xpath")
        self.sendKeysNotEnter(data="Test Đơn web", locator=CheckoutLinkLocators.NoteOrder, locatorType="xpath")

    def payment(self):
        self.elementClick(CheckoutLinkLocators.Payment, locatorType="xpath")

    def checkout_by_link(self):
        time.sleep(2)
        self.buy_now()
        time.sleep(4)
        self.button_checkout()
        time.sleep(4)
        self.fill_info_customer()
        time.sleep(2)
        self.fill_address_customer()
        time.sleep(1)
        self.payment()
        time.sleep(30)