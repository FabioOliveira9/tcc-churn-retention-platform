import streamlit as st
import requests
import pandas as pd

def run_predicao_id():
    st.title("🔍 Predição por ID do Cliente")
    st.write("Insira o ID do cliente para verificar a probabilidade de churn.")

    customer_id = st.text_input("ID do Cliente")

    if st.button("🔎 Prever"):
        if not customer_id:
            st.warning("Por favor, insira um ID de cliente.")
            return

        url = f"http://localhost:8000/predict_id/{customer_id}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                st.success(f"Probabilidade de Churn: {data['churn_proba']*100:.2f}%")
                st.markdown("### Ação Recomendada:")
                for acao in data['acoes']:
                    st.write(f"- {acao}")
                st.markdown("---")
                st.markdown("### Dados do Cliente:")
                st.dataframe(pd.DataFrame([data["dados_cliente"]]))
            else:
                st.error("Cliente não encontrado ou erro na API.")
        except Exception as e:
            st.error(f"Erro na requisição: {e}")