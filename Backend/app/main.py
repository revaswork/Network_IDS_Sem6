

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import NetworkData
from app.predictor import predict
from app.simulator import generate_packet

app = FastAPI(title="NIDS Backend 🚨")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health Check
@app.get("/")
def home():
    return {
        "message": "NIDS Backend Running 🚀",
        "status": "ok"
    }

# Predict
@app.post("/predict")
def predict_endpoint(input_data: NetworkData):
    try:
        return predict(input_data.data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Simulate
@app.get("/simulate")
def simulate():
    try:
        return generate_packet()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))