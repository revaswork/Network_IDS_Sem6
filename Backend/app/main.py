from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import NetworkData
from app.predictor import predict
from app.simulator import generate_packet

app = FastAPI(title="NIDS Backend 🚨")

# -----------------------------
# ✅ CORS CONFIG (IMPORTANT)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# 📌 Health Check
# -----------------------------
@app.get("/")
def home():
    return {"message": "NIDS Backend Running 🚀"}


# -----------------------------
# 📌 Predict Endpoint
# -----------------------------
@app.post("/predict")
def predict_endpoint(input_data: NetworkData):
    try:
        return predict(input_data.data)
    except Exception as e:
        return {"error": str(e)}


# -----------------------------
# 📌 Simulation Endpoint
# -----------------------------
@app.get("/simulate")
def simulate():
    try:
        return generate_packet()
    except Exception as e:
        return {"error": str(e)}