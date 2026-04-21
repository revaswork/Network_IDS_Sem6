import joblib
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

model = joblib.load(os.path.join(BASE_DIR, "model/xgb_model.pkl"))
label_encoder = joblib.load(os.path.join(BASE_DIR, "model/label_encoder.pkl"))

with open(os.path.join(BASE_DIR, "model/features.json")) as f:
    features = json.load(f) 