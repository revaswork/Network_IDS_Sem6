# 🚨 Network Intrusion Detection System (NIDS)

A real-time Network Intrusion Detection System built using **Machine Learning**, **FastAPI**, and **React**, capable of detecting malicious network traffic and visualizing it through an interactive dashboard.

---

## 📌 Overview

This project simulates live network traffic and classifies each packet as **Normal** or **Attack** using a trained **XGBoost model**. The system provides a real-time visualization of packet flow, detection results, and traffic distribution.

---

## 🧠 Features

* 🔁 Real-time packet simulation
* 🤖 ML-based attack detection (XGBoost)
* 📊 Live traffic visualization (Pie Chart)
* 📋 Detection logs with timestamps
* 🌐 Fully deployed frontend & backend
* ⚡ Interactive UI with animations

---

## 🏗️ Tech Stack

### Frontend

* React.js
* JavaScript
* Axios
* Framer Motion
* Recharts

### Backend

* FastAPI
* Python
* Uvicorn

### Machine Learning

* XGBoost
* Scikit-learn
* Pandas

---

## 📂 Project Structure

```
Network_IDS_Sem6/
│
├── Backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── predictor.py
│   │   ├── simulator.py
│   │   ├── model_loader.py
│   │   └── schemas.py
│   │
│   ├── model/
│   │   ├── xgb_model.pkl
│   │   ├── label_encoder.pkl
│   │   └── features.json
│   │
│   ├── data/
│   │   ├── X_test.csv
│   │   └── y_test.csv
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   └── App.js
│   └── package.json
│
└── README.md
```

---

## 🚀 Live Demo

* 🌐 Frontend: https://network-ids-sem6-1.onrender.com
* ⚙️ Backend API: https://network-ids-sem6.onrender.com

---

## ⚙️ How It Works

1. The frontend simulates network packet flow.
2. Each packet is sent to the backend API.
3. The backend uses a trained ML model to classify the packet.
4. The result is returned and visualized in real-time.

---



## 💻 Local Setup

### Backend

```bash
cd Backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

### Frontend

```bash
cd frontend
npm install
npm start
```

---

## 🌍 Deployment

* Backend deployed on Render (FastAPI)
* Frontend deployed on Render (Static Site)


## 👩‍💻 Author

**Reva Shukla**

---

## 📜 License

This project is for academic and educational purposes.
