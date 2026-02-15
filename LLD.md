
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


