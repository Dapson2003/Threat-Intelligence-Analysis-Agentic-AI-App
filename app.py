from fastapi import FastAPI
import uvicorn
from apis.root_api import root_router
from apis.Intel_agent_api import agent_router

# Create the FastAPI app
app = FastAPI()

# Include the routers for different parts of the app
app.include_router(root_router)
app.include_router(agent_router)

def start_api():
    """
    Start the FastAPI server without opening any UI.
    This will allow users to interact with the agent through API endpoints.
    """
    uvicorn.run(app, host="0.0.0.0", port=9002)

if __name__ == "__main__":
    print("Starting the agent API server...")
    start_api()
