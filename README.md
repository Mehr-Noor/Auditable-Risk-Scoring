# 🧠 Auditable Risk Scoring System (MVP)

An end-to-end **auditable Machine Learning scoring and decision system** designed to demonstrate real-world ML engineering skills beyond training simple classifiers.

This project simulates how **risk scoring systems** are built in production environments such as banking, lending, insurance, and other compliance-driven domains.

---

## 🎯 Project Objectives

- Design **interpretable and defensible ML scoring models**
- Clearly separate **scoring** from **decision logic**
- Support **real-time inference (API)** and **batch processing**
- Enable **auditability, reliability, and testing**
- Demonstrate evaluation, validation, and ensemble modeling techniques

---

## 🏗️ High-Level Architecture

Input (JSON / CSV)
↓
Feature Engineering
↓
ML Scoring (Probabilistic)
↓
Risk Bucketing
↓
Decision Engine (Explicit Rules)
↓
Audit-Friendly Output
---

**Core principle:**  
> Models produce *scores*. Decisions are made by explicit, auditable rules.

---

## 📁 Project Structure

Auditable-Risk-Scoring/
│
├── data/
│ └── credit_data.csv # Synthetic dataset
│
├── src/
│ ├── features.py # Feature engineering logic
│ ├── train.py # Model training & evaluation
│ ├── scoring.py # Scoring layer (ML inference)
│ ├── decision.py # Decision logic (business rules)
│ ├── api.py # FastAPI real-time service
│ └── batch.py # Batch inference pipeline
│
├── tests/
│ └── test_decision.py # Reliability & decision tests
│
├── logreg.pkl # Trained Logistic Regression model
├── xgb.pkl # Trained XGBoost model
├── requirements.txt
└── README.md

---

---

## 📊 Data & Feature Engineering

Synthetic data is generated to simulate realistic credit-risk behavior while avoiding sensitive real-world data.

**Base features**
- `age`
- `income`
- `loan_amount`
- `credit_history`

**Derived features**
- `loan_to_income_ratio`
- normalized numerical inputs

Feature engineering is fully decoupled from model logic to ensure reproducibility and auditability.

---

## 🤖 Machine Learning Models

### Logistic Regression
- Interpretable baseline model
- Serves as an audit reference

### XGBoost
- High predictive power
- Captures non-linear feature interactions

### Ensemble Scoring

Final risk score is computed as a weighted average of model probabilities:

final_score = 0.5 × Logistic Regression + 0.5 × XGBoost


This improves robustness and score stability.

---

## 📈 Evaluation & Validation

- Train / validation split
- ROC-AUC as the primary metric
- Ensemble performance comparison

Example result:
Ensemble AUC ≈ 0.74


---

## 🎯 Scoring, Risk Bucketing & Decision Logic

### Risk Buckets

| Score Range | Risk Level |
|------------|------------|
| < 0.30 | LOW |
| 0.30 – 0.60 | MEDIUM |
| > 0.60 | HIGH |

### Decision Rules

| Risk Level | Decision | Reason Code |
|-----------|----------|-------------|
| LOW | APPROVE | LOW_RISK |
| MEDIUM | REVIEW | MEDIUM_RISK |
| HIGH | REJECT | HIGH_RISK |

All decision rules are **explicit, deterministic, and audit-ready**.

---

## 🚀 Real-Time Inference API

The system is exposed as a backend service using FastAPI.

### Run the API
```bash
uvicorn src.api:app --reload


Swagger UI
http://127.0.0.1:8000/docs

Example Request
{
  "age": 40,
  "income": 6000,
  "loan_amount": 20000,
  "credit_history": 8
}
