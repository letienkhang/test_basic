import sys
import time
import os
from selenium import webdriver
from datetime import datetime

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from pages.checkout_basic.checkout_basic import CheckoutBasic


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]

    driver = webdriver.Chrome()
    page = CheckoutBasic(driver)

    try:
        product_codes = ['VAN6148', 'TSM7137', 'APN6226']
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('product_price_log.txt', 'a') as log_file:
            log_file.write(f"\nLog Date: {current_date}\n")
            log_file.write("=" * 40 + "\n")
        if url.startswith('https://beta.yody.vn/'):
            print("Running in Production environment")
            driver.maximize_window()
            driver.get(url)
            page.checkout_done()
            # for product_code in product_codes:
            #     page.search_same_price(product_code=product_code)
        elif url.startswith('https://dev.yody.io/'):
            print("Running in Development environment")
            driver.maximize_window()
            driver.get(url)
            page.checkout_done()
            # for product_code in product_codes:
            #     page.search_same_price(product_code=product_code)
        elif url.startswith('https://uat.yody.io/'):
            print("Running in Staging environment")
            driver.maximize_window()
            driver.get(url)
            page.checkout_done()
            # for product_code in product_codes:
            #     page.search_same_price(product_code=product_code)
        else:
            print("Unknown environment URL")
            sys.exit(1)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
