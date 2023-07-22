import pandas as pd
import requests
import json

df = pd.read_csv('userdata2.csv')

for(i, row) in df.iterrows():
    print({
        "user": 1,
        "account": 1,
        "category": row['category'].upper()[:3],
        "transaction_type": row['type'],
        "amount": row['amount'],
        "timestamp": row['timestamp'],
        "description": "dummy description",
        "narration": row["narration"],
        "initial_balance": row['initialBalance'],
        "mode": row['mode'][:3]
    })

    json_data = json.dumps({
        "account": 3,
        "category": row['category'].upper()[:3],
        "transaction_type": row['type'],
        "amount": row['amount'],
        "timestamp": row['timestamp'],
        "description": "dummy description",
        "narration": row["narration"],
        "initial_balance": row['initialBalance'],
        "mode": row['mode'][:3]
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkwMjU5MTIwLCJpYXQiOjE2ODk5OTk5MjAsImp0aSI6IjA3ZmU2NzA3NWI5MzRhZGY5ZDFmYWZlZmMzNGQ5OTA2IiwidXNlcl9pZCI6Nn0.D07k2fpxs6m2OPtPX8kee9p7BQLmToqJTnChXJryRHU',
    }

    requests.post('http://127.0.0.1:8000/api/bank/transaction/', headers=headers, data=json_data)