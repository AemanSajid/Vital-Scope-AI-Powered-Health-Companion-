import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

def train_diabetes_model():
    #  Load dataset
    df = pd.read_csv("data/diabetes.csv")

    #  Features and target
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    #  Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    #  Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=1)

    #  Train model
    model = svm.SVC(kernel='linear', probability=True)
    model.fit(X_train, y_train)

    #  Return values in correct order
    train_acc = accuracy_score(y_train, model.predict(X_train))
    test_acc = accuracy_score(y_test, model.predict(X_test))

    return model, scaler, X_test, y_test, train_acc, test_acc, df
