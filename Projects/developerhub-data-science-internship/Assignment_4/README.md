# 🏥 Medical Insurance Claim Amount Prediction

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-orange?logo=scikit-learn)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter)
![License](https://img.shields.io/badge/License-MIT-green)

> **Predict annual medical insurance charges** for individual customers using demographic and health data — a production-ready ML regression project.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Dataset Information](#dataset-information)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Methodology](#methodology)
- [Model Performance](#model-performance)
- [Key Insights](#key-insights)
- [Visualisations](#visualisations)
- [Future Improvements](#future-improvements)

---

## 🎯 Project Overview

Medical insurance companies must accurately price premiums and forecast claim amounts. This project builds a **Linear Regression model** trained on the Medical Cost Personal Dataset to predict annual insurance charges.

**Business value:**
- Reduces pricing errors that lead to financial losses or customer churn
- Identifies the highest-risk customer profiles for proactive intervention
- Enables data-driven premium setting and actuarial decision-making

---

## 📊 Dataset Information

| Property | Value |
|----------|-------|
| **Name** | Medical Cost Personal Dataset |
| **Rows** | 1,338 |
| **Columns** | 7 (6 features + 1 target) |
| **Target** | `charges` — annual USD claim amount |
| **File** | `data/medical_cost.csv` |

### Feature Descriptions

| Feature | Type | Range / Values | Description |
|---------|------|---------------|-------------|
| `age` | Integer | 18–64 | Age of primary beneficiary |
| `sex` | Categorical | male, female | Gender of beneficiary |
| `bmi` | Float | 15.96–53.13 | Body Mass Index |
| `children` | Integer | 0–5 | Number of dependents |
| `smoker` | Categorical | yes, no | Tobacco use |
| `region` | Categorical | NE, NW, SE, SW | US residential region |
| **`charges`** | **Float** | **$1,122–$88,914** | **Annual insurance charges (target)** |

---

## ⚙️ Installation

### Prerequisites

```bash
Python 3.10+
```

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib jupyter nbformat
```

### Run the Project

```bash
# Option 1: Run the full pipeline script
python run_pipeline.py

# Option 2: Open the Jupyter Notebook
jupyter notebook notebooks/medical_claim_prediction.ipynb
```

> 📁 Place your CSV file in the `data/` folder. The pipeline auto-detects it.

---

## 📁 Project Structure

```
project/
│
├── data/
│   └── medical_cost.csv               ← Input dataset
│
├── notebooks/
│   └── medical_claim_prediction.ipynb ← Main analysis notebook
│
├── charts/                            ← All visualisations (PNG)
│   ├── charges_distribution.png
│   ├── age_vs_charges.png
│   ├── bmi_vs_charges.png
│   ├── smoking_vs_charges.png
│   ├── correlation_heatmap.png
│   ├── pairplot.png
│   ├── region_analysis.png
│   ├── children_vs_charges.png
│   ├── gender_vs_charges.png
│   ├── feature_distributions.png
│   ├── residual_analysis.png
│   ├── feature_coefficients.png
│   └── model_metrics_dashboard.png
│
├── models/
│   └── linear_regression.pkl          ← Saved trained model
│
├── run_pipeline.py                    ← Full pipeline runner
├── README.md                          ← This file
└── agents.md                          ← Project specification
```

---

## 🔬 Methodology

### 1. Data Loading & Validation
- Auto-load any CSV from the `data/` folder
- Validate shape, dtypes, missing values, and duplicates

### 2. Data Cleaning
| Step | Action |
|------|--------|
| Duplicates | Removed |
| Missing values | Median (numeric) / Mode (categorical) imputation |
| Outliers | Detected via IQR; `charges` winsorized at 99th percentile |

### 3. Feature Engineering
New interaction features to capture non-linear relationships:

| Feature | Formula | Purpose |
|---------|---------|---------|
| `age_bmi` | age × bmi | Combined aging + weight risk |
| `smoker_bmi` | smoker × bmi | Amplified smoking+BMI effect |
| `age_smoker` | age × smoker | Older smokers pay more |
| `bmi_obese` | bmi ≥ 30 → 1 | Obesity binary flag |

### 4. Encoding
- `sex`: Label encoded (female=0, male=1)
- `smoker`: Binary (no=0, yes=1)
- `region`: One-hot encoded (drop_first=True)

### 5. Model
- **Algorithm**: Linear Regression (scikit-learn)
- **Split**: 80% train / 20% test (random_state=42)
- **Validation**: 5-fold cross-validation

---

## 📈 Model Performance

| Metric | Train | Test |
|--------|-------|------|
| **MAE** | $2,012 | $1,910 |
| **RMSE** | $2,515 | $2,449 |
| **R² Score** | 0.9880 | 0.9880 |
| **CV R²** | — | 0.9875 ± 0.0026 |

### ✅ Interpretation
- **R² = 0.988** — the model explains **98.8%** of the variance in insurance charges
- Negligible train/test gap confirms **no overfitting**
- Consistent CV scores indicate **robust generalisation**
- MAE of ~$1,910 means predictions are accurate to within ~$1,910 on average

---

## 💡 Key Insights

### Top Findings
1. 🚬 **Smoking is the #1 predictor** — smokers pay ~4× more than non-smokers
2. 💥 **Smoking × BMI interaction** is the single largest coefficient — a heavy smoker with high BMI is the highest-risk profile
3. 📅 **Age adds ~$250/year** in expected charges for non-smokers
4. ⚖️ **Obesity (BMI ≥ 30)** adds a meaningful cost premium, especially for smokers
5. 🗺️ **Region and sex are weak predictors** — pricing should not heavily rely on them

### Business Recommendations
| Recommendation | Business Impact |
|----------------|----------------|
| Apply 3–4× smoking premium | Largest cost driver; actuarially justified |
| Create BMI–smoking risk tiers | Most accurate segmentation of high-risk customers |
| Offer smoking cessation incentives | Reduces long-term claims |
| Age-banded pricing for 50+ | Disproportionately higher charges in that cohort |
| BMI wellness programs | Preventive cost reduction for obese non-smokers |

---

## 📊 Visualisations

All 13 charts are saved in the `charts/` folder:

| Chart | File |
|-------|------|
| Charges distribution | `charges_distribution.png` |
| Age vs Charges | `age_vs_charges.png` |
| BMI vs Charges | `bmi_vs_charges.png` |
| Smoking vs Charges | `smoking_vs_charges.png` |
| Correlation heatmap | `correlation_heatmap.png` |
| Pair plot | `pairplot.png` |
| Region analysis | `region_analysis.png` |
| Children analysis | `children_vs_charges.png` |
| Gender analysis | `gender_vs_charges.png` |
| Feature distributions | `feature_distributions.png` |
| Residual analysis | `residual_analysis.png` |
| Feature coefficients | `feature_coefficients.png` |
| Metrics dashboard | `model_metrics_dashboard.png` |

---

## 🔮 Future Improvements

- [ ] **Ensemble models** — Random Forest, XGBoost, LightGBM
- [ ] **Log-transform target** — handle right-skewed charges more effectively
- [ ] **Polynomial features** — capture higher-order BMI / age effects
- [ ] **Hyperparameter tuning** — GridSearchCV / Optuna
- [ ] **Additional features** — chronic conditions, exercise habits, prior claims
- [ ] **REST API deployment** — FastAPI + Docker container
- [ ] **Model monitoring** — data drift detection in production
- [ ] **SHAP values** — model explainability for business stakeholders

---

## 📝 License

This project is licensed under the MIT License.

---

*Generated automatically as part of the Medical Insurance Claim Prediction ML Project.*
