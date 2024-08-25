import requests
from selenium.webdriver.chrome import webdriver
from tabulate import tabulate
from datetime import datetime

#product_url = 'ao-polo-tre-em-cafe-bo-tronkid4035'
product_url = 'ao-polo-tre-em-cafe-bo-tronkid4035'
api_url = f'https://api-dev.yody.io/storefront-product/api/product/public/products-url/{product_url}.json'
# api_url = f'https://api.newfashion.com.vn/storefront-product/api/product/public/products-url/{product_url}.json'
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    variants = data.get('variants', [])

    top_variants = sorted(variants, key=lambda x: x['inventory_quantity'], reverse=True)[:]

    table_data = []
    for variant in top_variants:
        row = {
            "SKU": variant['sku'],
            "Tên": variant['name'],
            "Màu": variant['color'],
            "Size": variant['size'],
            "Tồn kho": variant['inventory_quantity'],
            "Giá": f"{variant['prices'][0]['price']} {variant['prices'][0]['currency_code']}",
            "Link": f"https://yody.vn/product/{product_url}?colorId={variant['color_id']}&sizeId={variant['size_id']}"
        }
        table_data.append(row)

    table = tabulate(table_data, headers="keys", tablefmt="grid")
    log_date = datetime.now().strftime("Log Date: %Y-%m-%d %H:%M:%S")
    file_name = "check_stock.txt"

    with open(file_name, "a", encoding="utf-8") as file:
        file.write(log_date + "\n")
        file.write(table + "\n\n")

    print("Dữ liệu đã được ghi vào file.")
else:
    print(f"Yêu cầu API không thành công: {response.status_code}")





