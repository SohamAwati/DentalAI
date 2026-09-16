import os
import joblib
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from mlxtend.frequent_patterns import apriori, association_rules

def train_insights():
    # 1. PCA & K-Means (Archetypes)
    # Synthetic features: [brushing_freq, sugar_intake, past_severity, age]
    X_habits = np.random.rand(200, 4)
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_habits)
    
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    kmeans.fit(X_pca)
    
    os.makedirs("models", exist_ok=True)
    joblib.dump(pca, "models/pca_model.pkl")
    joblib.dump(kmeans, "models/kmeans_model.pkl")
    print("PCA & KMeans saved.")
    
    # 2. Association Rule Mining (Apriori)
    # Synthetic binary transactions
    data = {'low_brushing': [1, 0, 1, 0, 1],
            'high_sugar': [1, 1, 0, 0, 1],
            'has_cavity': [1, 0, 1, 0, 1],
            'flosses': [0, 1, 0, 1, 0]}
    df = pd.DataFrame(data).astype(bool)
    
    frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
    
    rules.to_pickle("models/association_rules.pkl")
    print("Association rules saved to models/association_rules.pkl")

if __name__ == "__main__":
    import numpy as np
    train_insights()
