import os
import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

def train_regression():
    # Synthetic data: Features are [class_index, confidence]
    # class_index: 0=healthy, 1=mild, 2=moderate, 3=severe
    X = np.array([
        [0, 0.9], [0, 0.8], [0, 0.6],
        [1, 0.9], [1, 0.7], [1, 0.5],
        [2, 0.9], [2, 0.8], [2, 0.6],
        [3, 0.95], [3, 0.85], [3, 0.75]
    ])
    
    # Target: Severity Score 0-100
    y = np.array([5, 10, 15, 30, 40, 50, 60, 70, 75, 90, 95, 100])
    
    model = LinearRegression()
    model.fit(X, y)
    
    preds = model.predict(X)
    print("MAE:", mean_absolute_error(y, preds))
    print("R2:", r2_score(y, preds))
    
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/severity_regression.pkl")
    print("Model saved to models/severity_regression.pkl")

if __name__ == "__main__":
    train_regression()
