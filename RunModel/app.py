# app.py
from fastapi import FastAPI
from apis.root import root_router
from apis.PredictOne import predict_router
from apis.ConvertOne import convert_router
from apis.OpenServer import Open_Server_router  
from apis.MatchMitre import match_mitre_router
from Connection_to_Nats import OpenModelServer

app = FastAPI(title="Agent Model API")
#OpenModelServer
@app.on_event("startup")
async def startup_event():
    await OpenModelServer()  # ✅ Automatically run this at startup
# Route registration
app.include_router(root_router)  # Handles "/"
app.include_router(predict_router, prefix="/api")
app.include_router(convert_router, prefix="/api")
app.include_router(convert_router, prefix="/api")
app.include_router(Open_Server_router, prefix="/api")
app.include_router(match_mitre_router, prefix="/api")

