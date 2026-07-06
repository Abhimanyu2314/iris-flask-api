# 🌸 Iris Intelligence Platform

A production-grade, end-to-end Machine Learning web application that classifies Iris flower species using a trained Random Forest algorithm. The system features a responsive, premium "luxury-dark" glassmorphism web interface and exposes a scalable Flask REST API deployed globally on Render.

## 🚀 Live Demo
🌐 **Application URL:** [https://iris-flask-api-eax0.onrender.com/](https://iris-flask-api-eax0.onrender.com/)

---

## 🛠️ Tech Stack & Architecture

- **Machine Learning Core:** Python, Scikit-Learn, Joblib
- **Backend API Layer:** Flask (WSGI framework), Gunicorn (Production HTTP Server)
- **Frontend Layer:** HTML5, CSS3 (Custom Glassmorphism + Copper/Emerald Theme), Vanilla JavaScript (Async/Fetch API)
- **Cloud Infrastructure & DevOps:** Git, GitHub, Render Cloud Platform

---

## 📁 Repository Structure

```text
iris-flask-api/
│
├── templates/
│   └── index.html        # Premium front-end UI layout & async logic
│
├── app.py                # Core Flask backend application & prediction route
├── train.py              # ML training script utilizing Scikit-Learn
├── iris_model.pkl        # Serialized, trained Random Forest Classifier model
├── test_api.py           # Verification script for local/cloud endpoints
└── requirements.txt      # Production library dependencies