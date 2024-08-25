import pandas as pd

# Đọc dữ liệu từ file txt
input_file = "/Users/kanglee/PycharmProjects/pythonProject5/pages/check_stock/product_report.txt"
with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Lọc ra các dòng chứa dữ liệu
data_lines = [line.strip() for line in lines if "|" in line and "Product ID" not in line]

# Tạo dataframe từ dữ liệu
data = []
for line in data_lines:
    columns = line.split("|")[1:-1]
    data.append([col.strip() for col in columns])

df = pd.DataFrame(data, columns=["Product ID", "Variant ID", "Core SKU", "Available", "Tồn Unicorn"])

# Thêm cột "Tồn Unicorn" trống vào dataframe (nếu chưa thêm trước đó)
if "Tồn Unicorn" not in df.columns:
    df["Tồn Unicorn"] = ""

# Lưu dữ liệu vào file Excel
output_excel_file = "product_report_with_unicorn.xlsx"
df.to_excel(output_excel_file, index=False)

print(f"Dữ liệu đã được lưu vào file Excel: {output_excel_file}")
