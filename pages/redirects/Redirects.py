from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from tabulate import tabulate
from datetime import datetime

url_list = [
    "https://dev.yody.io/product/ao-polo-nam-pique-mat-chim-basic-co-gian-thoang-khi?colorId=1483",
    "https://dev.yody.io/product/ao-polo-tre-em-cafe-bo-tronkid4035?colorId=514",
]

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome()

results = []

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for initial_url in url_list:
    initial_response = requests.get(initial_url, allow_redirects=False)
    initial_status = initial_response.status_code

    driver.get(initial_url)
    final_url = driver.current_url

    final_response = requests.get(final_url, allow_redirects=False)
    final_status = final_response.status_code

    results.append({
        "Time": current_time,
        "Initial URL": initial_url,
        "Initial Status": initial_status,
        "Final URL": final_url,
        "Final Status": final_status
    })

driver.quit()

table = tabulate(results, headers="keys", tablefmt="pretty")

with open("redirect_results.txt", "a") as file:
    centered_time = current_time.center(70)
    file.write(f"{centered_time}\n\n")
    file.write(table)


print("Results have been written to redirect_results.txt")
