import joblib
import numpy as np
from src.features import build_features

logreg = joblib.load("logreg.pkl")
xgb = joblib.load("xgb.pkl")

def score(df):
    X = build_features(df)
    p1 = logreg.predict_proba(X)[:, 1]
    p2 = xgb.predict_proba(X)[:, 1]
    score = 0.4 * p1 + 0.6 * p2
    return score

def risk_bucket(score):
    if score < 0.3:
        return "LOW"
    if score < 0.6:
        return "MEDIUM"
    return "HIGH"
