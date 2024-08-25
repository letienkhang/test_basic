import logging
import time
import os
from datetime import datetime
import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver
from pages.promotion_order.locator import ProductDiscountLocators


class ProductDiscountPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_login_yody_id(self):
        self.elementClick(ProductDiscountLocators.LOGIN_WITH_YODY_ID_BUTTON, locatorType="xpath")

    def enter_username(self, username):
        self.sendKeysNotEnter(data=username, locator=ProductDiscountLocators.INPUT_USERNAME, locatorType="xpath")

    def enter_password(self, password):
        self.sendKeysNotEnter(data=password, locator=ProductDiscountLocators.USER_PASS_INPUT, locatorType="xpath")

    def click_login(self):
        self.elementClick(ProductDiscountLocators.LOGIN_BUTTON, locatorType="xpath")

    def login(self):
        self.click_login_yody_id()
        file_path = '/Users/kanglee/Downloads/YODY/buggy-automation-test/credential.txt'
        open(file_path, 'r')
        if os.path.exists(file_path):
            with open(file_path, 'r') as element:
                lines = element.readlines()
                if len(lines) >= 2:
                    username = lines[0].strip()
                    password = lines[1].strip()
                else:
                    print("Tệp không chứa đủ thông tin đăng nhập.")
        else:
            print(f"File {file_path} không tồn tại")
        self.enter_username(username=username)
        self.enter_password(password=password)
        self.click_login()
        time.sleep(4)

    def create_discount(self, driver):
        time.sleep(5)
        self.login()
        time.sleep(2)
        # self.choose_setup_promotion()
        # time.sleep(2)
        # self.choose_manage_promotion()
        # time.sleep(2)
        # self.create_promotion()
        # self.option_promotion()
        # time.sleep(2)
        # self.enter_content_promotion()
        # time.sleep(2)
        # self.type_promotion_dropdown()
        # time.sleep(2)
        # self.choose_due_date()
        # time.sleep(2)
        # self.create_item_new()
        # time.sleep(2)
        # self.enter_content_item()
        # time.sleep(4)
        # self.enable_promotion(driver=driver)
        # time.sleep(2)
        # self.elementClick(ProductDiscountLocators.YES_BUTTON, locatorType="xpath")
        # time.sleep(1)
        # self.elementClick(ProductDiscountLocators.TURN_ON_ITEM, locatorType="xpath")
        time.sleep(10)


    def choose_setup_promotion(self):
        self.elementClick(ProductDiscountLocators.ITEM_MENU_PROMOTION, locatorType="xpath")

    def choose_manage_promotion(self):
        self.elementClick(ProductDiscountLocators.ITEM_MENU_MANAGE_THE_PROMOTION, locatorType="xpath")

    def create_promotion(self):
        self.elementClick(ProductDiscountLocators.CREATE_PROMOTION, locatorType="xpath")

    def option_promotion(self):
        self.elementClick(ProductDiscountLocators.OPTION_PROMOTION_BUTTON, locatorType="xpath")

    def type_promotion_dropdown(self):
        self.elementClick(ProductDiscountLocators.TYPE_PROMOTION_DROPDOWN, locatorType="xpath")
        time.sleep(1)
        self.elementClick(ProductDiscountLocators.CHOOSE_ITEM_TYPE_DROPDOWN, locatorType="xpath")

    def enter_content_promotion(self):
        # Get the current time and date
        now = datetime.now()
        promo_name = f"AUTO CTKM cho đơn {now.day}/{now.month} - {now.hour}-{now.minute}"
        self.sendKeysNotEnter(data=promo_name, locator=ProductDiscountLocators.NAME_PROMOTION_INPUT,
                              locatorType="xpath")
        self.sendKeysNotEnter(data=promo_name, locator=ProductDiscountLocators.CONTENT_PROMOTION_INPUT, locatorType="xpath")

    def choose_due_date(self):
        self.elementClick(ProductDiscountLocators.CHOOSE_DUE_DATE, locatorType="xpath")
        time.sleep(1)
        self.elementClick(ProductDiscountLocators.PICKER_NEXT_BUTTON, locatorType="xpath")
        time.sleep(1)
        self.elementClick(ProductDiscountLocators.DUE_DATE_NEXT_MONTH, locatorType="xpath")
        time.sleep(1)
        self.elementClick(ProductDiscountLocators.OK_DUE_DATE_BUTTON, locatorType="xpath")

    def create_item_new(self):
        self.elementClick(ProductDiscountLocators.CREATE_NEW_ITEM_BUTTON, locatorType="xpath")
        time.sleep(1)
        self.elementClick(ProductDiscountLocators.TAB_CODE_PROMOTION, locatorType="xpath")
        time.sleep(1)
        self.elementClick(ProductDiscountLocators.CHOOSE_BY_ORDER, locatorType="xpath")

    def enter_content_item(self):
        #KM theo đơn hàng
        now = datetime.now()
        promo_name = f"AUTO KM theo đơn hàng {now.hour}{now.minute}"
        self.sendKeysNotEnter(data=promo_name, locator=ProductDiscountLocators.OPERATION_NAME_INPUT,
                              locatorType="xpath")
        time.sleep(1)
        #chon kenh ban hang
        self.elementClick(ProductDiscountLocators.SALES_CHANNEL, locatorType="xpath")
        time.sleep(1)
        self.elementClick(ProductDiscountLocators.SALES_CHANNEL_OPTION, locatorType="xpath")
        time.sleep(1)
        options_to_select = ["Web", "website", "Mobile_App", "Website", "App"]  # Add more options as needed

        for option in options_to_select:
            try:
                option_element = self.getElement(locatorType="xpath", locator=f'//div[@class="ant-select-item ant-select-item-option" and @title="{option}"]' )
                option_element.click()
                time.sleep(0.5)  # Pause briefly to allow the selection to register
            except Exception as e:
                print(f"Option '{option}' not found: {e}")

        self.sendKeysNotEnter(data=promo_name, locator=ProductDiscountLocators.CREATE_AREA_INPUT,
                              locatorType="xpath")

        self.sendKeysNotEnter(data='10000', locator=ProductDiscountLocators.PROMO_VALUE_INPUT,
                              locatorType="xpath")
        time.sleep(2)
        #self.elementClick(ProductDiscountLocators.SHOW_WEDSITE_CHECKBOX, locatorType="xpath")
        self.elementClick(ProductDiscountLocators.SAVE_PROMO, locatorType="xpath")

    def enable_promotion(self, driver):
        self.elementClick(ProductDiscountLocators.CHOOSE_CODE_LINK, locatorType="xpath")
        time.sleep(5)
        parent_window = driver.current_window_handle
        all_windows = driver.window_handles
        # Chuyển sang cửa sổ mới
        for window in all_windows:
            if window != parent_window:
                self.driver.switch_to.window(window)
                print(f"Switched to new window handle: {window}")
                break
        print(f"Current window title: {driver.title}")
        time.sleep(5)
        self.elementClick(ProductDiscountLocators.ADD_HAND_MADE_CODE, locatorType="xpath")
        time.sleep(2)
        now = datetime.now()
        promo_code = f"CODE{now.hour}{now.minute}"
        self.sendKeysNotEnter(data=promo_code, locator=ProductDiscountLocators.ENTER_HAND_MADE_CODE,
                              locatorType="xpath")
        time.sleep(2)
        self.elementClick(ProductDiscountLocators.HAND_MADE_CODE_BUTTON, locatorType="xpath")
        time.sleep(0.5)
        self.elementClick(ProductDiscountLocators.CONFIRM_HAND_CODE, locatorType="xpath")
        time.sleep(2)
        self.elementClick(ProductDiscountLocators.ENABLE_HAND_CODE, locatorType="xpath")
        print(f"Current window title: {driver.title}")
        time.sleep(4)
        # driver.close()
        driver.switch_to.window(parent_window)
        time.sleep(2)
        self.elementClick(ProductDiscountLocators.SAVE_DONE, locatorType="xpath")
        print(f"Current window title: {driver.title}")





