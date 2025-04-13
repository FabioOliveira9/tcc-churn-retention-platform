import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="Dashboard de Clientes")

# -------------------------
# Cabeçalho e frase inspiradora
# -------------------------
st.markdown("## 🧠 Plataforma para Predição e Prevenção de Churn")
st.markdown("<p style='font-style: italic; text-align: center;'>“Use dados e algoritmos para adaptar produtos e serviços aos desejos e necessidades do cliente.”</p>", unsafe_allow_html=True)
st.markdown("---")

# -------------------------
# Carga dos dados
# -------------------------
@st.cache_data
def carregar_dados():
    df = pd.read_csv("final_model_12.csv")
    return df

df = carregar_dados()

# -------------------------
# KPIs principais
# -------------------------
total_clientes = df.shape[0]
qtd_churn = df["churn_value"].sum()
perc_churn = (qtd_churn / total_clientes) * 100
media_mensal = df["monthly_charges"].mean()
total_receita = df["total_charges"].sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("📊 Total de Clientes", f"{total_clientes}")
col2.metric("❌ Clientes com Churn", f"{qtd_churn} ({perc_churn:.2f}%)")
col3.metric("💰 Receita Total", f"R$ {total_receita:,.2f}")
col4.metric("💵 Ticket Médio Mensal", f"R$ {media_mensal:,.2f}")

st.markdown("---")

# -------------------------
# Gráfico 1: Pizza de Churn
# -------------------------
st.markdown("### 🎯 Distribuição de Churn")
fig1, ax1 = plt.subplots()
df["churn_value"].value_counts().plot.pie(
    autopct="%1.1f%%",
    startangle=90,
    colors=["#66c2a5", "#fc8d62"],
    labels=["Não Churn", "Churn"],
    ax=ax1,
    textprops={"fontsize": 12}
)
ax1.set_ylabel("")
st.pyplot(fig1)

# -------------------------
# Gráfico 2: Churn por Tipo de Contrato
# -------------------------
st.markdown("### 📂 Churn por Tipo de Contrato")
fig2, ax2 = plt.subplots(figsize=(6,4))
df.groupby("contract")["churn_value"].mean().sort_values().plot(kind="bar", color="#fc8d62", ax=ax2)
ax2.set_ylabel("Taxa de Churn (%)")
ax2.set_xlabel("Tipo de Contrato")
ax2.set_title("Churn Médio por Contrato")
st.pyplot(fig2)

# -------------------------
# Gráfico 3: Receita Mensal por Cliente (Boxplot)
# -------------------------
st.markdown("### 💸 Distribuição de Receita Mensal")
fig3, ax3 = plt.subplots(figsize=(6,4))
df.boxplot(column="monthly_charges", by="churn_value", ax=ax3, grid=False)
ax3.set_title("Monthly Charges por Churn")
ax3.set_xlabel("Churn")
ax3.set_ylabel("Valor (R$)")
plt.suptitle("")
st.pyplot(fig3)

# -------------------------
# Gráfico 4: Dispersão Tenure x Monthly Charges
# -------------------------
st.markdown("### 🔍 Perfil de Clientes por Permanência e Receita")
fig4, ax4 = plt.subplots(figsize=(7,4))
cores = df["churn_value"].map({0: "#66c2a5", 1: "#fc8d62"})
ax4.scatter(df["tenure_months"], df["monthly_charges"], alpha=0.5, c=cores)
ax4.set_xlabel("Meses de Permanência")
ax4.set_ylabel("Monthly Charges (R$)")
ax4.set_title("Clientes: Permanência vs Receita Mensal")
st.pyplot(fig4)


st.markdown("---")
st.markdown("💡 Este painel é apenas uma parte da plataforma de previsão e prevenção de churn. Para consultar a probabilidade individual e recomendações de retenção, acesse a aba **Predição por Cliente** no menu lateral.")