from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np
from retention_rules import definir_acao_recomendacao

app = FastAPI()

# Carrega modelo e colunas
with open("lgbm_rand_model_12.pkl", "rb") as f:
    modelo = pickle.load(f)

with open("modelo_colunas.pkl", "rb") as f:
    colunas = pickle.load(f)

# Base de clientes para predição por ID
df = pd.read_csv("final_model_12.csv")

class DadosCliente(BaseModel):
    contract: float
    dependents: float
    monthly_charges: float
    online_security: float
    payment_method: float
    tech_support: float
    tenure_months: float
    internet_service: float
    online_backup: float
    paperless_billing: float
    partner: float
    streaming_movies: float

@app.post("/predict")
def predict_churn_manual(dados: DadosCliente):
    entrada = pd.DataFrame([dados.dict()])
    entrada = entrada[colunas]
    proba = modelo.predict_proba(entrada)[:, 1][0]
    acoes = definir_acao_recomendacao(entrada, proba)
    return {"churn_proba": float(proba), "acoes": acoes}

@app.get("/predict_id/{customer_id}")
def predict_churn_por_id(customer_id: str):
    cliente = df[df["customer_id"] == customer_id]
    if cliente.empty:
        return {"erro": "Cliente não encontrado"}

    entrada = cliente[colunas]
    proba = modelo.predict_proba(entrada)[:, 1][0]
    acoes = definir_acao_recomendacao(entrada, proba)
    dados_cliente = cliente.drop(columns=["churn_value"]).iloc[0].to_dict()
    return {"churn_proba": float(proba), "acoes": acoes, "dados_cliente": dados_cliente}