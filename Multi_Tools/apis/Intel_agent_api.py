from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from config.Config import Config
from agents.agent_factory import AgentFactory

agent_router = APIRouter()

class FToolAnalysisInput(BaseModel):
    attack_type: str
    ftools: List[str]

@agent_router.post("/Ftool_Recommender/")
async def recommend_ftools(input_data: FToolAnalysisInput):
    try:
        config = Config()
        agent_factory = AgentFactory(config)
        agent = agent_factory.create_ftool_selector_agent()

        input_dict = {
            "attack_type": input_data.attack_type,
            "ftools": ", ".join(input_data.ftools)
        }

        result = await agent.ainvoke(input_dict)  # LLMChain supports ainvoke()

        return {"status": "success", "result": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
