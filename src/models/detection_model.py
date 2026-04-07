import pandas as pd
from sklearn.linear_model import LogisticRegression


def load_data():
    return pd.read_csv("./data/breast_cancer.csv")


def prepare_data(dataset):
    X = dataset.iloc[:, 1:-1].values
    y = dataset.iloc[:, -1].values
    return X, y
    

def train_model(X, y):
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    return model


def predict(model, input_data):
    pred = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]
    return pred, prob
