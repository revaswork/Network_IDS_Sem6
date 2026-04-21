import pandas as pd
from app.model_loader import model, label_encoder, features

def predict(data: dict):
    df = pd.DataFrame([data])

    # Ensure correct feature order
    df = df[features]

    pred = model.predict(df)[0]
    prob = model.predict_proba(df).max()

    label = label_encoder.inverse_transform([pred])[0]

    return {
        "prediction": label,
        "confidence": float(prob)
    }