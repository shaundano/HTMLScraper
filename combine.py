import pandas as pd
import os

# Directory containing the Excel files
folder_path = "Excel data"

# Get a list of all Excel files in the directory
excel_files = [f for f in os.listdir(folder_path) if f.endswith(".xlsx")]

# Create a new Excel workbook named "combined_file.xlsx"
with pd.ExcelWriter("combined_file.xlsx", engine="xlsxwriter") as writer:
    for file in excel_files:
        # Read each Excel file into a DataFrame
        df = pd.read_excel(os.path.join(folder_path, file))
        
        # Use the first 31 characters of the file name (without the extension) as the sheet name
        sheet_name = os.path.splitext(file)[0][:31]
        
        # Write the DataFrame to a new sheet in the combined Excel file
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Excel files combined successfully into 'combined_file.xlsx'.")
