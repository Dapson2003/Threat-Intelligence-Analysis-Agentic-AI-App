from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict
from model.MatchMitre import optimized_match

match_mitre_router = APIRouter()

CSV_PATH = "./model/MitreMatch.csv"

class PredictionRequest(BaseModel):
    prediction: Dict[str, list]

@match_mitre_router.post("/match-mitre")
async def match_mitre(request: PredictionRequest):
    try:
        result = optimized_match(CSV_PATH, request.dict())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
