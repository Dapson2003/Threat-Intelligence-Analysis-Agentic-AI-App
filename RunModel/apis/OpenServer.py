from Connection_to_Nats import OpenModelServer
from fastapi import APIRouter, HTTPException


Open_Server_router = APIRouter()

@Open_Server_router.post("/Open_Server")
async def OpenServer():
    try:
       await OpenModelServer()  # Initialize NATS connection and start the model server
       return {"message": "Model server is running and ready to receive messages."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
