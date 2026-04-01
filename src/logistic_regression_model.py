import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

# Carregando o dataset
dataset = pd.read_csv('./breast_cancer.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# Separando o dataset em 'Training Set' e 'Test Set'
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Treinando o modelo de Regressão Logística a partir do 'Training Set'
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

# Prevendo resultados a partir do 'Test Set'
y_pred = classifier.predict(X_test)

# Construindo a 'Confusion Matrix'
cm = confusion_matrix(y_test, y_pred)