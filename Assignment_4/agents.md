
# agents.md

## Project: Medical Insurance Claim Amount Prediction

### Objective
Estimate the medical insurance claim amount based on personal data using machine learning.

Dataset:
- Medical Cost Personal Dataset
- User will upload the CSV file into the project folder

---

## Project Requirements

### 1. Jupyter Notebook

The notebook must include:

- Introduction and problem statement
- Dataset understanding and description
- Data cleaning and preparation
- Exploratory Data Analysis (EDA) with graphs
- Model training and testing
- Evaluation metrics (MAE, RMSE, and regression metrics)
- Conclusion summarizing key insights

---

### 2. Code Quality

- Code should be clean and well-structured
- Include comments explaining each step
- Use modular functions where possible
- Follow consistent naming conventions

---

## ML Requirements

- Train a Linear Regression model to predict insurance charges
- Visualize impact of:
  - BMI vs Charges
  - Age vs Charges
  - Smoking Status vs Charges
- Evaluate model using:
  - MAE
  - RMSE
  - R² Score

---

## Additional Value Additions

### Feature Engineering
- Create additional useful features if beneficial
- Detect and handle outliers
- Check missing values and duplicates

### Advanced Insights
- Correlation heatmap
- Feature importance/coefficients analysis
- Distribution plots
- Pair plots
- Residual analysis

### Deliverables

Project structure:

project/
│
├── data/
│   └── medical_cost.csv
│
├── notebooks/
│   └── medical_claim_prediction.ipynb
│
├── charts/
│   ├── age_vs_charges.png
│   ├── bmi_vs_charges.png
│   ├── smoking_vs_charges.png
│   ├── correlation_heatmap.png
│   └── residual_analysis.png
│
├── models/
│   └── linear_regression.pkl
│
├── README.md
│
└── agents.md

Mandatory:
- Save ALL generated charts/images automatically in a separate charts folder
- Automatically generate a professional README.md file after project completion
- Save trained model for reuse
- Include interpretation of model performance and business insights
