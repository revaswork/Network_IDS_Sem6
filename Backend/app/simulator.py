import pandas as pd
import os
from app.predictor import predict
from app.model_loader import label_encoder  # 👈 ADD THIS

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

X_PATH = os.path.join(BASE_DIR, "data", "X_test.parquet")
Y_PATH = os.path.join(BASE_DIR, "data", "y_test.parquet")

X_df = pd.read_parquet(X_PATH)
y_df = pd.read_parquet(Y_PATH)

def generate_packet():
    idx = X_df.sample(1).index[0]

    row = X_df.loc[idx].to_dict()

    # 🔥 get encoded value
    actual_encoded = y_df.loc[idx].values[0]

    # ✅ DECODE it
    actual = label_encoder.inverse_transform([actual_encoded])[0]

    result = predict(row)

    predicted = result["prediction"]

    # Normalize labels
    if str(predicted).upper() == "BENIGN":
        predicted = "Normal"

    if str(actual).upper() == "BENIGN":
        actual = "Normal"

    return {
        "packet": row,
        "prediction": predicted,
        "actual": actual,
        "confidence": result["confidence"]
    }