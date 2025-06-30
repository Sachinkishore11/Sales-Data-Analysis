- Project Overview
Company Context: Multichannel sales in both online & offline environments, across multiple regions.

Manager's Goals: Monitor historical performance, identify revenue opportunities, and track growth trends.

- Data & Tools
Data Sources: Multiple CSVs (Orders, Customers, Products, Regions).

Tools: Power BI Desktop, Power Query for ETL, DAX for calculations, Power BI Service for sharing.

- Data Preparation & Modeling
ETL & Data Cleaning

Combined CSV files via folder connector

Removed nulls, standardized columns, formatted dates and numeric types

Date Table

Created a dedicated Dates table using DAX

Marked as official "Date Table" for reliable time-intelligence

Schema Design

Built a star schema, connecting fact tables (Sales) to dimensions (Date, Product, Channel, Region)

- Key DAX Measures
Organized under a separate Key Measures table:

Total Sales

Total Profit

Total Quantity

Sales by Channel (Online vs Offline)

Year-over-Year Growth

Profit Margin (%)

Discount Impact

Examples of key DAX used:

DAX
Copy
Edit
Total Sales = SUM(Transactions[Sales])
YoY Growth % = DIVIDE([Total Sales] - CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date])), CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date])))
6. Dashboard Visuals & Interactivity
Designed to be intuitive, visually appealing, and filterable:

Overview Page:

KPI cards (Total Sales, Profit, Quantity, Discounts)

Treemap of Product Categories

Trend line of Monthly Sales

Channel Breakdown pie chart and Region map

Trend Analysis:

Line chart with Sales by Year & Month

YoY growth with conditional formatting

Channel & Region Insight:

Bar charts of Online vs Offline performance by region

Interactive slicers to filter by Date, Channel, Product

Product Analysis:

Top 10 products by sales (bar chart)

Category trend matrix

Design Considerations:

Applied consistent themes & conditional formatting

Enabled drill-down for detailed data exploration

Mobile-friendly layout ensured

- Business Impact
Identified top-performing regions and channels

![image](https://github.com/user-attachments/assets/a5d28d22-f787-42e9-9c58-c9a05d73ce42)
![image](https://github.com/user-attachments/assets/7f6b0839-7aba-4b8a-9545-6ab8eeb833ef)


Exposed seasonal sales trends and YoY growth, driving strategic planning

Highlighted top & underperforming products, aiding inventory and marketing decisions

Informed discount effectiveness and profitability strategies

