from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from config.Config import Config
from agents.agent_factory import AgentFactory

agent_router = APIRouter()

class FToolAnalysisInput(BaseModel):
    Detect_Type: List[str]
    Detect_Methods: List[str]
    Raw_Logs: str

@agent_router.post("/Ftool_Recommender/")
async def recommend_ftools(input_data: FToolAnalysisInput):
    try:
        config = Config()
        agent_factory = AgentFactory(config)
        agent = agent_factory.create_ftool_selector_agent()

        input_dict = {
            "Detection_Types": ", ".join(input_data.Detect_Type),
            "Detection_Methods": ", ".join(input_data.Detect_Methods),
            "Raw_Logs" : input_data.Raw_Logs
        }

        result = await agent.ainvoke(input_dict)  # LLMChain supports ainvoke()

        return {"status": "success", "result": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
