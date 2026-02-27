from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.metrics import precision_recall_curve

def get_predictions(independent, target):
    X_train, X_test, y_train, y_test = train_test_split(
        independent, target, test_size=0.2, random_state=42
    )

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    lr = LogisticRegression(class_weight="balanced")
    lr.fit(X_train, y_train)


    
    # Find best threshold on training data
    probs_train = lr.predict_proba(X_train)[:,1]
    precision, recall, thresholds = precision_recall_curve(y_train, probs_train)
    f1_scores = 2 * (precision * recall) / (precision + recall + 1e-8)
    best_threshold = thresholds[np.argmax(f1_scores[:-1])]

    # Apply threshold to TEST data
    probs_test = lr.predict_proba(X_test)[:,1]
    predictions = (probs_test >= best_threshold).astype(int)

    return predictions, y_test, probs_train, X_train, X_test, y_train