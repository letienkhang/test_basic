import pandas as pd

# Load both Excel files
file_1_path = '/Users/kanglee/PycharmProjects/pythonProject5/pages/redirects/modified_new_gender_product_love.xlsx'
file_2_path = '/Users/kanglee/PycharmProjects/pythonProject5/pages/redirects/modified_new_gender_product.xlsx'

# Perform the comparison between the two files on Ma_3
merged_data = pd.merge(data_1, data_2, on='Ma_3', how='outer', suffixes=('_file1', '_file2'))

# Add a column to flag discrepancies in GIOI_TINH
merged_data['comparison'] = merged_data.apply(
    lambda row: row['GIOI_TINH_file1'] if row['GIOI_TINH_file1'] == row['GIOI_TINH_file2'] else '--', axis=1
)

# Select relevant columns for output
comparison_result = merged_data[['Ma_3', 'GIOI_TINH_file1', 'GIOI_TINH_file2', 'comparison']]

# Save the result to a text file
output_file_path = '/mnt/data/ma3_comparison_result.txt'
comparison_result.to_csv(output_file_path, index=False, sep='\t')

output_file_path

# Save the comparison result to an Excel file as well
output_excel_path = '/mnt/data/ma3_comparison_result.xlsx'
comparison_result.to_excel(output_excel_path, index=False)

output_excel_path