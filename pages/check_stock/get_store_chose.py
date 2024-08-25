from selenium import webdriver

# Khởi tạo WebDriver (ví dụ này dùng Chrome)
driver = webdriver.Chrome()

# Mở trang web chứa dropdown
driver.get("URL_of_the_page_with_dropdown")

# Tìm các mục đã chọn trong dropdown
selected_items = driver.find_elements_by_css_selector(".ant-select-selection-item-content")

# Lấy và in ra giá trị của các mục đã chọn
selected_values = [item.text for item in selected_items]
for value in selected_values:
    print(value)

# Đóng trình duyệt
driver.quit()