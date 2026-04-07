from components import components
from models import detection_model
import numpy as np
import plotly.express as px
import streamlit as st
from assets import styles


# --------------------------
# Paleta de cores utilizadas
# --------------------------
PRIMARY_RED = "#DB1A1A"
LIGHT_BG = "#FFF6F6"
ACCENT_GREEN = "#8CC7C4"
ACCENT_BLUE = "#2C687B"
DARK_GRAY = "#2C2D2E"


# --------------------------
# Setup inicial
# --------------------------
def setup_app():
    st.set_page_config(page_title="Preditor - Câncer de Mama", layout="wide")
    styles.load_styles()


# --------------------------
# Dados e Modelo
# --------------------------
@st.cache_data
def load_data():
    return detection_model.load_data()


@st.cache_resource
def load_model(X, y):
    return detection_model.train_model(X, y)


# --------------------------
# Sidebar
# --------------------------
def build_sidebar(dataset, feature_names, feature_labels):
    components.show_sidebar()

    user_input = []

    for feature in feature_names:
        components.show_sidebar_card()
        
        value = st.sidebar.slider(
            feature_labels[feature],
            float(dataset[feature].min()),
            float(dataset[feature].max()),
            float(dataset[feature].mean()),
            help=f"Nome original: {feature}"
        )
        user_input.append(value)

    return np.array(user_input).reshape(1, -1)


# --------------------------
# Predição
# --------------------------
def make_prediction(model, input_array):
    return detection_model.predict(model, input_array)


# --------------------------
# Resultados
# --------------------------
def show_results(prediction, prob):
    with st.container():
        components.show_section_title("📊 Resultado")
        
        col1, col2 = st.columns(2)

        with col1:
            components.show_status_card(prediction)
        with col2:
            components.show_result_card("Probabilidade de Malignidade", prob)


# --------------------------
# Gráfico de Probabilidade
# --------------------------
def plot_probability_chart(prob):
    figure = px.bar(
        x=["Benigno", "Maligno"],
        y=[1 - prob, prob],
        labels={"x": "", "y": "Probabilidade"},
    )

    figure.update_traces(
        marker_color=[ACCENT_GREEN, PRIMARY_RED],
        text=[f"{(1-prob)*100:.1f}%", f"{prob*100:.1f}%"],
        textposition="outside"
    )

    figure.update_layout(
        plot_bgcolor=LIGHT_BG,
        paper_bgcolor=LIGHT_BG,
        font=dict(color=ACCENT_BLUE),
        margin=dict(l=20, r=20, t=40, b=20),
        
        xaxis=dict(tickfont=dict(color=ACCENT_BLUE)),
        yaxis=dict(tickfont=dict(color=ACCENT_BLUE)),
        yaxis_title_font=dict(color=ACCENT_BLUE),
    )
    st.plotly_chart(figure, use_container_width=True)


# --------------------------
# Gráfico de Importância
# --------------------------
def plot_relevance_chart(model, feature_names, feature_labels):
    components.show_section_title("📊 Influência das Variáveis")

    coefficients = model.coef_[0]
    abs_coeff = np.abs(coefficients)

    figure2 = px.bar(
        x=coefficients,
        y=[feature_labels[f] for f in feature_names],
        orientation="h",
        color=abs_coeff,
        color_continuous_scale=[
            (0.0, ACCENT_GREEN),
            (0.5, ACCENT_BLUE),
            (1.0, PRIMARY_RED),
        ]
    )

    figure2.update_layout(
        coloraxis_showscale=False,
        xaxis_title="Impacto no modelo",
        yaxis_title="",
        plot_bgcolor=LIGHT_BG,
        paper_bgcolor=LIGHT_BG,
        font=dict(color=DARK_GRAY),
        
        xaxis=dict(tickfont=dict(color=ACCENT_BLUE)),
        yaxis=dict(tickfont=dict(color=ACCENT_BLUE)),
        xaxis_title_font=dict(color=ACCENT_BLUE),
    )
    st.plotly_chart(figure2, use_container_width=True)


# --------------------------
# MAIN
# --------------------------
def main():
    setup_app()

    dataset = load_data()
    X, y = detection_model.prepare_data(dataset)
    model = load_model(X, y)

    components.show_title_card(
        "Sistema de Predição de Câncer de Mama",
        "Modelo de Machine Learning para apoio à análise clínica"
    )

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

    input_array = build_sidebar(dataset, feature_names, feature_labels)
    
    prediction, prob = make_prediction(model, input_array)

    show_results(prediction, prob)
    plot_probability_chart(prob)
    plot_relevance_chart(model, feature_names, feature_labels)

    components.show_about_project()


# --------------------------
# ENTRYPOINT
# --------------------------
if __name__ == "__main__":
    main()
