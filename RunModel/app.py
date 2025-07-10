# app.py
import os
from fastapi import FastAPI
from apis.root import root_router
from apis.PredictOne import predict_router
from apis.ConvertOne import convert_router
from apis.OpenServer import Open_Server_router  
from apis.MatchMitre import match_mitre_router
from Connection_to_Nats import OpenModelServer
from config.Config import cfg

app = FastAPI(title="Agent Model API")
#OpenModelServer base on environment variable
@app.on_event("startup")
async def startup_event():
    auto_open = cfg.AUTO_OPEN_CONNECTION # Is boolean, default is False
    if auto_open:
        print("AUTO_OPEN_CONNECTION is enabled. Connecting...")
        await OpenModelServer()
    else:
        print("AUTO_OPEN_CONNECTION is disabled. Skipping startup connection.")
        
# Route registration
app.include_router(root_router)  # Handles "/"
app.include_router(predict_router, prefix="/api")
app.include_router(convert_router, prefix="/api")
app.include_router(convert_router, prefix="/api")
app.include_router(Open_Server_router, prefix="/api")
app.include_router(match_mitre_router, prefix="/api")

