import os
from bs4 import BeautifulSoup
from tabulate import tabulate

# Đọc nội dung của tệp
with open('all_skus_html_content.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Phân tách nội dung thành các đoạn html_content dựa trên dấu phân cách "HTML content for SKU:"
html_contents = content.split("HTML content for SKU:")

# Khởi tạo danh sách để lưu trữ kết quả
log_entries = []

# Lặp qua từng đoạn html_content
for html_content in html_contents:
    if not html_content.strip():
        continue  # Bỏ qua đoạn rỗng

    # Tách SKU ra khỏi nội dung HTML
    lines = html_content.strip().splitlines()
    sku = lines[0] if lines else "Unknown SKU"  # SKU là dòng đầu tiên sau dấu phân cách
    html_body = "\n".join(lines[1:])  # Phần còn lại là nội dung HTML

    soup = BeautifulSoup(html_body, 'html.parser')

    # Danh sách các kho hiển thị trên web YODY mà bạn muốn lọc
    store_names = [
        "YODY Đức Phổ",
        "YODY Quy Nhơn 2",
        "YODY 172 Hòa Bình, HCM",
        "YODY Đông Anh",
        "YODY Cẩm Thuỷ",
        "YODY Vĩnh Lộc",
        "YODY Nga Sơn",
        "YODY Thuận Thành 2",
        "YODY Vân Đồn",
        "YODY PHỦ",
        "YODY Kim Động",
        "YODY Xô Viết Nghệ Tĩnh",
        "YODY Quảng Ngãi 2",
        "YODY Linh Đàm",
        "YODY yên Hòa",
        "YODY Đức Thọ",
        "YODY Phước An",
        "YODY Quảng Phú",
        "YODY Bắc Kạn",
        "YODY Buôn Trấp",
        "Yody Hậu Lộc",
        "YODY QUY NHƠN",
        "YODY Mai Sơn",
        "YODY Vụ Bản",
        "YODY Hương Khê",
        "YODY Lai Châu",
        "YODY Vĩnh Tường",
        "YODY Yên Thế",
        "YODY Đại Từ",
        "YODY Đồng Hỷ",
        "YODY Hồng Lĩnh",
        "YODY Cẩm Xuyên",
        "YODY Yên Mô",
        "YODY Giao Thủy",
        "YODY Đồng Văn",
        "YODY Quán Lào",
        "YODY Cổ Lễ",
        "YODY Buôn Hồ",
        "YODY Núi Thành",
        "YODY Bồng Sơn",
        "YODY An Lão",
        "YODY Quảng Trị",
        "YODY Hoàn Lão",
        "YODY Hồ Xá",
        "YODY Hội An",
        "YODY Ea Kar",
        "YODY Long Biên",
        "YODY Thạch Thành",
        "YODY Kiến Xương",
        "YODY Yên Khánh",
        "YODY Hoàng Mai",
        "YODY Vĩnh Điện 2",
        "YODY Ba Đồn",
        "YODY Nha Trang",
        "YODY Kiến Giang",
        "YODY Chư Sê",
        "YODY Giếng Đáy",
        "Yody Vĩnh Long",
        "YODY Cầu Giát",
        "YODY Như Quỳnh",
        "Hub Online",
        "uông bí",
        "YODY Tứ Kỳ 2",
        "YODY Ý Yên",
        "YODY Nam Định 2",
        "YODY Phú Yên",
        "Yody Chí Linh 2",
        "Yody Hòa Bình 2",
        "YODY Kon Tum",
        "YODY An Nhơn",
        "YODY Liên Chiểu",
        "YODY Tam Kỳ 1",
        "YODY Đông Hà",
        "YODY Vĩnh Điện",
        "YODY Đồng Hới 1",
        "YODY Quảng Ngãi",
        "YODY Lê Duẩn 1",
        "YODY Hà Lam",
        "YODY Tam Kỳ 2",
        "YODY Lê Duẩn 2",
        "YODY Đồng Hới 2",
        "YODY Gia Lai",
        "YODY Bình Sơn",
        "YODY Kỳ Anh",
        "YODY An Khê",
        "Yody Ngô Mây",
        "YODY Quảng Xương",
        "YODY Outlet",
        "Thái Bình 2",
        "YODY Quán Toan",
        "YODY Hải Hậu",
        "YODY Ngô Quyền",
        "YODY Thái Nguyên 2",
        "YODY Lạng Sơn",
        "YODY Lê Chân",
        "YODY Gia Bình",
        "YODY Thanh Hóa 2",
        "YODY Sông Công",
        "YODY Bắc Giang 2",
        "YODY Kim Thành",
        "YODY Quỳnh Côi",
        "YODY Quý Cao",
        "YODY Cẩm Phả 2",
        "YODY Lương Tài",
        "YODY Đồ Sơn",
        "YODY Ghẽ",
        "YODY Nam Sách",
        "YODY Hưng Hà",
        "YODY Đông Hưng",
        "YODY Sóc Sơn",
        "YODY Đông Triều",
        "YODY Hiệp Hòa",
        "YODY Ninh Bình 2",
        "YODY Hòa Bình",
        "YODY Quảng Yên",
        "YODY Văn Giang",
        "YODY Yên Lạc",
        "YODY Bình Xuyên",
        "YODY Triệu Sơn",
        "YODY Tiên Du",
        "YODY Diêm Điền",
        "YODY Đồi Ngô",
        "YODY Bích Động",
        "YODY An Dương",
        "YODY Kiến Thụy",
        "YODY Yên Phong",
        "YODY Ninh Giang",
        "YODY Gia Lộc",
        "YODY Tiên Lãng",
        "YODY Dân Tiến",
        "YODY Thanh Miện",
        "YODY Thuận Thành",
        "YODY Chũ",
        "YODY Tiền Trung",
        "YODY Phố Nối",
        "YODY Đồng Hới",
        "YODY Thanh Hà",
        "YODY Kinh Môn",
        "YODY Vĩnh Bảo",
        "YODY Quế Võ",
        "YODY Tứ Kỳ",
        "YODY TAM KỲ 3",
        "YODY Xuân Mai",
        "YODY Phổ Yên",
        "YODY Tiền Hải",
        "YODY Thái Bình 2",
        "YODY Mạo Khê 2",
        "YODY Vinh",
        "YODY Sơn Tây",
        "YODY Hạ Long",
        "YODY Điện Biên",
        "YODY Tam Điệp",
        "YODY Lào Cai",
        "YODY Móng Cái",
        "YODY Hà Nam",
        "YODY Bắc Ninh",
        "YODY Gia Lâm",
        "YODY Tĩnh Gia",
        "YODY Thanh Hóa",
        "YODY Từ Sơn",
        "YODY Phúc Yên",
        "YODY Thái Nguyên 3",
        "YODY Vĩnh Yên",
        "YODY Sơn La",
        "YODY Cẩm Phả",
        "YODY Việt Trì",
        "YODY Uông Bí",
        "YODY Kiến An",
        "YODY Bỉm Sơn",
        "YODY Online",
        "YODY Thủy Nguyên",
        "YODY Yên Bái",
        "YODY Nam Định",
        "YODY Tuyên Quang",
        "YODY Ngọc Lặc",
        "YODY Ninh Bình",
        "YODY Mạo Khê",
        "YODY Hồng Quang",
        "YODY Bắc Giang",
        "YODY Hưng Yên",
        "YODY Chí Linh",
        "YODY Trần Hưng Đạo",
        "YODY Kẻ Sặt",
        "YODY Thanh Trì",
        "YODY TRẦN ĐẠI NGHĨA",
        "YODY Cát Linh",
        "YODY 495 Nguyễn Thị Thập, HCM",
        "YODY Liên Nghĩa",
        "YODY Thiệu Hóa",
        "YODY Yên Dũng",
        "YODY Nguyễn Tuân",
        "YODY Đà Lạt",
        "YODY 396 Tân Sơn Nhì",
        "Yody 120 Cao Lỗ, HCM",
        "YODY Nguyễn Lương Bằng",
        "YODY Sầm Sơn",
        "YODY 239 Thống Nhất, HCM",
        "Yody Tiên Lữ",
        "YODY Hoàng Diệu",
        "YODY Yên Mỹ",
        "YODY 22-12 TP Thuận An",
        "YODY 651 Hương Lộ 3, HCM",
        "YODY Di Linh",
        "YODY Xuân La",
        "YODY Nguyễn Văn Lộc",
        "YODY Phan Thiết",
        "YODY 268 Nguyễn Văn Tăng, HCM",
        "YODY 450 Phạm Văn Chiêu, HCM",
        "YODY Thường Tín",
        "YODY Nguyễn Viết Xuân",
        "YODY Ái Nghĩa",
        "YODY HÀ GIANG",
        "YODY Ninh Kiều 1",
        "YODY Cần Thơ 2",
        "YODY 30 - 4 Cần Thơ",
        "YODY Nam Phước",
        "YODY Cần Thơ 3",
        "YODY Dĩ An",
        "YODY Nha Trang 2",
        "YODY Quang Trung",
        "YODY Phú Thọ",
        "YODY Long Xuyên",
        "YODY Yên Mỹ 2",
        "YODY Cam Ranh",
        "YODY Ngô Xuân Quảng",
        "YODY Mỹ Tho",
        "YODY 33 Bùi Hữu Nghĩa, Q5, HCM",
        "YODY Huế 2",
        "YODY Liên Hương",
        "YODY Bạc Liêu",
        "YODY Bến Lức",
        "YODY Thuận An 2",
        "YODY Thuận An 3",
        "YODY Thủ Dầu Một",
        "YODY Biên Hoà",
        "YODY Dĩ An 2",
        "YODY Vôi",
        "YODY Long Thành",
        "YODY Thuận An 4",
        "YODY Cao Lãnh",
        "YODY Long Xuyên 2",
        "YODY Lê Duẩn 3",
        "YODY Võ Văn Ngân, HCM",
        "YODY Ngã Bảy",
        "Kho Ecom",
        "YODY Phủ Lỗ",
        "YODY Kho Tổng Miền Bắc",
        "YODY Cầu Diễn",
        "YODY Bến Cát",
        "YODY Bãi Cháy",
        "YODY Xuân Hòa",
        "YODY 12 Nguyễn Trãi, Q5, HCM",
        "Hub Offline"
    ]

    data = []

    for row in soup.select('tbody.ant-table-tbody tr.ant-table-row'):
        store_name = row.select_one('td.ant-table-cell').text.strip()
        total_stock = row.select('td.ant-table-cell')[1].text.strip()
        in_stock = row.select('td.ant-table-cell')[2].text.strip()
        available_for_sale = row.select('td.ant-table-cell')[4].text.strip()

        data.append({
            'Store Name': store_name,
            'Total Stock': total_stock,
            'In Stock': in_stock,
            'Available for Sale': available_for_sale
        })

    # Tính toán tổng cho dữ liệu gốc
    total_stores_original = len(data)
    total_stock_sum_original = sum(int(item['Total Stock'].replace(",", "")) for item in data)
    in_stock_sum_original = sum(int(item['In Stock'].replace(",", "")) for item in data)
    available_for_sale_sum_original = sum(int(item['Available for Sale'].replace(",", "")) for item in data)

    # Lọc dữ liệu
    filtered_data = [item for item in data if item['Store Name'] in store_names]

    total_stores_filtered = len(filtered_data)
    total_stock_sum_filtered = sum(int(item['Total Stock'].replace(",", "")) for item in filtered_data)
    in_stock_sum_filtered = sum(int(item['In Stock'].replace(",", "")) for item in filtered_data)
    available_for_sale_sum_filtered = sum(int(item['Available for Sale'].replace(",", "")) for item in filtered_data)

    # Thêm kết quả vào danh sách log_entries với SKU
    log_entries.append({
        'Store Name': f' Original SKU: {sku} - Total ({total_stores_original} stores)',
        'Total Stock': total_stock_sum_original,
        'In Stock': in_stock_sum_original,
        'Available for Sale': available_for_sale_sum_original
    })

    log_entries.append({
        'Store Name': f'Filtered SKU: {sku} - Total ({total_stores_filtered} stores)',
        'Total Stock': total_stock_sum_filtered,
        'In Stock': in_stock_sum_filtered,
        'Available for Sale': available_for_sale_sum_filtered
    })

# Ghi kết quả vào tệp dưới dạng bảng
headers = ["Store Name", "Total Stock", "In Stock", "Available for Sale"]

with open('log_output.txt', 'w', encoding='utf-8') as f:
    f.write(tabulate(log_entries, headers="keys", tablefmt="grid"))

print("Dữ liệu đã được ghi vào file log_output.txt")
