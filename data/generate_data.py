import numpy as np
import pandas as pd

np.random.seed(42)
N = 5000

age = np.random.randint(21, 65, N)
income = np.random.normal(5000, 2000, N).clip(1000)
loan_amount = np.random.normal(15000, 8000, N).clip(1000)
credit_history = np.random.randint(1, 20, N)

loan_to_income = loan_amount / income

# risk logic (ground truth – noisy)
risk_score = (
    0.4 * loan_to_income +
    0.3 * (credit_history < 5).astype(int) +
    0.2 * (income < 3000).astype(int) +
    0.1 * (age < 25).astype(int)
)

prob_default = 1 / (1 + np.exp(-risk_score))
default = np.random.binomial(1, prob_default)

df = pd.DataFrame({
    "age": age,
    "income": income,
    "loan_amount": loan_amount,
    "credit_history": credit_history,
    "loan_to_income": loan_to_income,
    "default": default
})

df.to_csv("data/credit_data.csv", index=False)
print("✅ data/credit_data.csv generated")
