# dataset link: https://archive.ics.uci.edu/ml/datasets/Wine

import pandas as pd

#"fixed acidity";"volatile acidity";"citric acid";"residual sugar";"chlorides";"free sulfur dioxide";"total sulfur dioxide";"density";"pH";"sulphates";"alcohol";"quality"

df = pd.read_csv("winequality-red.csv", delimiter=';')
df = df.astype(float)


from sklearn.model_selection import train_test_split

X = df.drop('quality',axis=1)
y = df['quality']

X_train, X_test, y_train, y_test = train_test_split(X, y)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaler.fit(X_train)

StandardScaler(copy=True, with_mean=True, with_std=True)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neural_network import MLPClassifier



mlp = MLPClassifier(hidden_layer_sizes=(12, 12),max_iter=2000)

mlp.fit(X_train, y_train)

predictions = mlp.predict(X_test)

print(y_test.values)
print(predictions)
s = 0

for x in range(len(predictions)):
    s += abs(predictions[x] - y_test.values[x])
print(s)


