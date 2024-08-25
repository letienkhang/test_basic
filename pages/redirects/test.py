import pandas as pd

# Step 1: Load the Excel file
file_path = '/Users/kanglee/PycharmProjects/pythonProject5/pages/redirects/new_gender_product.xlsx'
data = pd.read_excel(file_path)

# Step 2: Read the list of MA_7 codes from the text file
with open('/Users/kanglee/PycharmProjects/pythonProject5/pages/redirects/data.txt', 'r') as file:
    product_codes = file.read().splitlines()

# Step 3: Filter the data to include only rows with MA_7 values in the provided list
filtered_data = data[data['MA_7'].isin(product_codes)]

# Step 4: Save the filtered data to a new Excel file
output_file_path = '/Users/kanglee/PycharmProjects/pythonProject5/pages/redirects/filtered_new_gender_product.xlsx'
filtered_data.to_excel(output_file_path, index=False)

# Optional: Display the first few rows of the filtered data
print(filtered_data)