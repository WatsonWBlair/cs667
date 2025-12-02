# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a CS667 Practical Data Science coursework repository for Fall 2025, focusing on data science projects involving retail sales analysis and financial anomaly detection.

## Repository Structure

The repository contains three main project directories:

- **Projects/EDA/**: Exploratory Data Analysis project using retail sales data
- **Projects/Predictive Modeling/**: Machine learning regression models for sales prediction  
- **Projects/Anomily Detection/**: Anomaly detection using GMM and Isolation Forest algorithms

## Common Commands

Since this is primarily a Jupyter notebook-based data science project, most work is done through:

```bash
# Install Python dependencies
pip install pandas seaborn matplotlib jupyter openpyxl scikit-learn

# Start Jupyter notebook server
jupyter notebook

# Start JupyterLab (alternative)
jupyter lab
```

## Key Technologies and Libraries

- **Core Data Science Stack**: pandas, numpy, matplotlib, seaborn
- **Machine Learning**: scikit-learn (for regression, clustering, anomaly detection)
- **Notebook Environment**: Jupyter notebooks (.ipynb files)
- **Data Formats**: Excel files (.xlsx), CSV files

## Utilities and Shared Code

### engUtl.py
Located in `Projects/Predictive Modeling/engUtl.py`, contains encoding utilities:
- `targetEncode()`: Target encoding using median values
- `labelEncode()`: Integer label encoding for categorical features
- `oneHotEncode()`: One-hot encoding with pandas get_dummies

### utils.py 
Located in `Projects/Anomily Detection/utils.py`, contains anomaly detection utilities.

## Project Workflow Patterns

### EDA Project (Project 1)
Execute notebooks in sequence:
1. `data_cleaning.ipynb` - Clean raw Excel data, export to clean_data.csv
2. `feature_engineering.ipynb` - Create temporal features, export to eng_data.csv  
3. `data_visualization.ipynb` - Generate visualizations and insights

### Predictive Modeling (Project 2)
Build regression models to predict Total Sales Amount using ensemble methods like XGBoost, Random Forest.

### Anomaly Detection (Project 3)  
Implement and compare GMM and Isolation Forest algorithms for detecting financial transaction anomalies.

## Data Pipeline

Standard data flow across projects:
1. Raw data (.xlsx) → Cleaned data (.csv) → Engineered features (.csv)
2. Each step preserves previous datasets for reproducibility
3. Feature engineering includes temporal decomposition, age binning, encoding

## Best Practices for this Codebase

- Use the existing encoding utilities in `engUtl.py` for consistent data preprocessing
- Follow the established notebook execution order within each project
- Maintain the data/ subdirectories structure for input/output files
- Import shared utilities at the notebook level rather than duplicating code
- Keep visualizations in designated subdirectories (e.g. visualizations/)

## Course Context

This is academic coursework for CS667-72872 Fall 2025 at Pace University. Projects build progressively from EDA through predictive modeling to advanced anomaly detection techniques.