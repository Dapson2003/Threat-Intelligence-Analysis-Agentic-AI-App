# apis/convertone.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from model.convert_input_format import convert_input_format

convert_router = APIRouter()

class NodeWrapper(BaseModel):
    node: Dict[str, Any]

@convert_router.post("/convert")
async def convert(alert: NodeWrapper):
    try:
        cleaned = convert_input_format(alert.dict())
        return {"converted_input": cleaned}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
