# api.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Carrega modelo e colunas
model = joblib.load("xgb_optuna_model_final.pkl")
selected_features = [
    'tenure_months', 'monthly_charges', 'total_charges',
    'senior_citizen_no', 'partner_no', 'dependents_no',
    'multiple_lines_no', 'online_security_no', 'online_backup_no',
    'tech_support_no', 'streaming_movies_yes',
    'contract_month_to_month', 'contract_one_year',
    'paperless_billing_no', 'payment_method_electronic_check'
]

class ClienteInput(BaseModel):
    tenure_months: float
    monthly_charges: float
    total_charges: float
    senior_citizen_no: int
    partner_no: int
    dependents_no: int
    multiple_lines_no: int
    online_security_no: int
    online_backup_no: int
    tech_support_no: int
    streaming_movies_yes: int
    contract_month_to_month: int
    contract_one_year: int
    paperless_billing_no: int
    payment_method_electronic_check: int

@app.post("/predict")
def predict_churn(dados: ClienteInput):
    input_df = pd.DataFrame([dados.dict()])
    input_df = input_df[selected_features]  # Garante ordem
    prediction = model.predict_proba(input_df)[0,1]  # Probabilidade de churn
    return {"churn_probability": round(prediction, 4)}
per