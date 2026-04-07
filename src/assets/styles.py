import streamlit as st


def load_styles():
    st.markdown(
        """
        <style>
            [data-testid="stAppViewContainer"] {
                background-color: #FFF6F6;
            }

            [data-testid="stSidebar"] {
                background: linear-gradient(180deg, #2C687B, #2C687B);
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

            div[data-testid="stPlotlyChart"] {
                background: transparent;
                padding: 0;
                margin: 0;
                box-shadow: none;
                border-radius: 16px;
                overflow: hidden;
            }

            h3 {
                margin-bottom: 24px;
            }
                
            .sidebar-card {
                background: rgba(255, 255, 255, 0.05);
                padding: 10px 12px;
                border-radius: 16px;
                margin-bottom: 12px;
                transition: 0.2s;
            }

            .sidebar-card:hover {
                background: rgba(255, 255, 255, 0.1);
            }
                
            .sidebar-header {
                background: rgba(255,255,255,0.08);
                padding: 12px;
                border-radius: 16px;
                margin-bottom: 60px;
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

            .sidebar {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                text-align: center;
            }

            .medical-cross {
                width: 100px;
                margin-bottom: 60px;
            }

            .title-card {
                background: linear-gradient(135deg, #2C687B, #2C687B);
                padding: 30px 20px;
                border-radius: 16px;
                border-left: 6px solid #DB1A1A;
                border-right: 6px solid #DB1A1A;
                text-align: center;
                color: white;
                box-shadow: 0 8px 20px rgba(0,0,0,0.15);
                margin-bottom: 25px;
            }
                
            .title-card h1 {
                margin: 0;
                font-size: 34px;
                font-weight: 700;
                letter-spacing: 0.5px;
            }
                
            .title-card p {
                margin-top: 8px;
                font-size: 14px;
                opacity: 0.9;
            }

            .result-card {
                background: white;
                padding: 18px;
                border-radius: 16px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.08);
                transition: 0.2s ease;
                height: 128px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                text-align: center;
                margin-bottom: 24px;
            }

            .result-card:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 18px rgba(0,0,0,0.12);
            }

            .result-title {
                font-size: 14px;
                color: #666;
                margin-bottom: 8px;
            }

            .result-value {
                font-size: 28px;
                font-weight: 700;
            }

            .status-card {
                background: white;
                padding: 18px;
                border-radius: 16px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.08);
                height: 128px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                text-align: center;
                transition: 0.2s ease;
            }

            .status-card:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 18px rgba(0,0,0,0.12);
            }

            .status-title {
                font-size: 14px;
                color: #666;
                margin-bottom: 8px;
            }

            .status-value {
                font-size: 24px;
                font-weight: 700;
            }

            .status-icon {
                font-size: 28px;
                margin-bottom: 6px;
            }

            .about-card {
                background: white;
                padding: 20px;
                border-radius: 16px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.08);
                margin-top: 64px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }

            .about-title {
                font-size: 18px;
                font-weight: 600;
                margin-bottom: 12px;
                color: black;
            }

            .about-list {
                font-size: 14px;
                color: #444;
                margin-bottom: 12px;
                display: flex;
                flex-direction: column;
                align-items: center;
            }

            .about-list b {
                color: #111;
            }

            .about-description {
                font-size: 14px;
                color: #666;
                line-height: 1.5;
                margin-bottom: 12px;
            }

            .about-credits {
                font-size: 14px;
                color: black;
                display: flex;
                flex-direction: column;
                align-items: center;
            }

            .credits-images img {
                margin: 12px;
                transition: 0.2s ease;
            }

            .credits-images img:hover {
                transform: translateY(-2px);
            }

            .section-card {
                background: linear-gradient(135deg, #2C687B, #2C687B);
                color: white;
                padding: 14px 20px;
                border-radius: 16px;
                font-size: 20px;
                font-weight: 600;
                margin-top: 32px;
                text-align: center;
                box-shadow: 0 4px 12px rgba(0,0,0,0.12);
            }
        </style>
        """, 
        unsafe_allow_html=True
    )