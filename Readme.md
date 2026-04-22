# Network Intrusion Detection System (NIDS)

A real-time Network Intrusion Detection System built using Machine Learning, FastAPI, and React. The system classifies live network traffic as benign or malicious and presents detection results through an interactive dashboard.

---

## Overview

This project trains a multi-class classifier on the CICIDS dataset to identify various categories of network attacks, then exposes that model through a REST API that simulates and scores live packet streams. Detection results are visualized in real time via a React frontend.

---

## Features

- Real-time packet simulation and classification
- Multi-class attack detection using XGBoost
- Live traffic visualization with pie chart and detection logs
- Timestamped event history for audit and review
- Fully deployed frontend and backend
- Interactive, animated UI

---

## Dataset and Preprocessing

The model is trained on the **CICIDS dataset** (CIC Intrusion Detection Systems dataset), processed end-to-end in the included notebook (`CICIDS_PINNACLE.ipynb`).

### Data Cleaning

- Duplicate records removed
- Column names stripped of leading/trailing whitespace
- Infinite values (`+inf`, `-inf`) replaced with `NaN`
- Missing values in `Flow Bytes/s` and `Flow Packets/s` imputed using column medians
- Zero-variance bulk-rate columns dropped (`Fwd/Bwd Avg Bytes/Bulk`, `Fwd/Bwd Avg Packets/Bulk`, `Fwd/Bwd Avg Bulk Rate`)
- Duplicate header column `Fwd Header Length.1` removed

### Label Engineering

Raw labels were consolidated into the following attack categories:

| Original Labels | Mapped Category |
|---|---|
| BENIGN | BENIGN |
| DDoS | DDoS |
| DoS Hulk, DoS GoldenEye, DoS slowloris, DoS Slowhttptest | DoS |
| PortScan | Port Scan |
| FTP-Patator, SSH-Patator | Brute Force |
| Bot | Bot |
| Web Attack (Brute Force, XSS, SQL Injection) | Web Attack |
| Infiltration, Heartbleed | Excluded (Rare Attack) |

Labels were encoded numerically using `sklearn.preprocessing.LabelEncoder`, and the fitted encoder is serialized to `label_encoder.pkl` for use at inference time.

### Feature Selection

A correlation matrix was computed over all numeric features. Features with pairwise absolute correlation above 0.90 were dropped to reduce multicollinearity. The `Destination Port` column was also excluded from the final feature set.

### Class Balancing

The BENIGN class was downsampled to 200,000 records to reduce its dominance over attack classes. The final dataset was shuffled and split 80/20 into training and test sets using stratified sampling to preserve class proportions.

---

## Model

The classifier is an **XGBoost** model trained on the preprocessed CICIDS feature set. A Random Forest baseline was also evaluated during development. The final XGBoost model and label encoder are serialized and loaded by the backend API at startup.

---

## Tech Stack

**Frontend:** React.js, Axios, Framer Motion, Recharts

**Backend:** FastAPI, Python, Uvicorn

**Machine Learning:** XGBoost, Scikit-learn, Pandas, NumPy, Joblib

---

## Project Structure

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
├── CICIDS_PINNACLE.ipynb
└── README.md
```

---

## Live Demo

- **Frontend:** https://network-ids-sem6-1.onrender.com
- **Backend API:** https://network-ids-sem6.onrender.com

---

## How It Works

1. The frontend generates simulated network packet data.
2. Each packet is submitted to the FastAPI backend via HTTP.
3. The backend loads the packet's features, applies the trained XGBoost model, and returns a predicted class label.
4. The frontend renders the classification result in real time, updating the traffic chart and detection log.

---

## Local Setup

**Backend**

```bash
cd Backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend**

```bash
cd frontend
npm install
npm start
```

---

## Deployment

The backend is deployed on Render as a FastAPI application. The frontend is deployed on Render as a static site.

---

## Author

**Reva Shukla**

---

## License

This project is developed for academic and educational purposes.