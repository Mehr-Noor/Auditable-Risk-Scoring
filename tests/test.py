import requests

url = "http://127.0.0.1:9710/decision"

payload = {
    "age": 40,
    "income": 6000,
    "loan_amount": 20000,
    "credit_history": 8
}

response = requests.post(url, json=payload)
print(response.json())
