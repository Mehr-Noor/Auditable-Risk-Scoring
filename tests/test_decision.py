from src.batch import score, risk_bucket, make_decision
import pandas as pd

df = pd.read_csv("data/credit_data.csv").head(5)
scores = score(df)

for i, s in enumerate(scores):
    decision, reason = make_decision(s, df.iloc[i]["age"])
    print(i, round(s, 3), risk_bucket(s), decision, reason)
