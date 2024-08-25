import logging
import time
import sys
import utilities.custom_logger as cl
from selenium import webdriver
from base.selenium_driver import SeleniumDriver


class CheckoutBasic(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    _iconSearchMobile = "//div[@class='p-2']//*[name()='svg' and @class='cursor-pointer']"
    _logoYody = "//div[@class='flex flex-grow justify-center']"
    _inputSearchDesktop = "//input[@class=' input__l input--default pl-12 pr-12  w-full bg-yd-grey-light-2 hover:bg-yd-grey-light-3 rounded-[1.25rem] text-yd-body-2 focus:border-0  !rounded-[1.25rem] bg-[#F2F5F8] w-full md:h-12 truncate']"
    _textSearch = 'T-shirt Kid Bé'
    _itemProductFirstElement = "//div[@class='font-medium text-yd-label-3 xlg:text-[14px] text-yd-typo-title line-clamp-1 min-h-[22px] xlg:min-h-[24px] !font-[400] capitalize']"
    _buttonUpdateQualityPlus = "//button[@class='product-quantity-update-tool_button__dMhNl product-quantity-update-tool_button_right__MHn0c product-quantity-update-tool_button-normal__YS_yD  undefined']"
    _buttonAddCart = "//button[contains(@class, 'product-call-to-action_add-cart_button') and .//span[text()='Thêm vào giỏ']]"
    _iconRemovePopup = "//div[@class='flex items-center']//*[name()='svg' and @class='ml-auto rotate-45 cursor-pointer']"
    _buttonBuyNow = "//button[contains(@class, 'btn-extra-large') and contains(@class, 'product-call-to-action_buy-now_button') and .//span[text()='Mua ngay']]"
    _buttonClearText = "//button[@class='hover:scale-110 active:scale-100 inline-block focus-visible:outline-none visited:outline-none opacity-60 group-hover:opacity-100 transition-all duration-200 hover:duration-75 undefined']"
    _textSearch2nd = 'ao polo'
    _buttonUpdateProduct = "//button[@class=' btn btn-small md:btn-medium btn-solid-default bg-yd-grey-light-2 text-yd-button-text-5 xlg:text-yd-button-text-3 w-fit text-yd-typo-title disabled:bg-yd-grey-light-2 disabled:!text-yd-typo-disabled rounded-lg ']"
    _buttonUpdatePopup = "//div[@class='py-3 xmd:py-0']//div[@class='font-semibold text-yd-button-text-1 text-yd-typo-title']"
    _buttonUpdateProduct2 = "(//button[@class=' btn btn-small md:btn-medium btn-solid-default bg-yd-grey-light-2 text-yd-button-text-5 xlg:text-yd-button-text-3 w-fit text-yd-typo-title disabled:bg-yd-grey-light-2 disabled:!text-yd-typo-disabled rounded-lg '])[2]"
    _qualityPlusPopup = "(//button[@class= 'product-quantity-update-tool_button__dMhNl product-quantity-update-tool_button_right__MHn0c product-quantity-update-tool_button-normal__YS_yD product-quantity-update-tool_small__RSqR_']//*[name()='svg' and @class='product-quantity-update-tool_icon__7wU6c'])[2]"
    _qualityMinusPopup = "(//button[@class= 'product-quantity-update-tool_button__dMhNl product-quantity-update-tool_button_right__MHn0c product-quantity-update-tool_button-normal__YS_yD product-quantity-update-tool_small__RSqR_']//*[name()='svg' and @class='product-quantity-update-tool_icon__7wU6c'])"
    _buttonCheckout = "//button[@class=' btn btn-extra-large btn-solid btn-solid-primary btn-solid-3d-primary w-full mt-7']"
    _buttonInputSearchDesktop = "//input[@class=' input__m input--default pl-12 pr-4  bg-yd-grey-light-2 hover:bg-yd-grey-light-3 focus:bg-yd-grey-light-3 text-yd-body-2 transition-all duration-200 w-[10.5rem] !rounded-[1.25rem] truncate']"
    _textLinkElement = "//span[@class='font-regular md:font-regular text-yd-subtitle-3 md:text-yd-subtitle-2 text-yd-typo-subtitle group-hover:text-yd-alert-info ']"
    _fillNameCus = "//input[@class=' input__xl input--default pl-12 pr-4  w-full h-[52px] !pr-3 !pl-[42px] rounded-[4px] placeholder:text-yd-gray-100 border-yd-gray-50 truncate'][@name='name']"
    _dataName = "Test Đơn web"
    _dataPhone = "0900000001"
    _dataDetailAddress = "90 Le Loi"
    _fillNumberCus = "//input[@class=' input__xl input--default pl-12 pr-4  w-full h-[52px] !pr-3 !pl-[42px] rounded-[4px] placeholder:text-yd-gray-100 border-yd-gray-50 truncate'][@name='phone']"
    _addressCus = "//div[@class = 'w-full relative select-city-district-ward !rounded-[4px] !border-yd-gray-50 text-yd-typo-title']"
    _addressCity = "//input[@class= ' input__m input--default pl-12 pr-4  w-full w-full h-11 !pl-9 !rounded-none !border-t-0 !border-r-0 !border-l-0 truncate']"
    _chooseCity = "//div[@class= 'font-regular text-yd-label-4 text-yd-typo-label']"
    _addressProvince = "//input[@class= ' input__m input--default pl-12 pr-4  w-full w-full h-11 !pl-9 !rounded-none !border-t-0 !border-r-0 !border-l-0 truncate']"
    _chooseProvince = "//div[@class= 'font-regular text-yd-label-4 text-yd-typo-label']"
    _detailAddress = "//input[@name='address'][@class=' input__xl input--default pl-4 pr-4  w-full h-[52px] rounded-[4px] placeholder:text-yd-gray-100 border-yd-gray-50 truncate']"
    _noteOrder = "//input[@class=' input__xl input--default pl-12 pr-4  w-full h-[52px] !pr-3 !pl-[42px] rounded-[4px] placeholder:text-yd-gray-100 border-yd-gray-50 truncate'][@name= 'note']"
    _payment = "//button[@class= ' btn btn-solid btn-solid-primary btn-solid-3d-primary w-full h-[48px]']"

    def click_search(self):
        self.elementClick(self._buttonInputSearchDesktop, locatorType="xpath")

    def enter_search(self, key):
        self.sendKeys(data=key, locator=self._inputSearchDesktop, locatorType="xpath")

    def choose_product1st(self):
        self.elementClick(self._itemProductFirstElement, locatorType="xpath")

    def update_quality_plus(self):
        self.elementClick(self._buttonUpdateQualityPlus, locatorType="xpath")

    def add_to_cart(self):
        self.elementClick(self._buttonAddCart, locatorType="xpath")

    def remove_popup(self):
        self.elementClick(self._iconRemovePopup, locatorType="xpath")

    def click_text_link(self):
        self.elementClick(self._textLinkElement, locatorType="xpath")

    def buy_now(self):
        self.elementClick(self._buttonBuyNow, locatorType="xpath")

    def clear_fields(self):
        self.elementClick(self._buttonClearText, locatorType="xpath")

    def open_update_popup(self):
        self.elementClick(self._buttonUpdateProduct, locatorType="xpath")

    def open_update_popup_2nd(self):
        self.elementClick(self._buttonUpdateProduct2, locatorType="xpath")

    def add_quality_plus_popup(self):
        self.elementClick(self._qualityPlusPopup, locatorType="xpath")
        self.elementClick(self._buttonUpdatePopup, locatorType="xpath")

    def add_quality_plus_popup_2nd(self):
        self.elementClick(self._qualityPlusPopup, locatorType="xpath")
        self.elementClick(self._buttonUpdatePopup, locatorType="xpath")

    def minus_quality_popup(self):
        self.elementClick(self._qualityMinusPopup, locatorType="xpath")
        self.elementClick(self._buttonUpdatePopup, locatorType="xpath")

    def button_checkout(self):
        self.elementClick(self._buttonCheckout, locatorType="xpath")

    def checkout_done(self):
        self.click_search()
        time.sleep(1)
        self.enter_search(key=self._textSearch)
        time.sleep(2)
        self.choose_product1st()
        time.sleep(2)
        self.update_quality_plus()
        self.update_quality_plus()
        self.add_to_cart()
        time.sleep(2)
        self.remove_popup()
        time.sleep(2)
        self.click_text_link()
        time.sleep(2)
        self.search_2nd()
        time.sleep(2)
        self.buy_now()
        time.sleep(2)
        self.update_value_product_1st()
        time.sleep(2)
        self.update_value_product_2nd()
        time.sleep(2)
        self.button_checkout()
        time.sleep(3)
        self.fill_info_customer()
        time.sleep(3)
        self.fill_address_customer()
        time.sleep(3)
        # self.payment()
        # time.sleep(4)

    def search_2nd(self):
        self.click_search()
        self.clear_fields()
        self.enter_search(key=self._textSearch2nd)
        time.sleep(2)
        self.choose_product1st()
        self.update_quality_plus()

    def update_value_product_1st(self):
        self.open_update_popup()
        self.add_quality_plus_popup()

    def update_value_product_2nd(self):
        self.open_update_popup_2nd()
        self.minus_quality_popup()

    def fill_info_customer(self):
        self.sendKeysNotEnter(data=self._dataName, locator=self._fillNameCus, locatorType="xpath")
        self.sendKeysNotEnter(data=self._dataPhone, locator=self._fillNumberCus, locatorType="xpath")

    def fill_address_customer(self):
        self.elementClick(self._addressCus, locatorType="xpath")
        self.sendKeysNotEnter(data="An giang", locator=self._addressCity, locatorType="xpath")
        self.elementClick(self._chooseCity, locatorType="xpath")
        time.sleep(3)
        self.sendKeysNotEnter(data="Châu Thành", locator=self._addressProvince, locatorType="xpath")
        self.elementClick(locator=self._chooseProvince, locatorType="xpath")
        time.sleep(3)
        self.sendKeysNotEnter(data="Thị trấn An Châu", locator=self._addressProvince, locatorType="xpath")
        self.elementClick(locator=self._chooseProvince, locatorType="xpath")
        time.sleep(3)
        self.sendKeysNotEnter(data=self._dataDetailAddress, locator=self._detailAddress, locatorType="xpath")
        self.sendKeysNotEnter(data="Test Đơn web", locator=self._noteOrder, locatorType="xpath")

    def payment(self):
        self.elementClick(self._payment, locatorType="xpath")

    def verify_add_cart_failed(self):
        result = self.isElementPresent("(//div[contains(text(),'Cảm ơn bạn đã mua sắm tại Yody')])[2]",
                                       locatorType="xpath")
        return result
