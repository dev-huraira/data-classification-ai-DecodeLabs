import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score, confusion_matrix, classification_report

# PDF Page 7 & 8 - IPO Framework Phase 1: INPUT
iris = load_iris()
X = iris.data
y = iris.target
class_names = ['Setosa', 'Versicolor', 'Virginica']

# PDF Page 9 - Gatekeeper Rule: Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PDF Page 10 - Train-Test Split 80/20 + Shuffle
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, shuffle=True, random_state=42
)

# PDF Page 11 & 12 - KNN Algorithm K=5 (Optimal Elbow Point)
# PDF Page 13 - Scikit-Learn Workflow: fit/predict
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# PDF Page 14 - Accuracy Mirage: Do NOT rely on accuracy alone
# PDF Page 15 - Confusion Matrix TP FP FN TN
cm = confusion_matrix(y_test, predictions)

# PDF Page 16 - F1 Score Precision and Recall
f1 = f1_score(y_test, predictions, average='weighted')
report = classification_report(y_test, predictions, target_names=class_names)

MODEL_RESULTS = {
    'f1_score': float(f1),
    'confusion_matrix': cm.tolist(),
    'classification_report': report,
    'training_size': int(len(y_train)),
    'testing_size': int(len(y_test)),
    'class_names': class_names,
    'k_value': 5,
    'algorithm': 'K-Nearest Neighbors',
    'dataset': 'Iris Benchmark',
    'total_samples': 150,
    'features': 4,
    'classes': 3
}

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

with open('results.pkl', 'wb') as f:
    pickle.dump(MODEL_RESULTS, f)

print("=" * 50)
print("MODEL TRAINING SUMMARY")
print("=" * 50)
print(f"Training Size: {MODEL_RESULTS['training_size']}")
print(f"Testing Size: {MODEL_RESULTS['testing_size']}")
print(f"F1 Score: {MODEL_RESULTS['f1_score']:.4f}")
print("\nConfusion Matrix:")
print(cm)
print("\nClassification Report:")
print(report)
print("=" * 50)
print("Model saved successfully")
