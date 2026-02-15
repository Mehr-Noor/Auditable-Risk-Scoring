# Software Requirements Specification (SRS)
## Auditable Risk Scoring System

---

## 1. Introduction

### 1.1 Purpose

This document specifies the software requirements for the **Auditable Risk Scoring System**, an end-to-end Machine Learning–based system designed to generate interpretable risk scores and auditable decisions.

The SRS is intended for:
- ML Engineers
- Backend Engineers
- Data Scientists
- Reviewers and Auditors
- Technical Interviewers

---

### 1.2 Scope

The system provides:
- Probabilistic risk scoring using ML models
- Explicit, rule-based decision logic
- Real-time inference via API
- Batch inference for offline processing
- Audit-friendly outputs suitable for regulated environments

The system does **not** perform real financial decisions and uses synthetic data for demonstration purposes.

---

### 1.3 Definitions & Acronyms

| Term | Definition |
|----|-----------|
| ML | Machine Learning |
| Risk Score | Probability of default (0–1) |
| Decision Engine | Rule-based component mapping score to action |
| Auditability | Ability to explain and reproduce decisions |
| API | Application Programming Interface |

---

## 2. Overall Description

### 2.1 Product Perspective

The system is a **stateless ML inference service** composed of:
- Feature engineering layer
- Scoring layer (ML models)
- Decision layer (business rules)
- API interface
- Batch processing interface

---

### 2.2 System Architecture

Client
↓
API Layer (FastAPI)
↓
Feature Engineering
↓
ML Scoring (Ensemble Models)
↓
Risk Bucketing
↓
Decision Engine
↓
Response (Score + Decision + Reason Code)


---

### 2.3 User Classes

| User | Description |
|----|-------------|
| ML Engineer | Maintains models and scoring logic |
| Backend Engineer | Maintains API and deployment |
| Analyst | Consumes batch outputs |
| Auditor | Reviews decisions and rules |

---

### 2.4 Operating Environment

- Python 3.11
- FastAPI
- Docker container
- Localhost or cloud-based container runtime

---

## 3. Functional Requirements

### 3.1 Data Handling

**FR-1**  
The system shall accept structured numerical input features:
- age
- income
- loan_amount
- credit_history

**FR-2**  
The system shall support batch input from CSV files.

---

### 3.2 Feature Engineering

**FR-3**  
The system shall generate derived features such as:
- loan-to-income ratio
- normalized numerical features

**FR-4**  
Feature engineering logic shall be deterministic and reproducible.

---

### 3.3 Scoring

**FR-5**  
The system shall compute a probabilistic risk score in the range [0,1].

**FR-6**  
The score shall be produced using an ensemble of ML models.

**FR-7**  
The scoring layer shall not contain business decision logic.

---

### 3.4 Risk Bucketing

**FR-8**  
The system shall map scores to risk buckets:
- LOW
- MEDIUM
- HIGH

Thresholds must be configurable.

---

### 3.5 Decision Engine

**FR-9**  
The system shall determine decisions using explicit rule-based logic.

**FR-10**  
Each decision shall include a reason code suitable for audit.

**FR-11**  
Decision rules shall be deterministic and reproducible.

---

### 3.6 API Interface

**FR-12**  
The system shall expose a REST API endpoint for real-time inference.

**FR-13**  
The API shall accept JSON requests and return JSON responses.

**FR-14**  
The API shall provide auto-generated documentation (OpenAPI).

---

### 3.7 Batch Processing

**FR-15**  
The system shall support batch inference from CSV input files.

**FR-16**  
Batch output shall include scores, risk buckets, and decisions.

---

### 3.8 Testing & Reliability

**FR-17**  
The system shall include automated tests for decision logic.

**FR-18**  
The system shall validate score ranges and decision consistency.

---

## 4. Non-Functional Requirements

### 4.1 Performance

- Average API latency < 200 ms for single inference
- Batch processing scalable to thousands of records

---

### 4.2 Reliability

- Deterministic outputs for identical inputs
- Graceful handling of invalid inputs

---

### 4.3 Maintainability

- Modular code structure
- Clear separation of concerns
- Versionable model artifacts

---

### 4.4 Security

- No sensitive data storage
- Stateless API design

---

### 4.5 Auditability & Explainability

- Explicit decision rules
- Reason codes included in every decision
- Reproducible scoring logic

---

## 5. Constraints

- Synthetic data only
- No online training
- Models loaded at application startup

---

## 6. Assumptions

- Input data is numerical and pre-validated
- Thresholds are defined externally
- Deployment environment supports Docker

---

## 7. Future Enhancements

- SHAP-based explainability
- Fairness and bias analysis
- Model monitoring and drift detection
- Cloud-native deployment

---

## 8. Appendix

This SRS document is designed to reflect **real-world ML scoring systems** used in regulated environments and serves as a reference for both implementation and evaluation.
