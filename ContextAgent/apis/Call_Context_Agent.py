from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Tuple, Dict, Any
from agents.agent_factory import AgentFactory
from apis.Example_Log_Keeper import example_log_body as example_log
from apis.Example_Log_Keeper import example_type_body as example_type
import json

# Set up router
context_agent_router = APIRouter()

# --- Pydantic Models ---

class NodeWrapper(BaseModel):
    node: Dict[str, Any] = Field(
        example=example_log["node"]
    )

class Prediction(BaseModel):
    tactic: List[Tuple[str, float]]
    technique: List[Tuple[str, float]]
    subtechnique: List[Tuple[str, float]]

class MitreMatch(BaseModel):
    tactic: str
    technique: str
    subtechnique: Optional[str]
    Detection: str

class ExampleTypeBody(BaseModel):
    prediction: Prediction
    Mitre_Match: List[MitreMatch]

    class Config:
        schema_extra = {
            "example": example_type
        }

# --- API Endpoint ---

@context_agent_router.post("/call-context-agent/")
async def call_context_agent(input_log: NodeWrapper):
    try:
        agent_factory = AgentFactory()
        agent = agent_factory.create_ask_tools_agent()

        # Feed full node and static example_type_body into agent
        response = agent(input_log.node, example_type)
        return {"status": "success", "result": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
