import streamlit as st
import requests

st.set_page_config(page_title="Predição Manual", layout="wide")

st.title("🔍 Predição de Churn - Preenchimento Manual")

st.write("Preencha os campos abaixo para obter a probabilidade de churn e uma recomendação estratégica:")

with st.form("formulario_manual"):
    col1, col2 = st.columns(2)

    with col1:
        tenure = st.slider("Meses de Contrato (tenure_months)", 1, 72, 12)
        monthly_charges = st.number_input("Cobrança Mensal (monthly_charges)", min_value=0.0, value=70.0)
        paperless_billing_no = st.selectbox("Possui Fatura Impressa? (paperless_billing_no)", ["Sim", "Não"])
        partner_no = st.selectbox("Possui Cônjuge? (partner_no)", ["Sim", "Não"])
        senior_citizen_no = st.selectbox("É Idoso(a)? (senior_citizen_no)", ["Sim", "Não"])
        streaming_movies_yes = st.selectbox("Assina Streaming de Filmes? (streaming_movies_yes)", ["Sim", "Não"])

    with col2:
        total_charges = st.number_input("Cobrança Total (total_charges)", min_value=0.0, value=1400.0)
        dependents_no = st.selectbox("Possui Dependentes? (dependents_no)", ["Sim", "Não"])
        multiple_lines_no = st.selectbox("Possui Múltiplas Linhas? (multiple_lines_no)", ["Sim", "Não"])
        online_security_no = st.selectbox("Possui Segurança Online? (online_security_no)", ["Sim", "Não"])
        online_backup_no = st.selectbox("Possui Backup Online? (online_backup_no)", ["Sim", "Não"])
        tech_support_no = st.selectbox("Possui Suporte Técnico? (tech_support_no)", ["Sim", "Não"])

    st.markdown("### Tipo de Contrato")
    contrato = st.radio("Contrato", ["Mensal", "Anual", "Bianual"], horizontal=True)
    contract_month_to_month = 1 if contrato == "Mensal" else 0
    contract_one_year = 1 if contrato == "Anual" else 0

    st.markdown("### Método de Pagamento")
    metodo_pagamento = st.radio("Método", ["Electronic Check", "Outro"], horizontal=True)
    payment_method_electronic_check = 1 if metodo_pagamento == "Electronic Check" else 0

    submit = st.form_submit_button("🔍 Realizar Predição")

if submit:
    payload = {
        "tenure_months": tenure,
        "monthly_charges": monthly_charges,
        "total_charges": total_charges,
        "senior_citizen_no": 1 if senior_citizen_no == "Não" else 0,
        "partner_no": 1 if partner_no == "Não" else 0,
        "dependents_no": 1 if dependents_no == "Não" else 0,
        "multiple_lines_no": 1 if multiple_lines_no == "Não" else 0,
        "online_security_no": 1 if online_security_no == "Não" else 0,
        "online_backup_no": 1 if online_backup_no == "Não" else 0,
        "tech_support_no": 1 if tech_support_no == "Não" else 0,
        "streaming_movies_yes": 1 if streaming_movies_yes == "Sim" else 0,
        "contract_month_to_month": contract_month_to_month,
        "contract_one_year": contract_one_year,
        "paperless_billing_no": 1 if paperless_billing_no == "Sim" else 0,
        "payment_method_electronic_check": payment_method_electronic_check,
    }

    with st.spinner("Enviando dados para a API..."):
        response = requests.post("https://tcc-churn-retention-platform.streamlit.app/predict", json=payload)

    if response.status_code == 200:
        resultado = response.json()
        st.success(f"🧠 Probabilidade de Churn: **{round(resultado['churn_proba'] * 100, 2)}%**")
        st.info(f"📌 Recomendação: **{resultado['acao_recomendada']}**")
    else:
        st.error("Erro na requisição. Verifique a API ou os dados enviados.")