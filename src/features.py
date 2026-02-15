import pandas as pd

FEATURES = [
    "age",
    "income",
    "loan_amount",
    "credit_history",
    "loan_to_income"
]

def build_features(df: pd.DataFrame):
    return df[FEATURES]
