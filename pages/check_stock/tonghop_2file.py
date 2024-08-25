import pandas as pd

# Đường dẫn tới file txt
file_path = '/Users/kanglee/PycharmProjects/pythonProject5/pages/check_stock/product_report_with_unicorn.txt'

# Đọc file .txt thành các dòng riêng biệt
with open(file_path, 'r') as file:
    lines = file.readlines()

# Xóa các dòng không cần thiết, chỉ giữ lại phần có dữ liệu
data_lines = lines[4:-1]

# Loại bỏ các ký tự đầu dòng và cuối dòng thừa thãi (nếu có)
cleaned_data = [line.strip('| \n') for line in data_lines]

# Tách dữ liệu thành các cột
cleaned_data = [line.split('|') for line in cleaned_data]

# Tạo DataFrame từ dữ liệu đã làm sạch với đúng số cột
df = pd.DataFrame(cleaned_data, columns=["Product ID", "Variant ID", "Core SKU", "Available", "Tồn Unicorn"])

# Xóa khoảng trắng thừa ở tên cột và các giá trị trong DataFrame
df.columns = df.columns.str.strip()
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Lưu DataFrame thành file Excel
output_path = 'product_report.xlsx'
df.to_excel(output_path, index=False)

print(f"File đã được lưu tại: {output_path}")
