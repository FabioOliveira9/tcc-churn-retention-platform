import streamlit as st
from PIL import Image
import base64

# ============================
# Configuração da Página
# ============================
st.set_page_config(page_title="Plataforma de Churn", layout="wide")

# ============================
# Estilo customizado
# ============================
st.markdown("""
    <style>
        .centered-image img {
            border-radius: 50%;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 170px;
        }
        .title {
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: gray;
            margin-bottom: 20px;
        }
        .quote {
            text-align: center;
            font-style: italic;
            color: #555;
            margin-bottom: 30px;
        }
        .nav-boxes {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 30px;
        }
        .nav-box {
            background-color: #f0f2f6;
            padding: 25px;
            border-radius: 12px;
            width: 250px;
            text-align: center;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
            transition: all 0.3s ease-in-out;
        }
        .nav-box:hover {
            background-color: #e6eefc;
            cursor: pointer;
            transform: scale(1.02);
        }
        .nav-box a {
            text-decoration: none;
            color: black;
            font-weight: 500;
        }
    </style>
""", unsafe_allow_html=True)

# ============================
# Imagem e Informacoes
# ============================
st.markdown('<div class="centered-image"> <img src="foto_fabio.jpeg"> </div>', unsafe_allow_html=True)

st.markdown("""
<div class="title">Fabio do Nascimento Oliveira</div>
<div class="subtitle">Engenharia Eletrônica e de Computação – Universidade Federal do Rio de Janeiro</div>
<div class="quote">"Use dados e algoritmos para adaptar produtos e serviços aos desejos e necessidades do cliente."</div>
<div class="subtitle" style="font-size:16px; color:#333;">Trabalho de Conclusão de Curso: <b>Desenvolvimento de uma Plataforma Web para Previsão de Churn e Estratégias de Retenção com Machine Learning, FastAPI e Interface Interativa em Streamlit</b></div>
""", unsafe_allow_html=True)

# ============================
# Navegacao Visual
# ============================
st.markdown("""
<div class="nav-boxes">
    <div class="nav-box"><a href="app_dashboard" target="_self">📊 Dashboard de Clientes</a></div>
    <div class="nav-box"><a href="app_predicao_por_id" target="_self">🔎 Predição por ID</a></div>
    <div class="nav-box"><a href="app_predicao_manual" target="_self">✍️ Previsão Manual</a></div>
</div>
""", unsafe_allow_html=True)