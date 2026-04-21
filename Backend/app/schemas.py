from pydantic import BaseModel

class NetworkData(BaseModel):
    data: dict

class PredictionResponse(BaseModel):
    prediction: str
    confidence: float