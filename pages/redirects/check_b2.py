import pandas as pd
# Load the Excel file
file_path = '/Users/kanglee/PycharmProjects/pythonProject5/pages/redirects/filtered_new_gender_product.xlsx'
data = pd.read_excel(file_path)

# Rename the column MA_7 to Ma_3 and extract the first 3 characters, converting to lowercase
data['Ma_3'] = data['MA_7'].str[:3].str.lower()

# Drop the original MA_7 column
data = data[['Ma_3', 'GIOI_TINH']]

# Save the modified DataFrame to a new Excel file
output_file_path = '/Users/kanglee/PycharmProjects/pythonProject5/pages/redirects/modified_new_gender_product.xlsx'
data.to_excel(output_file_path, index=False)

# Display the first few rows of the modified data
data.head()
