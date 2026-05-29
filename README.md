# 🌸 Data Classification Using AI
## DecodeLabs Industrial Training | Batch 2026 | Project 2

---

### About
A machine learning web application that classifies
Iris flowers using the K-Nearest Neighbors algorithm.
Built strictly following the DecodeLabs Project 2
PDF specifications.

---

### PDF Concepts Implemented

| PDF Page | Concept | Status |
|---|---|---|
| Page 7 | IPO Framework | ✅ |
| Page 8 | Iris Benchmark Dataset | ✅ |
| Page 9 | Gatekeeper Rule - StandardScaler | ✅ |
| Page 10 | Train-Test Split 80/20 + Shuffle | ✅ |
| Page 11 | KNN Algorithm K=5 Majority Vote | ✅ |
| Page 12 | Optimal K - Elbow Point | ✅ |
| Page 13 | Scikit-Learn Workflow fit/predict | ✅ |
| Page 14 | Accuracy Mirage - No blind accuracy | ✅ |
| Page 15 | Confusion Matrix TP FP FN TN | ✅ |
| Page 16 | F1 Score Precision and Recall | ✅ |
| Page 17 | Full Pipeline Architecture | ✅ |

---

### Tech Stack
- Backend: Python, Flask
- ML Library: Scikit-Learn
- Algorithm: K-Nearest Neighbors (K=5)
- Dataset: Iris Benchmark (150 samples)
- Frontend: HTML, CSS, Vanilla JavaScript
- Theme: Dark / Black

---

### How to Run

Step 1 - Install dependencies:
pip install flask scikit-learn numpy

Step 2 - Train and save the model:
python model.py

Step 3 - Run the web server:
python app.py

Step 4 - Open in browser:
http://localhost:5000

---

### How to Use

1. Open http://localhost:5000
2. Enter 4 flower measurements:
   - Sepal Length (cm): 4.0 to 8.0
   - Sepal Width (cm): 2.0 to 5.0
   - Petal Length (cm): 1.0 to 7.0
   - Petal Width (cm): 0.1 to 3.0
3. Click PREDICT SPECIES
4. See the predicted flower species

---

### Sample Test Values

| Species | Sepal L | Sepal W | Petal L | Petal W |
|---|---|---|---|---|
| Setosa | 5.1 | 3.5 | 1.4 | 0.2 |
| Versicolor | 6.0 | 2.9 | 4.5 | 1.5 |
| Virginica | 6.3 | 3.3 | 6.0 | 2.5 |

---

### Project Structure
data-classification-ai/
├── model.py
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── templates/
    └── index.html

---

### Built By
- Program : DecodeLabs Industrial Training
- Batch   : 2026
- Project : Project 2 - Data Classification Using AI
- Contact : decodelabs.tech@gmail.com
- Website : www.decodelabs.tech
