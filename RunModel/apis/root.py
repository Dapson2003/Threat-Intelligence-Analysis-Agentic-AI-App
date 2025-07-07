# apis/root.py
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

root_router = APIRouter()

@root_router.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head><title>Agent Model API</title></head>
        <body>
            <h1>Welcome to the Agent Model API</h1>
            <p>
                Try: <br>
                - <a href="/api/predict">/api/predict</a><br>
                - <a href="/api/convert">/api/convert</a><br>
                - <a href="/api/logs">/api/logs</a><br>
                Or visit the <a href="/docs">Swagger UI</a>.
            </p>
        </body>
    </html>
    """
