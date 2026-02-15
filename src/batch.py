import pandas as pd
from src.scoring import score, risk_bucket
from src.decision import make_decision

df = pd.read_csv("data/credit_data.csv").head(10)

scores = score(df)

for i, s in enumerate(scores):
    decision, reason = make_decision(s, df.iloc[i]["age"])
    print(i, round(s, 3), risk_bucket(s), decision, reason)
