# api/root.py
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

root_router = APIRouter()

@root_router.get("/", response_class=HTMLResponse)
async def root():
    html_content = """
    <html>
        <head>
            <title>Agent API</title>
        </head>
        <body>
            <h1>Welcome to the Agent API</h1>
            <p>This is the main entry point for interacting with the agent via API.</p>
            <p>To start using the agent, make a POST request to <a href="/api/publish">/api/publish</a> or <a href="/docs">check the docs</a>.</p>
        </body>
    </html>
    """
    return html_content
