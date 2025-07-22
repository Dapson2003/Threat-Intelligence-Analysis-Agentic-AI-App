from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Tuple, Dict, Any
from agents.agent_factory import AgentFactory
from tools.Example_Log_Keeper import example_log_body as example_log
from tools.Example_Log_Keeper import example_type_body as example_type
from tools.Example_Log_Keeper import example_client_tools_body as example_client_tools

# Set up router
recommendation_agent_router = APIRouter()

# --- Pydantic Models ---

class NodeWrapper(BaseModel):
    node: Dict[str, Any] 
    
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
    
    
class RecommendationInput(BaseModel):
    log: Optional[NodeWrapper] = Field(
        default=None,
        example=example_log
    )
    type: Optional[ExampleTypeBody] = Field(
        default=None,
        example=example_type
    )
    client_tools: Optional[Dict[str, Any]] = Field(
        default=None,
        example=example_client_tools
    )


# --- API Endpoint ---
@recommendation_agent_router.post("/call-recommendation-agent/")
async def call_recommendation_agent(input_data: RecommendationInput):
    
    # Handle defaults on API side This code run when the API package is Null
    try:
        log_data = input_data.log.node if input_data.log and input_data.log.node else example_log["node"]
        type_data = input_data.type.dict() if input_data.type else example_type
        tools_data = input_data.client_tools if input_data.client_tools else example_client_tools

        agent_factory = AgentFactory()
        agent = agent_factory.create_recommending_agent()

        response = agent(
            log=log_data,
            mitre_attack_type=type_data,
            client_tools_json=tools_data
        )
        return {"status": "success", "result": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
