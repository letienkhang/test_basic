import requests
import pandas as pd
from tabulate import tabulate
from datetime import datetime

excel_file = "/Users/kanglee/PycharmProjects/pythonProject5/pages/check_stock/filecheck.xlsx"
df = pd.read_excel(excel_file)

mapping = dict(zip(df['ecommerce_variant_id'], df['core_sku']))

product_ids = [37657, 37685, 37645, 37705, 37689, 37670, 37684, 37679, 37698, 37683, 37663, 37703, 37662, 37666, 37660, 37648, 37659, 37676, 34909, 37673, 37643, 37678]

base_url = "https://api.newfashion.com.vn/yobuggy-inventories/v1/inventories/products/{}/saleable-qty"

with open("product_report.txt", "w", encoding="utf-8") as f:
    for product_id in product_ids:
        url = base_url.format(product_id)
        response = requests.get(url)

        log_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header_time = f"Log Date: {log_date} | Product ID: {product_id}"

        if response.status_code == 200:
            json_data = response.json()

            if json_data["code"] == 200 and "data" in json_data:
                table_data = []
                for item in json_data["data"]:
                    variant_id = item.get("variant_id")
                    available = item.get("available", "--")

                    core_sku = mapping.get(variant_id, "--")

                    table_data.append([product_id, variant_id, core_sku, available])

                table = tabulate(table_data, headers=["Product ID", "Variant ID", "Core SKU", "Available"],
                                 tablefmt="grid")

                f.write(header_time + "\n")
                f.write(table + "\n\n")

                print(header_time)
                print(table)
            else:
                table_data = [["--", "--", "--", "--"]]
                table = tabulate(table_data, headers=["Product ID", "Variant ID", "Core SKU", "Available"],
                                 tablefmt="grid")

                f.write(header_time + "\n")
                f.write(table + "\n")
                f.write("Note: No data available for this product ID.\n\n")
                print(f"No data available for product_id: {product_id}")
        else:
            table_data = [["--", "--", "--", "--"]]
            table = tabulate(table_data, headers=["Product ID", "Variant ID", "Core SKU", "Available"], tablefmt="grid")

            f.write(header_time + "\n")
            f.write(table + "\n")
            f.write("Note: Failed to retrieve data for this product ID.\n\n")
            print(f"Failed to retrieve data for product_id: {product_id}")
