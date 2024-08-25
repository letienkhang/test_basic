import pandas as pd

file_path = '/Users/kanglee/PycharmProjects/pythonProject5/pages/check_stock/log_output.txt'
data = pd.read_csv(file_path, delimiter='|', skiprows=[0, 2])

# Xóa khoảng trắng thừa ở tên cột nếu có
data.columns = data.columns.str.strip()

# Lọc các hàng có "Store Name" bắt đầu bằng "Filtered SKU:", bỏ qua NaN
filtered_data = data[data['Store Name'].str.contains('Filtered SKU:', na=False)].copy()

# Trích xuất SKU từ "Store Name" và gán vào cột SKU sử dụng .loc
filtered_data.loc[:, 'SKU'] = filtered_data['Store Name'].str.extract(r'Filtered SKU: (\S+)')

# Chọn cột SKU và Available for Sale để tạo bảng mới
final_data = filtered_data[['SKU', 'Available for Sale']]

# Đặt lại tên cột nếu cần thiết
final_data.columns = ['SKU', 'Available for Sale']

# Lưu bảng mới vào file txt hoặc csv
final_data.to_csv('filtered_sku_output.txt', sep='|', index=False)

print(final_data)