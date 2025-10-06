# Retail Sales Exploratory Data Analysis (EDA) Project

## Project Overview

This project performs comprehensive exploratory data analysis on retail sales data as part of CS667 course (Fall 2025). The analysis examines customer purchasing behavior across different product categories, demographics, and temporal patterns to uncover meaningful insights about retail sales performance.

The project analyzes retail transaction data including customer demographics (age, gender), product information (category, price, quantity), and temporal patterns to identify trends and relationships that can inform business decisions.

## Project Structure

```text
EDA/
├── CS667-72872-Fa2025-Project-1.pdf   # Project requirements and specifications
├── README.md                           # Project documentation (this file)
├── data_cleaning.ipynb                 # Data preprocessing and cleaning
├── feature_engineering.ipynb           # Feature creation and transformation
├── data_visualization.ipynb            # Exploratory data analysis and visualizations
└── data/
    ├── retail_sales.xlsx              # Original raw data
    ├── clean_data.csv                 # Cleaned dataset
    └── eng_data.csv                   # Engineered features dataset
```

## Data Description

The retail sales dataset contains the following key attributes:

- **Transaction Information**: Transaction ID, Date
- **Customer Demographics**: Customer ID, Age, Gender
- **Product Details**: Product Category, Price per Unit, Quantity
- **Financial Metrics**: Total Amount (calculated from quantity × price per unit)

## Notebook Execution Order

Execute the Jupyter notebooks in the following sequence:

### 1. **data_cleaning.ipynb**

- **Purpose**: Clean and preprocess the raw retail sales data
- **Key Operations**:
  - Load raw Excel data (`retail_sales.xlsx`)
  - Convert column names to snake_case format
  - Validate data integrity (verify total_amount calculations)
  - Remove non-descriptive columns (transaction_id, customer_id)
  - Export cleaned data to `clean_data.csv`
- **Output**: `data/clean_data.csv`

### 2. **feature_engineering.ipynb**

- **Purpose**: Create derived features for enhanced analysis
- **Key Operations**:
  - Parse date fields into temporal components (year, month, day, day of week, quarter)
  - Create human-readable labels for months and days of week
  - Generate age groups/bins (20-29, 30-39, 40-49, 50-59, 60+)
  - Export engineered features to `eng_data.csv`
- **Output**: `data/eng_data.csv`

### 3. **data_visualization.ipynb**

- **Purpose**: Visualize patterns and relationships in the data
- **Key Visualizations**:
  - Violin plots: Age distribution by gender and product category
  - Box plots: Price distribution across product categories
  - Count plots: Quantity patterns by product category
  - Heatmap: Sales patterns by day of week and month
  - Scatter plots: Age vs spending relationships
  - Pair plots: Correlations between numerical variables
  - Distribution plots: Sales distribution by gender and product category

## Key Insights

The analysis explores:

- Customer demographic patterns in purchasing behavior
- Price variations across different product categories
- Seasonal and weekly sales trends
- Relationships between customer age, gender, and spending habits
- Product category preferences by customer segments

## Requirements

- Python 3.x
- pandas
- seaborn
- matplotlib
- Jupyter Notebook/JupyterLab

## Installation

```bash
# Install required packages
pip install pandas seaborn matplotlib jupyter openpyxl
```

## Usage

1. Clone or download the project directory
2. Ensure all data files are in the `data/` subdirectory
3. Open Jupyter Notebook/JupyterLab
4. Execute the notebooks in the order specified above
5. Review the generated visualizations and insights

## AI Usage Disclosure

This project utilized AI assistance for the following purposes:

- README file generation and formatting
- Documentation structure and organization
- Markdown syntax formatting

**Important Note**: AI was NOT used for any code generation in the Jupyter notebooks. All data analysis code, data cleaning procedures, feature engineering logic, and visualization implementations were developed without AI assistance.

## Author
Watson Blair
watsonwblair@gmail.com
wb43728n@pace.edu
U00700851

## Course:
CS667-72872 Fall 2025
