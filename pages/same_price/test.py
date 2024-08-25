import sys
from selenium import webdriver
from datetime import datetime
from tabulate import tabulate
from pages.same_price.same_price_page import SamePricePage


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]

    driver = webdriver.Chrome()
    page = SamePricePage(driver)

    try:
        #product_codes = ['APM3635', 'SCM1357', 'QJN5084', 'APM3635', 'SQM6025']
        # product_codes = ['TSN6176', 'APN7028', 'TSK6350', 'STM7067']
        product_codes = [
            'APK5177','APK6024', 'APK6130', 'APM3635', 'APM4239', 'APM6297'
        ]
        log_data = []  # Initialize log_data list to store results

        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open('product_price_log.txt', 'a') as log_file:
            log_file.write(f"\nLog Date: {current_date}\n")
            log_file.write("=" * 40 + "\n")

            if url.startswith('https://beta.yody.vn/'):
                print("Running in Production environment")
                driver.maximize_window()
                driver.get(url)
                for product_code in product_codes:
                    page.search_same_price(product_code=product_code, log_data=log_data)
            elif url.startswith('https://dev.yody.io/'):
                print("Running in Development environment")
                driver.maximize_window()
                driver.get(url)
                for product_code in product_codes:
                    page.search_same_price(product_code=product_code, log_data=log_data)
            elif url.startswith('https://uat.yody.io/'):
                print("Running in Staging environment")
                driver.maximize_window()
                driver.get(url)
                for product_code in product_codes:
                    page.search_same_price(product_code=product_code, log_data=log_data)
            else:
                print("Unknown environment URL")
                sys.exit(1)

            # After collecting all the data, create the table and write it to the file
            table = tabulate(log_data, headers=["Search", "Product Code", "Price", "Compare at Price", "Discount"],
                             tablefmt="grid")
            log_file.write(f"{table}\n")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
