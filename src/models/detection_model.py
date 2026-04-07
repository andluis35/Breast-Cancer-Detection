import pandas as pd
from sklearn.linear_model import LogisticRegression


def load_data():
    '''
        Carrega o dataset de câncer de mama a partir de um arquivo CSV.
    '''

    return pd.read_csv("./data/breast_cancer.csv")


def prepare_data(dataset):
    '''
        Separa o dataset em variáveis independentes (X) e variável alvo (y),
        removendo a coluna de identificação e mantendo apenas as features relevantes.
    '''

    X = dataset.iloc[:, 1:-1].values
    y = dataset.iloc[:, -1].values
    return X, y
    

def train_model(X, y):
    '''
        Treina um modelo de Regressão Logística utilizando os dados fornecidos,
        retornando o modelo ajustado.
    '''

    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    return model


def predict(model, input_data):
    '''
        Realiza a predição de uma nova amostra, retornando a 
        classe prevista e a probabilidade associada.
    '''

    pred = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]
    return pred, prob
