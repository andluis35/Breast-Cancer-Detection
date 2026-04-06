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
        <div class="result-card">
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


def show_about_project():
    st.markdown("""
        ###
            - Dataset: Wisconsin Breast Cancer (UCI)
            - Modelo: Regressão Logística
            - Objetivo: Classificação binária (Benigno vs Maligno)
                    
            Este projeto busca demonstrar como modelos de Machine Learning podem auxiliar na análise de dados médicos.
        """
    )
