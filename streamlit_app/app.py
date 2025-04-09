# app.py
import streamlit as st
from PIL import Image
from churn_predicao_id import run as run_predicao_id

# Título e imagem lateral
st.set_page_config(page_title="Plataforma de Retenção", layout="wide")

with st.sidebar:
    st.image("foto_fabio.jpeg", width=200)
    st.markdown("#### Fabio do Nascimento Oliveira")
    st.markdown("Engenharia Eletrônica e de Computação - UFRJ")
    st.markdown("**Trabalho de Conclusão de Curso**")
    st.markdown("**Plataforma para Predição e Prevenção de Churn utilizando Machine Learning, WebAPIs e Estratégias de Growth**")
    st.markdown("Orientador: Heraldo Luis Silveira Almeida")
    pagina = st.selectbox("🔎 Navegue pelas seções:", ["Página Inicial", "Predição por CustomerID"])

# Página Central
if pagina == "Página Inicial":
    st.markdown("## 📊 Plataforma de Retenção de Clientes")
    st.write("""
    Esta plataforma foi desenvolvida como parte do Trabalho de Conclusão de Curso de Engenharia Eletrônica e de Computação na UFRJ. 
    Seu objetivo é prever a probabilidade de churn (cancelamento) de clientes e propor estratégias de retenção baseadas em dados reais e explicabilidade.
    
    ### Funcionalidades:
    - Predição individual por CustomerID
    - Estratégias de retenção personalizadas
    - Visualização da importância dos fatores (SHAP)
    """)
    
    st.markdown("### ⚙️ Modelagem Utilizada")
    st.write("""
    - Algoritmo base: **XGBoost**
    - Técnica de balanceamento: **SMOTE**
    - Seleção de variáveis: **RFE com 15 features**
    - Otimização de hiperparâmetros: **Optuna (F1-score)**
    """)

elif pagina == "Predição por CustomerID":
    run_predicao_id()