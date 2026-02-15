import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score
from src.features import build_features

df = pd.read_csv("data/credit_data.csv")
X = build_features(df)
y = df["default"]

Xtr, Xte, ytr, yte = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

logreg = LogisticRegression(class_weight="balanced", max_iter=1000)
xgb = XGBClassifier(
    max_depth=3,
    n_estimators=100,
    learning_rate=0.1,
    eval_metric="logloss"
)

logreg.fit(Xtr, ytr)
xgb.fit(Xtr, ytr)

logreg_pred = logreg.predict_proba(Xte)[:, 1]
xgb_pred = xgb.predict_proba(Xte)[:, 1]

ensemble_pred = 0.4 * logreg_pred + 0.6 * xgb_pred

print("LogReg AUC:", roc_auc_score(yte, logreg_pred))
print("XGB AUC:", roc_auc_score(yte, xgb_pred))
print("Ensemble AUC:", roc_auc_score(yte, ensemble_pred))

joblib.dump(logreg, "logreg.pkl")
joblib.dump(xgb, "xgb.pkl")
print("✅ models saved")
