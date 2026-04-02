import streamlit as st


def load_styles():
    st.markdown("""
        <style>
        .main {
            background-color: #f5f7fa;
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1e1e2f, #2c2c54);
        }

        [data-testid="stSidebar"] * {
            color: white;
        }
        </style>
        """, unsafe_allow_html=True
    )