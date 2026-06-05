# Data Science Internship — DeveloperHub

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-orange?logo=scikit-learn)
![pandas](https://img.shields.io/badge/pandas-2.x-150458?logo=pandas)
![License](https://img.shields.io/badge/License-MIT-green)

A collection of five end-to-end data science projects completed during the DeveloperHub Data Science Internship — covering EDA, classification, regression, and unsupervised learning.

---

## Repository Structure

```
developerhub-data-science-internship/
│
├── Assignment_1/          ← EDA & Visualisation — Iris Dataset
├── Assignment_2/          ← Classification — Loan Default Prediction
├── Assignment_3/          ← Classification — Customer Retention Analytics
├── Assignment_4/          ← Regression — Medical Insurance Charges
├── Assignment_5/          ← Clustering — Customer Segmentation
│
├── requirements.txt       ← All Python dependencies
└── README.md              ← This file
```

---

## Assignments Overview

### Assignment 1 — Iris Data Exploration & Visualisation

| Property | Details |
|----------|---------|
| **Notebook** | `Assignment_1/iris-data-exploration-and-visualization/Iris_Data_Exploration.ipynb` |
| **Type** | Exploratory Data Analysis |
| **Dataset** | Iris (sklearn built-in) — 150 records · 4 features · 3 species |
| **Goal** | Identify visual patterns that separate three Iris flower species |

**Key Techniques:**
- Histograms, Box Plots, Violin Plots, Swarm Plots
- Scatter Plots, Pairplot
- Correlation Heatmap

**Key Finding:** Petal length and petal width alone are sufficient to perfectly separate *Setosa* from the other two species.

---

### Assignment 2 — Loan Default Prediction

| Property | Details |
|----------|---------|
| **Notebook** | `Assignment_2/loan-default-analysis/Loan_Default_Prediction.ipynb` |
| **Type** | Binary Classification |
| **Dataset** | `Loan_default.csv` — 255,347 records · 18 features |
| **Target** | `Default` (0 = No Default · 1 = Default) |
| **Models** | Logistic Regression · Decision Tree |

**Key Techniques:**
- EDA with class imbalance analysis
- Label encoding · One-hot encoding
- Class-balanced Logistic Regression
- ROC-AUC · Threshold tuning · Risk tier bucketing

**Model Performance:**

| Model | Accuracy | ROC-AUC |
|-------|----------|---------|
| Logistic Regression | 88.53% | 0.75+ |
| Decision Tree | 88.52% | 0.73+ |
| LR Balanced (improved) | ~68% | **0.75 (better recall)** |

---

### Assignment 3 — Customer Retention Analytics

| Property | Details |
|----------|---------|
| **Notebook** | `Assignment_3/customer-retention-analytics/Customer_Retention_Analytics.ipynb` |
| **Type** | Binary Classification · Business Analytics |
| **Dataset** | Synthetic Telecom — 7,043 records · 17 features |
| **Target** | `churn` (0 = Retained · 1 = Churned) |
| **Models** | Logistic Regression · Decision Tree |

**Key Techniques:**
- Churn rate analysis by segment
- Categorical churn rate bar charts
- Tenure bucket analysis
- ROC curves · Feature importance

**Key Finding:** Month-to-month contracts and short tenure (<12 months) are the top two churn predictors.

---

### Assignment 4 — Medical Insurance Charge Prediction

| Property | Details |
|----------|---------|
| **Notebook** | `Assignment_4/notebooks/analysis.ipynb` |
| **Type** | Regression |
| **Dataset** | `data/insurance.csv` — 1,338 records · 7 features |
| **Target** | `charges` — annual USD insurance claim amount |
| **Model** | Linear Regression (scikit-learn) |

**Key Techniques:**
- Feature engineering (interaction terms: age×bmi, smoker×bmi)
- Label encoding · One-hot encoding
- 5-fold cross-validation
- Residual analysis · Feature coefficient plots

**Model Performance:**

| Metric | Train | Test |
|--------|-------|------|
| R² Score | 0.9880 | 0.9880 |
| MAE | $2,012 | $1,910 |
| RMSE | $2,515 | $2,449 |

**Key Finding:** Smoking is the #1 cost driver — smokers pay ~4× more than non-smokers.

---

### Assignment 5 — Customer Segmentation (K-Means Clustering)

| Property | Details |
|----------|---------|
| **Notebook** | `Assignment_5/Customer_Segmentation.ipynb` |
| **Type** | Unsupervised Learning · Clustering |
| **Dataset** | Synthetic E-Commerce — 2,000 records · 6 features |
| **Algorithm** | K-Means Clustering |

**Key Techniques:**
- Elbow Method & Silhouette Score for optimal K
- StandardScaler for feature normalisation
- PCA for 2D cluster visualisation
- Radar chart for segment profiling

**Segments Identified:**

| Segment | Size | Description |
|---------|------|-------------|
| Budget Shoppers | ~30% | Low income, infrequent, price-sensitive |
| Regular Customers | ~40% | Mid-tier, core customer base |
| Premium Customers | ~30% | High income, frequent, high order value |

---

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Ahaulakh0890/developerhub-data-science-internship.git
cd developerhub-data-science-internship
```

### 2. Create & Activate Virtual Environment

A **single shared environment** covers all 5 assignments — no need for separate envs.

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch Jupyter

```bash
jupyter notebook
```

Then open any `.ipynb` file from the assignment folders.

> **Note:** Select the `.venv` kernel inside Jupyter via *Kernel → Change Kernel → Python (.venv)*.

---

## Technologies Used

| Library | Purpose |
|---------|---------|
| `pandas` | Data loading, manipulation, groupby analysis |
| `numpy` | Numerical operations, array manipulation |
| `matplotlib` | Base plotting and figure customisation |
| `seaborn` | Statistical visualisation (heatmaps, violin plots, pairplots) |
| `scikit-learn` | ML models, preprocessing, metrics, datasets |
| `joblib` | Model serialisation (saving/loading .pkl / .joblib files) |
| `jupyter` | Interactive notebook environment |

---

## Learning Outcomes

- End-to-end data science project workflow (EDA → preprocessing → modelling → evaluation)
- Handling imbalanced datasets with class weighting
- Feature engineering for linear and tree-based models
- Unsupervised clustering and business interpretation of segments
- Model evaluation beyond accuracy: ROC-AUC, F1, Silhouette Score

---

*DeveloperHub Data Science Internship — 2026*
