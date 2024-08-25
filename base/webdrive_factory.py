"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import json
import ssl
import time
import traceback
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
import certifi
import urllib3

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        options = uc.ChromeOptions()
        options.headless = True
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-images")
        options.add_argument("--disable-javascript")
                # baseURL = "https://dev.yody.io/"
        # baseURL = "https://uat.yody.io/"
        baseURL = "https://dev.yody.io/"
        # baseURL = "https://unicorn-uat.yody.io/"
        # baseURL = "https://unicorn-dev.yody.io/"
       
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
            # driver.set_window_size(1440, 900)
        elif self.browser == "safari":
            driver = webdriver.Safari()
            # driver.set_window_size(1440, 900)
        else:
            driver = webdriver.Firefox()
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        #driver.set_window_size(1440, 900)
        # Loading browser with App URL
        driver.get(baseURL)
        return driver
    
