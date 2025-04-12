import streamlit as st
from PIL import Image

# Configurações da página
st.set_page_config(
    page_title="Plataforma de Retenção - Página Inicial",
    page_icon="📊",
    layout="wide"
)

# Sidebar (pode deixar vazia ou usar pra navegação)
with st.sidebar:
    st.image("foto_fabio.jpeg", width=160)
    st.markdown("<h3 style='text-align: center; margin-top: 10px;'>Fabio do Nascimento Oliveira</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Engenharia Eletrônica e de Computação</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Escola Politécnica - UFRJ</p>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

# Conteúdo central
st.markdown("<h1 style='text-align: center;'>Plataforma para Predição e Prevenção de Churn</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Utilizando Machine Learning, WebAPIs e Estratégias de Growth</h4>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px; margin-top: 30px;'>Use dados e algoritmos para adaptar produtos e serviços aos desejos e necessidades do cliente</p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Caixas de navegação
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div style="border-radius: 15px; padding: 30px; background-color: #f0f2f6; text-align: center; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05);">
            <h2>📊</h2>
            <h4>Dashboard de Clientes</h4>
            <p style='color: gray;'>Métricas, churn, receita e oportunidades.</p>
            <a href="?page=Dashboard" style="text-decoration: none;">
                <button style="margin-top: 10px; padding: 8px 16px; border-radius: 8px; border: none; background-color: #3ba6a2; color: white;">Acessar</button>
            </a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="border-radius: 15px; padding: 30px; background-color: #f0f2f6; text-align: center; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05);">
            <h2>🔎</h2>
            <h4>Predição por ID</h4>
            <p style='color: gray;'>Busque um cliente específico pela ID.</p>
            <a href="?page=Predição por ID" style="text-decoration: none;">
                <button style="margin-top: 10px; padding: 8px 16px; border-radius: 8px; border: none; background-color: #3ba6a2; color: white;">Acessar</button>
            </a>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div style="border-radius: 15px; padding: 30px; background-color: #f0f2f6; text-align: center; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05);">
            <h2>📝</h2>
            <h4>Previsão Manual</h4>
            <p style='color: gray;'>Informe os dados de um cliente e gere a predição.</p>
            <a href="?page=Previsão Manual" style="text-decoration: none;">
                <button style="margin-top: 10px; padding: 8px 16px; border-radius: 8px; border: none; background-color: #3ba6a2; color: white;">Acessar</button>
            </a>
        </div>
    """, unsafe_allow_html=True)