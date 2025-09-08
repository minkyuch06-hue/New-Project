# Data Cleaning Process for Online Retail Dataset

The following steps were performed using a Python script with the pandas library to clean the raw `OnlineRetail.csv` dataset.

- **Initial State:** The raw dataset contained `XXXXXX` rows.
- **Step 1 (Null Customer IDs):** Rows with a null `CustomerID` were dropped. These transactions cannot be tied to a specific customer and are not useful for retention or cohort analysis.
- **Step 2 (Cancelled Orders):** Rows where the `InvoiceNo` number started with 'C' were filtered out. These represent cancelled or returned orders and should not be included in revenue calculations.
- **Step 3 (Feature Engineering):** A `Revenue` column was created by multiplying `Quantity` by `UnitPrice`.
- **Final State:** The cleaned dataset, saved as `clean_retail_data.csv`, contains `XXXXXX` rows.