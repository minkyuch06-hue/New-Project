# Retail FP&A Dashboard

## Live Dashboard on Tableau Public
[**Click here to view the interactive dashboard**](https://public.tableau.com/app/profile/jeremy.choi/viz/RetailFPATableauDashboard-JeremyChoi/Dashboard1?publish=yes)

---

### Project Overview

This project is an interactive Financial Planning & Analysis (FP&A) dashboard built to analyze a sample of transactions from a UK-based online retailer. The objective was to transform raw transactional data into a high-level strategic tool for a non-technical stakeholder, focusing on key business metrics like revenue, customer acquisition, and product performance.

### Key Features

*   **KPI Summary:** At-a-glance view of Total Revenue, Total Unique Customers, and Average Order Value (AOV).
*   **"What-If" Discount Simulator:** An interactive parameter that allows a user to model the impact of a percentage discount on total revenue, demonstrating the trade-off between promotions and profitability.
*   **Revenue by Product:** A sorted bar chart identifying the most profitable products by StockCode.
*   **Sales by Country:** A geographic map visualizing revenue distribution across different countries.

### Technical Details

*   **Data Cleaning (ETL):** The raw `.csv` data was cleaned and processed using a Python script with the `pandas` library. Key steps included removing cancelled orders, dropping entries with null Customer IDs, and engineering a "Revenue" feature. The full process is documented in `DATA_CLEANING.md`.
*   **Data Visualization:** The dashboard was built using Tableau Public.

### Dashboard Preview

![Dashboard Preview](dashboard_screenshot.png)
