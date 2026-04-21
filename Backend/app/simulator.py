# import pandas as pd
# import os
# from app.predictor import predict
# from app.model_loader import label_encoder  # 👈 ADD THIS

# BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# X_PATH = os.path.join(BASE_DIR, "data", "X_test.parquet")
# Y_PATH = os.path.join(BASE_DIR, "data", "y_test.parquet")

# X_df = pd.read_parquet(X_PATH)
# y_df = pd.read_parquet(Y_PATH)

# def generate_packet():
#     idx = X_df.sample(1).index[0]

#     row = X_df.loc[idx].to_dict()

#     # 🔥 get encoded value
#     actual_encoded = y_df.loc[idx].values[0]

#     # ✅ DECODE it
#     actual = label_encoder.inverse_transform([actual_encoded])[0]

#     result = predict(row)

#     predicted = result["prediction"]

#     # Normalize labels
#     if str(predicted).upper() == "BENIGN":
#         predicted = "Normal"

#     if str(actual).upper() == "BENIGN":
#         actual = "Normal"

#     return {
#         "packet": row,
#         "prediction": predicted,
#         "actual": actual,
#         "confidence": result["confidence"]
#     }

# import pandas as pd
# import os
# from app.predictor import predict
# from app.model_loader import label_encoder

# BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# X_PATH = os.path.join(BASE_DIR, "data", "X_test.parquet")
# Y_PATH = os.path.join(BASE_DIR, "data", "y_test.parquet")

# # Load safely
# try:
#     X_df = pd.read_parquet(X_PATH)
#     y_df = pd.read_parquet(Y_PATH)
# except Exception as e:
#     print("Error loading data:", e)
#     X_df = None
#     y_df = None


# def generate_packet():
#     if X_df is None or y_df is None:
#         return {"error": "Data not loaded"}

#     idx = X_df.sample(1).index[0]

#     row = X_df.loc[idx].to_dict()

#     actual_encoded = y_df.loc[idx].values[0]
#     actual = label_encoder.inverse_transform([actual_encoded])[0]

#     result = predict(row)

#     predicted = result["prediction"]

#     # Normalize labels
#     if str(predicted).upper() == "BENIGN":
#         predicted = "Normal"

#     if str(actual).upper() == "BENIGN":
#         actual = "Normal"

#     return {
#         "packet": row,
#         "prediction": predicted,
#         "actual": actual,
#         "confidence": result["confidence"]
#     }

import pandas as pd
import os
from app.predictor import predict
from app.model_loader import label_encoder

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# ✅ Directly use CSV (no parquet anywhere)
X_PATH = os.path.join(BASE_DIR, "data", "X_test.csv")
Y_PATH = os.path.join(BASE_DIR, "data", "y_test.csv")

# Load safely
try:
    X_df = pd.read_csv(X_PATH)
    y_df = pd.read_csv(Y_PATH)
except Exception as e:
    print("Error loading data:", e)
    X_df = None
    y_df = None


def generate_packet():
    if X_df is None or y_df is None:
        return {"error": "Data not loaded"}

    idx = X_df.sample(1).index[0]

    row = X_df.loc[idx].to_dict()

    actual_encoded = y_df.loc[idx].values[0]
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