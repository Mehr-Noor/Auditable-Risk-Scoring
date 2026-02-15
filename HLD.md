# High Level Design (HLD)
## Auditable Risk Scoring System

---

## 1. Overview

The Auditable Risk Scoring System is a production-style Machine Learning inference system designed to generate **interpretable risk scores** and **explicit, auditable decisions**.

The architecture follows a **layered, stateless design** to ensure scalability, reliability, and auditability.

---

## 2. High-Level Architecture

### Logical Flow
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
Response (Score + Decision + Reason)


---

## 3. System Components

### 3.1 Client
- External system or user
- Sends JSON or CSV inputs
- Consumes decisions and scores

---

### 3.2 API Layer
- Built with FastAPI
- Handles:
  - Input validation
  - Request/response lifecycle
  - OpenAPI documentation

---

### 3.3 Feature Engineering Layer
- Deterministic transformations
- Generates derived features
- Fully decoupled from models

---

### 3.4 ML Scoring Layer
- Loads pre-trained models at startup
- Produces probabilistic risk scores
- No business logic embedded

---

### 3.5 Risk Bucketing
- Maps continuous scores to discrete risk levels
- Threshold-based and configurable

---

### 3.6 Decision Engine
- Explicit rule-based logic
- Produces:
  - Decision (APPROVE / REVIEW / REJECT)
  - Reason code for audit

---

### 3.7 Batch Processing
- Offline inference for large datasets
- Uses same scoring and decision logic as API

---

## 4. Deployment Architecture

Docker Container
├── FastAPI Application
├── ML Models (.pkl)
├── Decision Logic
└── Batch Inference Scripts


- Stateless container
- Horizontal scaling supported

---

## 5. Non-Functional Considerations

- **Scalability:** Stateless API
- **Reliability:** Deterministic outputs
- **Auditability:** Explicit rules and reason codes
- **Maintainability:** Modular architecture

---

## 6. High-Level Diagram (Mermaid)

```mermaid
graph TD
    A[Client] --> B[FastAPI API]
    B --> C[Feature Engineering]
    C --> D[ML Scoring]
    D --> E[Risk Bucketing]
    E --> F[Decision Engine]
    F --> G[Response]

---

---

# 🔧 LLD – Low Level Design

## فایل: `LLD.md`

⬇️ **این فایل را عیناً کپی کن** ⬇️

```markdown
# Low Level Design (LLD)
## Auditable Risk Scoring System

---

## 1. Module Breakdown

### 1.1 api.py
**Responsibility**
- Expose REST endpoint `/decision`
- Handle request validation
- Orchestrate feature → scoring → decision flow

**Key Functions**
- `POST /decision`

---

### 1.2 features.py
**Responsibility**
- Feature engineering
- Data normalization
- Derived feature generation

**Key Function**
```python
build_features(df: pd.DataFrame) -> pd.DataFrame


