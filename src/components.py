import streamlit as st


def show_result_card(title, value):
    percentage = value * 100

    #Definição de cor baseada no risco
    if percentage < 40:
        color = "#2ecc71"
    elif percentage < 50:
        color = "#f1c40f"
    else:
        color = "#e74c3c"

    st.markdown(
        f"""
        <div class="result-card" style="border-right: 6px solid {color};">
            <div class="result-title">{title}</div>
            <div class="result-value" style="color:{color};">{percentage:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)
    

def show_title_card(title, subtitle=None):
    st.markdown(
        f"""
        <div class="title-card">
            <h1>{title}</h1>
            {f"<p>{subtitle}</p>" if subtitle else ""}
        </div>
        """, 
        unsafe_allow_html=True
    )


def show_section_title(text):
    st.markdown(
        f"<h3 style='text-align: center;'>{text}</h3>",
        unsafe_allow_html=True
    )


def show_status_card(prediction):
    if prediction == 2:
        label = "Tumor Benigno"
        color = "#2ecc71"
        icon = "🟢"

    if prediction == 4:
        label = "Tumor Maligno"
        color = "#e74c3c"
        icon = "🔴"

    st.markdown(
        f"""
        <div class="status-card" style="border-left: 6px solid {color};">
            <div class="status-icon">{icon}</div>
            <div class="status-value" style="color:{color};">{label}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def show_about_project():
    st.markdown(
        """
        <div class="about-card">
            <div class="about-title">🧠 Sobre o Projeto 🧠</div>
            <div class="about-list">
                <div><b>Dataset:</b> Wisconsin Breast Cancer (UCI)</div>
                <div><b>Modelo:</b> Regressão Logística</div>
                <div><b>Objetivo:</b> Classificação binária (Benigno vs Maligno)</div>
            </div>
            <div class="about-description">
                Este projeto demonstra como modelos de Machine Learning podem ser aplicados
                na análise de dados médicos, auxiliando na identificação de padrões e no apoio
                à tomada de decisão clínica.
            </div>
            <div class="about-credits">
                <div><b>Feito por:</b> Anderson Luis</div>
                <div class="credits-images">
                    <a href="https://github.com/andluis35" target="_blank">
                        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="30">
                    </a>
                    <a href="https://linkedin.com/in/anderson-luis-663970325" target="_blank">
                        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="30">
                    </a>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )