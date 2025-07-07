# app.py
from fastapi import FastAPI
from apis.root import root_router
from apis.PredictOne import predict_router
from apis.ConvertOne import convert_router
from apis.LogOne import loggen_router  # Optional

app = FastAPI(title="Agent Model API")

# Route registration
app.include_router(root_router)  # Handles "/"
app.include_router(predict_router, prefix="/api")
app.include_router(convert_router, prefix="/api")
app.include_router(loggen_router, prefix="/api/logs")  # Optional
