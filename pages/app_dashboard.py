
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =======================
# CONFIGURAÇÃO DA PÁGINA
# =======================
st.set_page_config(page_title="Dashboard de Churn", layout="wide")

# ============
# CARREGAR DADOS
# ============
@st.cache_data
def carregar_dados():
    df = pd.read_csv("final_model_12.csv")
    return df

df = carregar_dados()

# ============
# LAYOUT - TOPO
# ============
st.markdown("### Plataforma para Predição e Prevenção de Churn")
st.markdown("*Use dados e algoritmos para adaptar produtos e serviços aos desejos e necessidades do cliente.*")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de Clientes", df.shape[0])
col2.metric("Churn (%)", f"{df['churn'].mean()*100:.2f}%")
col3.metric("Receita Total", f"${df['total_charges'].sum():,.0f}")
col4.metric("Receita Média", f"${df['monthly_charges'].mean():.2f}/mês")

st.markdown("---")

# ============
# GRÁFICO 1: Proporção de Churn
# ============
st.subheader("Proporção de Clientes que Churnaram")
fig1, ax1 = plt.subplots()
df['churn'].value_counts(normalize=True).plot(kind='pie', autopct='%1.1f%%', labels=['Não', 'Sim'], ax=ax1, colors=['#66c2a5', '#fc8d62'])
ax1.set_ylabel('')
st.pyplot(fig1)

# ============
# GRÁFICO 2: Churn por Tipo de Contrato
# ============
st.subheader("Churn por Tipo de Contrato")
fig2, ax2 = plt.subplots()
pd.crosstab(df['contract'], df['churn'], normalize='index').plot(kind='bar', stacked=True, ax=ax2, color=['#66c2a5', '#fc8d62'])
ax2.set_ylabel("Proporção")
ax2.set_xlabel("Tipo de Contrato")
ax2.legend(["Não Churn", "Churn"])
st.pyplot(fig2)

# ============
# GRÁFICO 3: Churn por Método de Pagamento
# ============
st.subheader("Churn por Método de Pagamento")
fig3, ax3 = plt.subplots()
pd.crosstab(df['payment_method'], df['churn'], normalize='index').plot(kind='bar', stacked=True, ax=ax3, color=['#66c2a5', '#fc8d62'])
ax3.set_ylabel("Proporção")
ax3.set_xlabel("Método de Pagamento")
ax3.legend(["Não Churn", "Churn"])
st.pyplot(fig3)

# ============
# GRÁFICO 4: Churn por Serviço de Internet
# ============
st.subheader("Churn por Tipo de Internet")
fig4, ax4 = plt.subplots()
pd.crosstab(df['internet_service'], df['churn'], normalize='index').plot(kind='bar', stacked=True, ax=ax4, color=['#66c2a5', '#fc8d62'])
ax4.set_ylabel("Proporção")
ax4.set_xlabel("Tipo de Internet")
ax4.legend(["Não Churn", "Churn"])
st.pyplot(fig4)
