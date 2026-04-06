import streamlit as st


def load_styles():
    st.markdown("""
        <style>
            .main {
                background-color: #FAEED1;
            }

            [data-testid="stSidebar"] {
                background: linear-gradient(180deg, #1e1e2f, #2c2c54);
            }

            [data-testid="stSidebar"] * {
                color: white;
            }
                
            [data-testid="stSidebarHeader"] {
                margin: 0;    
            }
                    
            [data-testid="stSidebar"] h1,
            [data-testid="stSidebar"] h2,
            [data-testid="stSidebar"] h3 {
                color: #ffffff;
                font-weight: bolder;
                margin-bottom: 16px;
            }
                
            .sidebar-card {
                background: rgba(255, 255, 255, 0.05);
                padding: 10px 12px;
                border-radius: 10px;
                margin-bottom: 12px;
                transition: 0.2s;
            }

            .sidebar-card:hover {
                background: rgba(255, 255, 255, 0.1);
            }
                
            .sidebar-header {
                background: rgba(255,255,255,0.08);
                padding: 12px;
                border-radius: 10px;
                margin-bottom: 15px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                text-align: center;
            }
                
            .sidebar-title {
                font-size: 24px;
                font-weight: 800;    
            }
        </style>
        """, unsafe_allow_html=True
    )