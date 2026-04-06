import streamlit as st


def show_result_card(title, value, color):
    st.markdown(f"""
        <div style="
            background-color: #f0f2f6;
            color: #000000;
            height: 56px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        ">
            <h5>{title}
                <div style="color:{color};">{value*100:.2f}%</div>
                </div>
            </h5>
        </div>
        """, unsafe_allow_html=True)
    

def show_centered_title(text):
    st.markdown(
        f"<h1 style='text-align:center;'>{text}</h1>",
        unsafe_allow_html=True
    )
    st.markdown("***")


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
