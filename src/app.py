import components
import detection_model
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio
from sklearn.linear_model import LogisticRegression
import streamlit as st
import styles
from time import sleep


# Configurações iniciais da página
st.set_page_config(page_title="Preditor - Câncer de Mama", layout="wide")
styles.load_styles()


# Carregamento do dataset
@st.cache_data
def get_data():
    return detection_model.load_data()

dataset = get_data()
X, y = detection_model.prepare_data(dataset)


# Treinamento do modelo (já validado anteriormente)
@st.cache_resource
def get_model():
    return detection_model.train_model(X, y)

model = get_model()


# Cabeçalho da página
components.show_title_card("🔬 Preditor de Câncer de Mama 🔬", "Modelo de Machine Learning para apoio à análise clínica")


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
st.sidebar.markdown('<div class="sidebar-header"> <span class="sidebar-title">Simulação Clínica</span> <span> Ajuste os parâmetros do exame citológico. </span> </div>', unsafe_allow_html=True)

user_input = []

for feature in feature_names:
    st.sidebar.markdown('<div class="sidebar-card">', unsafe_allow_html=True)
    
    value = st.sidebar.slider(
        feature_labels[feature],
        float(dataset[feature].min()),
        float(dataset[feature].max()),
        float(dataset[feature].mean()),
        help=f"Nome original: {feature}"
    )
    user_input.append(value)

input_array = np.array(user_input).reshape(1, -1)


# Efetuando previsão
prediction, prob = detection_model.predict(model, input_array)


# Carregamento
col1, col2, col3 = st.columns([1,2,1])

with col2:
    with st.spinner("Analisando dados..."):
        sleep(2)

# Exibição dos resultados
with st.container():
    components.show_section_title("📊 Resultado 📊")
    
    col1, col2 = st.columns(2)

    with col1:
        components.show_status_card(prediction)
    with col2:
        components.show_result_card("Probabilidade de Malignidade", prob)


# Gráfico de probabilidade
figure = px.bar(
    x=["Benigno", "Maligno"],
    y=[1 - prob, prob],
    labels={"x": "", "y": "Probabilidade"},
)

figure.update_traces(
    marker_color=["#2ecc71", "#e74c3c"],
    text=[f"{(1-prob)*100:.1f}%", f"{prob*100:.1f}%"],
    textposition="outside"
)

figure.update_layout(
    showlegend=False,
    yaxis=dict(range=[0,1]),
)

st.plotly_chart(figure, use_container_width=True)

# Gráfico de importância das variáveis
components.show_section_title("📊 Influência das Variáveis 📊")
coefficients = model.coef_[0]
abs_coeff = np.abs(coefficients)

figure2 = px.bar(
    x=coefficients,
    y=[feature_labels[f] for f in feature_names],
    orientation="h",
    color=abs_coeff,
    color_continuous_scale="Reds"
)

figure2.update_layout(
    coloraxis_showscale=False,
    xaxis_title="Impacto no modelo",
    yaxis_title=""
)
st.plotly_chart(figure2, use_container_width=True)


# Sobre o projeto
components.show_about_project()
