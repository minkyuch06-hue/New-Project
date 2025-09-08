# cleaning_script.py
"""
This script cleans the Online Retail dataset using pandas.

Steps:
1. Reads the CSV file with proper encoding to handle special characters.
2. Drops rows where 'CustomerID' is null.
3. Filters out rows where 'InvoiceNo' starts with 'C' (cancelled orders).
4. Creates a new 'Revenue' column = Quantity * UnitPrice.
5. Saves the cleaned dataset to 'clean_retail_data.csv' without the index.
"""

import pandas as pd

def clean_retail_data(input_file: str, output_file: str):
    # Step 1: Read the input CSV with correct encoding
    # 'ISO-8859-1' handles special characters in this dataset better than default UTF-8
    df = pd.read_csv(input_file, encoding="ISO-8859-1")
    
    # Print initial row count
    print(f"Number of rows before cleaning: {len(df)}")
    
    # Step 2: Drop rows with null CustomerID
    df = df.dropna(subset=["CustomerID"])
    
    # Step 3: Remove rows where InvoiceNo starts with 'C'
    df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]
    
    # Step 4: Create a new 'Revenue' column
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]
    
    # Print final row count
    print(f"Number of rows after cleaning: {len(df)}")
    
    # Step 5: Save cleaned DataFrame to CSV (without index)
    df.to_csv(output_file, index=False)
    print(f"✅ Cleaned file saved as: {output_file}")


if __name__ == "__main__":
    # Run the function with the given input/output
    clean_retail_data("OnlineRetail.csv", "clean_retail_data.csv")
