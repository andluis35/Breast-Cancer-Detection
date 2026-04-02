import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LogisticRegression
import streamlit as st

# Configurações iniciais da página
st.set_page_config(
    page_title="Preditor - Câncer de Mama",
    layout="wide"
)

# Carregamento do dataset
@st.cache_data
def load_data():
    return pd.read_csv("breast_cancer.csv")

dataset = load_data()
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# Treinamento do modelo (já validado anteriormente)
@st.cache_resource
def train_model():
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    return model

model = train_model()

# Cabeçalho da página
st.title("🔬 Preditor de Câncer de Mama 🔬")
st.markdown("Modelo de Machine Learning utilizando Regressão Logística para classificação de tumores.")

# Tradução das features
feature_labels = {
    "Clump Thickness": "Espessura do aglomerado celular",
    "Uniformity of Cell Size": "Uniformidade do tamanho das células",
    "Uniformity of Cell Shape": "Uniformidade do formato das células",
    "Marginal Adhesion": "Aderência marginal",
    "Single Epithelial Cell Size": "Tamanho das células epiteliais isoladas",
    "Bare Nuclei": "Núcleos desnudos",
    "Bland Chromatin": "Cromatina homogênea",
    "Normal Nucleoli": "Nucléolos normais",
    "Mitoses": "Taxa de mitoses"
}
feature_names = dataset.columns[1:-1]

# Menu lateral com as entradas do usuário
st.sidebar.header("🧪 Parâmetros do Exame 🧪")
user_input = []

for feature in feature_names:
    value = st.sidebar.slider(
        feature_labels[feature],
        float(dataset[feature].min()),
        float(dataset[feature].max()),
        float(dataset[feature].mean()),
        help=f"Nome original: {feature}"
    )
    user_input.append(value)

input_array = np.array(user_input).reshape(1, -1)

# Botão de predição
if st.sidebar.button("🔍 Prever"):
    prediction = model.predict(input_array)[0]
    prob = model.predict_proba(input_array)[0][1]

    # Resultado
    col1, col2 = st.columns(2)

    with col1:
        if prediction == 2:
            st.success("🟢 Tumor Benigno")
        if prediction == 4:
            st.error("🔴 Tumor Maligno")
    
    with col2:
        st.metric("Probabilidade de malignidade", f"{prob:.2f}")

    # Gráfico de probabilidade
    figure = px.bar(
        x=["Benigno", "Maligno"],
        y=[1 - prob, prob],
        labels={"x": "Classe", "y": "Probabilidade"},
    )
    st.plotly_chart(figure, use_container_width=True)

    # Visualização da importância das variáveis
    st.subheader("📊 Influência das Variáveis 📊")
    coefficients = model.coef_[0]

    figure2 = px.bar(
        x=coefficients,
        y=[feature_labels[f] for f in feature_names],
        orientation="h",
        labels={"x": "Impacto no modelo", "y": "Variável"},
    )
    st.plotly_chart(figure2, use_container_width=True)


# Sobre o projeto
st.markdown("""
---
### 🧠 Sobre o projeto 🧠
    - Dataset: Wisconsin Breast Cancer (UCI)
    - Modelo: Regressão Logística
    - Objetivo: Classificação binária (Benigno vs Maligno)
            
    Este projeto busca demonstrar como modelos de Machine Learning podem auxiliar na análise de dados médicos.
""")