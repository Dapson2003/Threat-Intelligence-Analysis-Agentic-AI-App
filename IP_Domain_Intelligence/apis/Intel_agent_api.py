from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from config.Config import Config
from agents.agent_factory import ThreatIntelAgentFactory

# Create a FastAPI instance
agent_router = APIRouter()

# Define the input data model that will be sent via the API
class QueryInput(BaseModel):
    query: str

# Define the API endpoint to invoke the agent
@agent_router.post("/IP_Domain_Intelligence/")
async def process_query(query_input: QueryInput):
    try:
        # Initialize configuration and agent factory
        config = Config()
        agent_factory = ThreatIntelAgentFactory(config)
        
        # Create the agent using the factory
        agent = agent_factory.create_react_agent()
        
        # Invoke the agent with the provided query
        result = await agent.ainvoke({"input": query_input.query})
        
        # Return the result
        return {"status": "success", "result": result}
    
    except Exception as e:
        # If an error occurs, return an error response
        raise HTTPException(status_code=500, detail=str(e))
