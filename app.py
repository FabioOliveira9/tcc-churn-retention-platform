
import streamlit as st
from app_home import show_home
from app_dashboard import show_dashboard
from app_predicao_por_id import show_predicao_por_id
from app_predicao_manual import show_predicao_manual

st.set_page_config(page_title="Plataforma de Retenção", page_icon="📊", layout="wide")

# Sidebar
st.sidebar.image("foto_fabio.jpeg", width=160)
st.sidebar.markdown("<h3 style='text-align: center; margin-top: 10px;'>Fabio do Nascimento Oliveira</h3>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center;'>Engenharia Eletrônica e de Computação</p>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center;'>Escola Politécnica - UFRJ</p>", unsafe_allow_html=True)
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

pagina = st.sidebar.selectbox(
    "Escolha uma página:",
    ["🏠 Página Inicial", "🔎 Predição por ID", "📝 Previsão Manual", "📊 Dashboard"]
)

if pagina == "🏠 Página Inicial":
    show_home()
elif pagina == "🔎 Predição por ID":
    show_predicao_por_id()
elif pagina == "📝 Previsão Manual":
    show_predicao_manual()
elif pagina == "📊 Dashboard":
    show_dashboard()