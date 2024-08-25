import os
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from tabulate import tabulate
from datetime import datetime

class ProductDiscountLocators:
    LOGIN_WITH_YODY_ID_BUTTON = (By.XPATH, "//ul[@class='pf-c-login__main-footer-links kc-social-links ']")
    INPUT_USERNAME = (By.XPATH, "//input[@class='pf-c-form-control'][@name='username']")
    USER_PASS_INPUT = (By.XPATH, "//input[@class='pf-c-form-control'][@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//div[@class='form-group']//input[@class ='pf-c-button pf-m-primary pf-m-block btn-lg'][@name='login']")
    ITEM_MENU_PROMOTION = (By.XPATH, "//div[@class='ant-menu-submenu-title']//span[@class='ant-menu-title-content']//div[text()='Kho hàng']")
    ITEM_MENU_MANAGE_THE_PROMOTION =(By.XPATH,  "//li[@role='menuitem' and @tabindex='-1']//a[@title='Tồn kho']")
    INPUT_SEARCH = (By.XPATH, "//input[@placeholder='Tìm kiếm sản phẩm theo Tên, Mã vạch, SKU']")
    BUTTON_SUBMIT = (By.XPATH, "//button[@type='submit' and @class='ant-btn ant-btn-primary']")

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def send_keys(self, data, locator):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(data)

    def send_keys_enter(self, data, locator):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(data + Keys.ENTER)

    def click_login_yody_id(self):
        self.click_element(ProductDiscountLocators.LOGIN_WITH_YODY_ID_BUTTON)

    def enter_username(self, username):
        self.send_keys(data=username, locator=ProductDiscountLocators.INPUT_USERNAME)

    def enter_password(self, password):
        self.send_keys(data=password, locator=ProductDiscountLocators.USER_PASS_INPUT)

    def click_login(self):
        self.click_element(ProductDiscountLocators.LOGIN_BUTTON)

    def process_sku(self, sku):
        time.sleep(3)
        self.click_element(ProductDiscountLocators.ITEM_MENU_PROMOTION)
        time.sleep(3)
        self.click_element(ProductDiscountLocators.ITEM_MENU_MANAGE_THE_PROMOTION)
        time.sleep(3)
        self.send_keys(data=sku, locator=ProductDiscountLocators.INPUT_SEARCH)
        time.sleep(3)
        self.click_element(ProductDiscountLocators.BUTTON_SUBMIT)
        time.sleep(4)
        self.click_element((By.XPATH, f"//a[text()='{sku}']"))
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, "(//div[@class='ant-tabs ant-tabs-top'])[2]")
        time.sleep(4)
        html_content = element.get_attribute('outerHTML')

        return html_content

    def process_all_skus(self, sku_list):
        time.sleep(2)
        with open("all_skus_html_content.txt", "a", encoding="utf-8") as file:
            for sku in sku_list:
                html_content = self.process_sku(sku)
                file.write(f"HTML content for SKU: {sku}\n")
                file.write(html_content + "\n\n")
                print(f"HTML content for {sku} has been saved to all_skus_html_content.txt")
                time.sleep(3)  # Thời gian chờ giữa các lần lặp (có thể điều chỉnh nếu cần)

    def login(self):
        # time.sleep(5)
        # self.click_login_yody_id()
        # time.sleep(5)

        file_path = '/Users/kanglee/Downloads/YODY/buggy-automation-test/credential.txt'

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if len(lines) >= 2:
                    username = lines[0].strip()
                    password = lines[1].strip()
                else:
                    print("Tệp không chứa đủ thông tin đăng nhập.")
                    return
        else:
            print(f"File {file_path} không tồn tại")
            return

        self.enter_username(username=username)
        self.enter_password(password=password)
        self.click_login()
        time.sleep(3)

        # Danh sách SKU cần xử lý
        sku_list = ['TSN7052-TRA-M']

        # # Danh sách SKU cần xử lý
        # sku_list = ['APN6150-HOG-S',
        #             'APN6150-HOG-M',
        #             'APN6150-HOG-L',
        #             'APN6150-HOG-XL',
        #             'APN6150-HOG-2XL',
        #             'APN6150-TMN-S',
        #             'APN6150-TMN-M',
        #             'APN6150-TMN-L',
        #             'APN6150-TMN-XL',
        #             'APN6150-TMN-2XL',
        #             'APN6150-TRA-S',
        #             'APN6150-TRA-M',
        #             'APN6150-TRA-L',
        #             'APN6150-TRA-XL',
        #             'APN6150-TRA-2XL',
        #             'APN6150-DEN-S',
        #             'APN6150-DEN-M',
        #             'APN6150-DEN-L',
        #             'APN6150-DEN-XL'
        #             'APN6150-DEN-2XL',
        #             'TSN6262-CBA-S']
        self.process_all_skus(sku_list)

        time.sleep(40)

# Khởi tạo WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://unicorn.yody.io/")

login_page = LoginPage(driver)

login_page.login()

driver.quit()
