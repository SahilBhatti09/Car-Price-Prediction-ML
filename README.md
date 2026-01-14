# 🚗 Car Price Prediction – Full Stack ML App

A **full-stack Machine Learning project** that predicts the **selling price of used cars** using a trained ML model, exposed via a **FastAPI backend** and consumed by a **Streamlit frontend UI**.

---

## 📌 Project Overview

This project demonstrates an **end-to-end ML workflow**, covering:

- Data preprocessing & model training
- Model evaluation using regression metrics
- Backend API using FastAPI
- Frontend UI using Streamlit
- Deployment-ready architecture

The system allows users to enter car details and receive a **predicted selling price** in real time.

---

## 🧠 Tech Stack

### Machine Learning
- Python
- Pandas, NumPy
- Scikit-learn (RandomForestRegressor)
- Joblib

### Backend
- FastAPI
- Uvicorn

### Frontend
- Streamlit
- Requests

### Deployment
- Railway / Render (API)
- Streamlit Cloud / Railway (UI)

---

## 🏗️ Architecture
User
│
│ (inputs)
▼
Streamlit Frontend
│
│ HTTP POST (JSON)
▼
FastAPI Backend
│
│ ML Pipeline (Preprocessing + Model)
▼
Predicted Car Price

---

## 📊 Model Details

- **Model**: RandomForestRegressor
- **Preprocessing**:
  - One-Hot Encoding for categorical features
  - Numeric features passed as-is
  - `handle_unknown="ignore"` to prevent inference failures
- **Pipeline**: `ColumnTransformer + RandomForest`

---

## 📈 Model Performance

| Metric | Value |
|------|------|
| Train R² | ~0.98 |
| Test R² | ~0.96 |
| MAE | ~0.59 |
| RMSE | ~0.89 |
| Mean CV R² | ~0.35 |

### ⚠️ Important Note on Metrics
- The **cross-validation score is unstable** due to:
  - Small dataset size
  - High-cardinality categorical feature (`Car_Name`)
- This is expected behavior for tree-based models with limited data.
- Increasing dataset size or using **CatBoost / LightGBM** would significantly improve generalization.

---

## 🔑 Key Learnings & Findings

- One-hot encoding high-cardinality features can harm cross-validation stability
- Train/test scores alone can be misleading without CV
- Pipelines simplify deployment and prevent feature mismatch errors
- `handle_unknown="ignore"` is critical for real-world APIs
- Separating frontend and backend improves scalability

---

## 🎨 Streamlit Frontend

A clean, interactive UI built using **Streamlit** that:

- Collects user input via forms
- Sends JSON payload to FastAPI
- Displays prediction results instantly
- Handles API failures gracefully

### Features
- Dropdowns for categorical features
- Numeric validation
- Live JSON preview
- User-friendly error handling
- Footer branding

---

## 📂 Project Structure
Car-Price-Prediction-ML/
│
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ └── model.py
│ │ └── schema.py
│ ├── random_forest_model.pkl
│ ├── feature_columns.pkl
│ ├── encoder.pkl
│ ├── requirements.txt
│ ├── runtime.txt
│
├── frontend/
│ ├── streamlit_app.py
│ ├── requirements.txt
│ ├── runtime.txt
│
├── car_data.csv
├── train.ipynb
├── README.md


---

## 🚀 Running Locally

### 1️⃣ Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

---

## 🚀 Running Locally

### 1️⃣ Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

API available at:
http://127.0.0.1:8000

### 2️⃣ Frontend (Streamlit)
cd frontend
pip install -r requirements.txt
streamlit run streamlit_app.py

Frontend runs at:
http://localhost:8501

### 🌍 Deployment
* Backend deployed using FastAPI
* Frontend deployed using Streamlit
* Services communicate via REST API
* Free-tier compatible deployment strategy

### 🔮 Future Improvements
* Increase dataset size
* Replace One-Hot Encoding with CatBoost encoding
* Add logging & monitoring
* Model versioning
* Authentication layer

## 👤 Author
Sahil Bhatti
