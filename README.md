# 🌸 Data Classification Using AI
## DecodeLabs Industrial Training | Batch 2026 | Project 2

---

## 📌 About

This is a Machine Learning Web Application that classifies
Iris flowers into 3 species using the K-Nearest Neighbors
algorithm. Built strictly following the DecodeLabs Project 2
PDF specifications.

You enter 4 measurements of a flower, click Predict, and
the AI tells you which species it is out of 3 types.

---

## 🤖 What This Project Does

### The Simple Flow
User enters 4 measurements
↓
Flask receives the data
↓
StandardScaler normalizes the numbers
↓
KNN Algorithm finds 5 nearest neighbors
↓
Majority vote decides the species
↓
Result shown on screen

### What Each File Does

| File | Job |
|---|---|
| model.py | Trains the AI and saves it to disk |
| app.py | Runs the web server and handles requests |
| templates/index.html | The web page the user sees |
| model.pkl | The trained AI brain saved as file |
| scaler.pkl | The data normalizer saved as file |
| results.pkl | F1 score and confusion matrix saved |
| requirements.txt | List of libraries needed |

### What the Web App Shows

LEFT SIDE:
- 4 input fields for flower measurements
- Predict button
- Result box with species name and emoji

RIGHT SIDE:
- F1 Score metric card
- Algorithm name card
- Dataset size card
- Confusion Matrix table
- Model information table

### The 3 Flower Species

| Species | Emoji | Description |
|---|---|---|
| Setosa | 🌸 | Small petals, easy to identify |
| Versicolor | 🌺 | Medium sized flower |
| Virginica | 🌼 | Largest of the three |

### Model Performance

| Metric | Value |
|---|---|
| Algorithm | KNN K=5 |
| Dataset | Iris Benchmark |
| Total Samples | 150 flowers (balanced) |
| Training Data | 120 flowers (80%) |
| Testing Data | 30 flowers (20%) |
| Features | 4 measurements per flower |
| Classes | 3 species |
| Scaling | StandardScaler Mean=0 Variance=1 |
| Evaluation | F1 Score + Confusion Matrix |

---

## 🏗️ Architecture

- Model: K-Nearest Neighbors (Supervised Learning)
- Lookup: K=5 Optimal Elbow Point
- Structure: IPO Model (Input → Process → Output)
- Scaling: StandardScaler (Gatekeeper Rule)
- Evaluation: F1 Score — No Accuracy Mirage
- Pipeline: Train → Scale → Split → Fit → Predict

---

## 🛠️ Tech Stack

- Backend: Python 3, Flask
- ML Library: Scikit-Learn
- Algorithm: K-Nearest Neighbors (K=5)
- Dataset: Iris Benchmark (150 samples)
- Frontend: HTML, CSS, Vanilla JavaScript
- Theme: Dark / Black
- Serialization: Pickle

---

## 📁 Project Structure
data-classification-ai/
├── model.py              ← Train and save ML model
├── app.py                ← Flask web server
├── model.pkl             ← Saved trained model
├── scaler.pkl            ← Saved scaler
├── results.pkl           ← Saved metrics
├── requirements.txt      ← Dependencies
├── .gitignore            ← Git ignore rules
├── README.md             ← This file
└── templates/
└── index.html        ← Web UI

---

## ⚙️ How to Run — First Time Setup

### Step 1 — Install Python

- Download Python 3.8 or higher from python.org
- During installation check "Add Python to PATH"
- Verify installation:
python --version

### Step 2 — Get the Project

Option A — Clone from GitHub:
git clone https://github.com/dev-huraira/data-classification-ai
cd data-classification-ai

Option B — Copy folder manually:
- Copy the entire project folder to your system
- Open terminal inside that folder

### Step 3 — Install Libraries
pip install flask scikit-learn numpy

### Step 4 — Train the Model (REQUIRED)
python model.py

This step is MANDATORY on every new system because:
- model.pkl is in .gitignore
- scaler.pkl is in .gitignore
- results.pkl is in .gitignore
- These files are NOT on GitHub
- They are created fresh when you run model.py

You will see this output:
==================================================
MODEL TRAINING SUMMARY
Training Size: 120
Testing Size: 30
F1 Score: 0.9667
Confusion Matrix: ...
Classification Report: ...
Model saved successfully

### Step 5 — Start the Web Server
python app.py

You will see:

Running on http://127.0.0.1:5000
Debug mode: on


### Step 6 — Open in Browser
http://localhost:5000

---

## 🔄 How to Run on a New System

Every time you move to a new computer follow
these steps in this exact order:
=======================================
QUICK START — NEW SYSTEM

pip install flask scikit-learn numpy
python model.py
python app.py
open http://localhost:5000

ALWAYS run model.py BEFORE app.py
.pkl files are NOT on GitHub
They are created by model.py
=======================================

---

## 🧪 How to Use the Web App

1. Open http://localhost:5000 in your browser
2. Enter 4 flower measurements in the input fields
3. Click PREDICT SPECIES button
4. See the predicted flower species with emoji

---

## 🌸 Sample Test Values

Use these values to test your model is working:

### Test 1 — Should predict SETOSA

| Field | Value |
|---|---|
| Sepal Length | 5.1 |
| Sepal Width | 3.5 |
| Petal Length | 1.4 |
| Petal Width | 0.2 |

Expected Result: 🌸 SETOSA

### Test 2 — Should predict VERSICOLOR

| Field | Value |
|---|---|
| Sepal Length | 6.0 |
| Sepal Width | 2.9 |
| Petal Length | 4.5 |
| Petal Width | 1.5 |

Expected Result: 🌺 VERSICOLOR

### Test 3 — Should predict VIRGINICA

| Field | Value |
|---|---|
| Sepal Length | 6.3 |
| Sepal Width | 3.3 |
| Petal Length | 6.0 |
| Petal Width | 2.5 |

Expected Result: 🌼 VIRGINICA

---

## ❌ Common Errors and Fixes

| Error | Cause | Fix |
|---|---|---|
| ModuleNotFoundError: flask | Libraries not installed | pip install flask scikit-learn numpy |
| FileNotFoundError: model.pkl | model.py not run first | Run python model.py first |
| FileNotFoundError: scaler.pkl | model.py not run first | Run python model.py first |
| FileNotFoundError: results.pkl | model.py not run first | Run python model.py first |
| Port 5000 already in use | Another app using port | Close other apps or change port in app.py |
| pip not found | Python not in PATH | Reinstall Python with PATH checkbox ticked |

---

## ⚠️ Important Rules
ALWAYS run in this exact order:
python model.py    ← FIRST (creates .pkl files)
python app.py      ← SECOND (starts web server)
Never run app.py before model.py
on a fresh system. It will crash
because .pkl files will be missing.

---

## 📄 PDF Concepts Implemented

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

## 👨‍💻 Built By

- Program : DecodeLabs Industrial Training
- Batch   : 2026
- Project : Project 2 - Data Classification Using AI
- Contact : decodelabs.tech@gmail.com
- Website : www.decodelabs.tech
