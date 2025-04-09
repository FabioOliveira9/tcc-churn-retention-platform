import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Predição de Churn por ID", page_icon="🔍")

st.title("🔍 Predição de Churn por CustomerID")

@st.cache_data

def carregar_base():
    df = pd.read_csv("df_churn_model_ready.csv")  # Arquivo com customerID e as 15 features
    df.columns = df.columns.str.lower().str.replace(" ", "_").str.replace("-", "_")
    return df
   

# Lista de features que o modelo espera
features = [
    'tenure_months', 'monthly_charges', 'total_charges',
    'senior_citizen_no', 'partner_no', 'dependents_no',
    'multiple_lines_no', 'online_security_no', 'online_backup_no',
    'tech_support_no', 'streaming_movies_yes',
    'contract_month_to_month', 'contract_one_year',
    'paperless_billing_no', 'payment_method_electronic_check'
]

# 1. Carrega base
cliente = carregar_base()

# 2. Selectbox com os IDs disponíveis
id_cliente = st.selectbox("Selecione um CustomerID:", cliente["customerid"].unique())

# 3. Filtra o cliente
x_cliente = cliente[cliente["customerid"] == id_cliente][features]

# 4. Chamada à API
if st.button("Realizar Predição"):
    dados = x_cliente.to_dict(orient="records")[0]
    try:
        resposta = requests.post("http://127.0.0.1:8000/predict", json=dados)
        if resposta.status_code == 200:
            resultado = resposta.json()
            st.success(f"🔮 Probabilidade de Churn: **{resultado['probabilidade']*100:.2f}%**")
            st.info(f"📌 Ação recomendada: **{resultado['acao']}**")
        else:
            st.error("Erro na requisição à API.")
    except Exception as e:
        st.error(f"Erro ao conectar à API: {e}")
