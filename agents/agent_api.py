from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config.Config import Config
from agents.agent_factory import ThreatIntelAgentFactory

# Create a FastAPI instance
app = FastAPI()

# Define the input data model that will be sent via the API
class QueryInput(BaseModel):
    query: str

# Define the API endpoint to invoke the agent
@app.post("/process_query/")
async def process_query(query_input: QueryInput):
    try:
        # Initialize configuration and agent factory
        config = Config()
        agent_factory = ThreatIntelAgentFactory(config)
        
        # Create the agent using the factory
        agent = agent_factory.create_react_agent()
        result = agent.invoke({"input": query_input.query})
        
        return {"status": "success", "result": result}
    
    except Exception as e:
        # If an error occurs, return an error response
        raise HTTPException(status_code=500, detail=str(e))
