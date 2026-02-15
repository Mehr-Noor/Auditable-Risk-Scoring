from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from src.scoring import score, risk_bucket
from src.decision import make_decision

app = FastAPI()

class Request(BaseModel):
    age: int
    income: float
    loan_amount: float
    credit_history: int

@app.post("/decision")
def decision(req: Request):
    df = pd.DataFrame([{
        "age": req.age,
        "income": req.income,
        "loan_amount": req.loan_amount,
        "credit_history": req.credit_history,
        "loan_to_income": req.loan_amount / req.income
    }])

    s = score(df)[0]
    decision, reason = make_decision(s, req.age)

    return {
        "score": round(float(s), 3),
        "risk_level": risk_bucket(s),
        "decision": decision,
        "reason": reason
    }
