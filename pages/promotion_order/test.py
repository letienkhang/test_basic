import sys
import time

from selenium import webdriver

from pages.promotion_order.promotion_order import ProductDiscountPage


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]

    driver = webdriver.Chrome()
    page = ProductDiscountPage(driver)

    try:
        if url.startswith('https://unicorn-dev.yody.io/'):
            print("Running in Development environment")
            driver.maximize_window()
            driver.get(url)
            page.create_discount(driver=driver)
        elif url.startswith('https://unicorn-uat.yody.io/'):
            print("Running in UAT environment")
            driver.maximize_window()
            driver.get(url)
            page.create_discount(driver=driver)
        else:
            print("Unknown environment URL")
            sys.exit(1)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
