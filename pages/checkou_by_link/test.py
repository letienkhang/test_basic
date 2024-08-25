import sys
import os
from selenium import webdriver
from datetime import datetime
from tabulate import tabulate
# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from pages.checkou_by_link.checkout_link import CheckoutLinkBasic



urlsProd = [
    'https://yody.vn/product/khan-mat-modal-mem-min-combo-2-chiec-1?colorId=1175&sizeId=90',
    'https://yody.vn/product/bo-do-the-thao-nam-ni-phoi-soc?colorId=437&sizeId=4',
    'https://yody.vn/category/ao-polo-nam',
    'https://yody.vn/category/ao-khoac-nu',
    'https://yody.vn/collection/yody-sport',
    'https://yody.vn/collection/thoi-trang-cong-so',
    'https://yody.vn/blog/ve-yody',
    'https://yody.vn/blog/thoi-trang-the-gioi',
    'https://yody.vn/page/clean-vn',
    'https://yody.vn/page/yody-sport-new-collection'
]

urlsDev = [
    # 'https://dev.yody.io/product/polo-nam-coolmate-mat-chim-hot?colorId=522&sizeId=3',
    'https://dev.yody.io/product/ao-polo-mat-lanh-vvvvv-1390545?colorId=1099&sizeId=37'
]

urlsUAT = [
    'https://uat.yody.io/',
    'https://uat.yody.io/product/ao-so-mi-nam-dai-tay-thoang-khi-?colorId=532&sizeId=6',
    'https://uat.yody.io/product/quan-jeans-nu-baggy-co-gian-?colorId=521&sizeId=18',
    'https://uat.yody.io/product/ao-so-mi-nam-bac-ha-coc-tay?colorId=503&sizeId=4',
    'https://uat.yody.io/product/ao-so-mi-tay-dai-nu-nano-ke-nang-dong?colorId=187&sizeId=4',
    'https://uat.yody.io/category/ao-polo-nu',
    'https://uat.yody.io/category/ao-so-mi-nam',
    'https://uat.yody.io/category/quan-jeans-nu',
    'https://uat.yody.io/page/jeanflex2024',
    'https://uat.yody.io/page/yoguu',
    'https://uat.yody.io/page/yody-sport-new-collection',
    'https://uat.yody.io/collection/ao-polo-yody',
    'https://uat.yody.io/collection//khang-test-bug-3734-uat',
    'https://uat.yody.io/blog',
]

driver = webdriver.Chrome()
log_data = []
page = CheckoutLinkBasic(driver)


def checkout_by_link(url):
    driver.maximize_window()
    driver.get(url)
    page.checkout_by_link()


if len(sys.argv) < 2:
    print("Usage: python script.py <url>")
    sys.exit(1)

url = sys.argv[1]

if url.startswith('https://beta.yody.vn/'):
    for prod_url in urlsProd:
        checkout_by_link(prod_url)
elif url.startswith('https://dev.yody.io/'):
    for dev_url in urlsDev:
        checkout_by_link(dev_url)
elif url.startswith('https://uat.yody.io/'):
    for uat_url in urlsUAT:
        checkout_by_link(uat_url)
else:
    print("Unknown environment URL")
    sys.exit(1)

driver.quit()

# Write results to file
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open('meta_robots_log.txt', 'a') as file:
    file.write(f"\nLog Date: {timestamp}\n")
    file.write("========================================\n")
    table = tabulate(log_data, headers=["URL", "Meta Robots"], tablefmt="grid")
    file.write(table)
    file.write("\n")
