# 🧬 Breast Cancer Detection App
### Machine Learning Web Application

* **Breast Cancer Detection App** é uma aplicação web desenvolvida para prever a probabilidade de câncer de mama com base em características clínicas, utilizando um modelo de Machine Learning (Regressão Logística).

* **Breast Cancer Detection App** is a web application designed to predict the probability of breast cancer based on clinical features, using a Machine Learning model (Logistic Regression).

* O objetivo do projeto é demonstrar a aplicação prática de Ciência de Dados e Engenharia de Software, integrando modelagem preditiva com uma interface interativa construída em Streamlit.

* The goal of this project is to demonstrate the practical application of Data Science and Software Engineering, integrating predictive modeling with an interactive interface built using Streamlit.

---

## Tecnologias Utilizadas / Tools & Technologies

### Data Science & Machine Learning
- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn (Logistic Regression)**

### Scikit-learn (Logistic Regression)
- **Streamlit**
- **Plotly (visualização de dados)**

### Outros / Others
- **Git & GitHub**
- **Streamlit Cloud (deploy)**

---

## 📂 Estrutura do Projeto / Project Structure

```bash
breast-cancer-detection/
├─ data/                          # Dataset utilizado no modelo / Dataset used
│  └─ breast-cancer.csv
│
├─ src/
│  ├─ assets/
│  │   └─ styles.py              # Estilos visuais do app / App styling
│  │
│  ├─ components/
│  │   └─ components.py          # Componentes reutilizáveis da interface / Reusable UI components
│  │
│  ├─ models/
│  │   └─ detection_model.py     # Lógica de Machine Learning (treino e predição) / ML logic (training & prediction)
│  │
│  └─ app.py                     # Aplicação principal em Streamlit / Main Streamlit app
│
├─ requirements.txt              # Dependências do projeto / Project dependencies
├─ .gitignore                    # Arquivos ignorados pelo Git / Ignored files
└─ README.md                     # Documentação do projeto / Project documentation
```

## ⚙️ Decisões de Design / Design Decisions

* **Regressão Logística / Logistic Regression:** Escolhida por ser um modelo simples, interpretável e eficiente para problemas de classificação binária. Chosen for being simple, interpretable, and effective for binary classification problems.

* **Streamlit:** Permite criar rapidamente interfaces interativas para modelos de ML sem necessidade de frontend complexo. Allows rapid development of interactive ML interfaces without complex frontend frameworks.

* **Separação de responsabilidades / Separation of concerns:** O código foi dividido entre interface (app.py) e lógica de modelo (detection_model.py) para melhor organização e manutenção. The code is separated between UI (app.py) and model logic (detection_model.py) for better organization and maintainability.

* **Uso de caching / Caching strategy:** Uso de st.cache_data para evitar recarregamento desnecessário do dataset e melhorar performance. Use of st.cache_data to avoid unnecessary data reload and improve performance.

## 🌟 Funcionalidades Principais & Futuras / Key Features & Future Work

### 1. Funcionalidades principais / Key Features

* **Predição em tempo real / Real-time prediction:** O usuário insere dados clínicos e recebe a classificação e probabilidade do modelo. Users input clinical data and receive classification and probability predictions.

* **Probabilidade do diagnóstico / Prediction probability:** Exibição da probabilidade associada à predição (ex: risco de malignidade). Displays prediction confidence (e.g., malignancy probability).

* **Visualização de dados / Data visualization:** Gráficos interativos para melhor interpretação dos resultados. Interactive charts for better understanding of results.

* **Interface amigável / User-friendly interface:** Layout simples, intuitivo e responsivo com Streamlit. Clean and intuitive interface using Streamlit.

### 2. Funcionalidades Futuras / Future Features

* **Persistência de dados / Data persistence:** Salvar histórico de predições. Store prediction history.

* **Modelos mais avançados / Advanced models:** Testar Random Forest, XGBoost ou redes neurais. Experiment with more advanced ML models.

* **Deploy com API / API integration:** Transformar o modelo em uma API REST. Expose the model through a REST API.

## 🚀 Como rodar o projeto / How to run the project

```bash
# Clonar repositório / Clone repository
git clone https://github.com/andluis35/breast-cancer-detection.git
cd breast-cancer-detection

# Criar ambiente virtual (opcional) / Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instalar dependências / Install dependencies
pip install -r requirements.txt

# Rodar aplicação / Run app
streamlit run src/app.py
```

* O servidor estará disponível em: http://localhost:8501
* Access in the browser: http://localhost:8501

### 2. Rodando com Streamlit Cloud / Running with Streamlit Cloud

* Este modo usa a hospedagem do Streamlit
* This mode uses Streamlit hosting

* Acesso disponível em: https://andluis35-breast-cancer-detection-srcapp-la9k15.streamlit.app/
* Access available at: https://andluis35-breast-cancer-detection-srcapp-la9k15.streamlit.app/