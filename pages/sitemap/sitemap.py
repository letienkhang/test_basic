import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from tabulate import tabulate

# URL lists for different environments
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
    'https://dev.yody.io',
    'https://dev.yody.io/product/ao-nu-t-shirt-dang-om-phoi-bo?colorId=1103',
    'https://dev.yody.io/product/ao-nu-t-shirt-dang-om-phoi-bo?colorId=531',
    'https://dev.yody.io/product/ao-polo-mat-lanh-vvvvv-1390545?sizeId=36',
    'https://dev.yody.io/product/ao-nu-airycool-bo-qua-tram?colorId=530&sizeId=2',
    'https://dev.yody.io/category/ao-thun-nu',
    'https://dev.yody.io/category/ao-thun-nam',
    'https://dev.yody.io/page/jeanflex2024',
    'https://dev.yody.io/page/yoguu',
    'https://dev.yody.io/page/yody-sport-new-collection',
    'https://dev.yody.io/collection/ao-polo-yody',
    'https://dev.yody.io/collection//khang-test-bug-3734',
    'https://dev.yody.io/blog/blog-thoi-trang-tre-em',
    'https://dev.yody.io/post/mua-ao-dai-cach-tan-cho-be-gai-o-dau',
    'https://dev.yody.io/post/shop-quan-ao-tre-em',
    'https://dev.yody.io/blog'
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


def check_meta_robots(url):
    driver.get(url)
    time.sleep(2)
    index_follow = "not found"
    noindex_nofollow = "not found"

    try:
        driver.find_element(By.XPATH, '//meta[@name="robots"][@content="index, follow"]')
        index_follow = "found"
    except Exception:
        pass

    try:
        driver.find_element(By.XPATH, '//meta[@name="robots"][@content="noindex, nofollow"]')
        noindex_nofollow = "found"
    except Exception:
        pass

    log_data.append([url, index_follow, noindex_nofollow])


if len(sys.argv) < 2:
    print("Usage: python script.py <url>")
    sys.exit(1)

url = sys.argv[1]

if url.startswith('https://beta.yody.vn/'):
    for prod_url in urlsProd:
        check_meta_robots(prod_url)
elif url.startswith('https://dev.yody.io/'):
    for dev_url in urlsDev:
        check_meta_robots(dev_url)
elif url.startswith('https://uat.yody.io/'):
    for uat_url in urlsUAT:
        check_meta_robots(uat_url)
else:
    print("Unknown environment URL")
    sys.exit(1)

driver.quit()

# Write results to file
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open('meta_robots_log.txt', 'a') as file:
    file.write(f"\nLog Date: {timestamp}\n")
    file.write("========================================\n")
    table = tabulate(log_data, headers=["URL", "Index Follow", "Noindex Nofollow"], tablefmt="grid")
    file.write(table)
    file.write("\n")
