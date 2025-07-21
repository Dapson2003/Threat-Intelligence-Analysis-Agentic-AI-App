from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from rag.rag_chain import build_rag_chain

from tools.Example_Log_Keeper import (
    example_log_body as example_log,
    example_type_body as example_type,
    example_client_tools_body as example_client_tools
)

# Set up router
rag_agent_router = APIRouter()
qa_chain = build_rag_chain()

# --- Pydantic Model ---

class NodeWrapper(BaseModel):
    node: Dict[str, Any]

class RagQueryInput(BaseModel):
    log: Optional[NodeWrapper] = Field(
        default=None,
        example=example_log
    )
    type: Optional[Dict[str, Any]] = Field(
        default=None,
        example=example_type
    )
    client_tools: Optional[Dict[str, Any]] = Field(
        default=None,
        example=example_client_tools
    )
    query: Optional[str] = Field(
        default="What action should be taken?",
        example="What are the key cybersecurity threats in this log?"
    )

# --- API Endpoint ---

@rag_agent_router.post("/rag_ask/")
async def ask_rag(input_data: RagQueryInput):
    try:
        log_data = input_data.log.node if input_data.log and input_data.log.node else example_log["node"]
        type_data = input_data.type if input_data.type else example_type
        tools_data = input_data.client_tools if input_data.client_tools else example_client_tools
        query = input_data.query.strip() if input_data.query else "What action should be taken?"

        # Call RAG chain (returns plain str)
        result_text = qa_chain(
            log=log_data,
            mitre_attack_type=type_data,
            client_tools_json=tools_data,
            question=query
        )

        return {"status": "success", "result": result_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))










































"""_summary_

    Old code for the RAG agent API endpoint.


from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from rag.rag_chain import build_rag_chain

# Set up router
rag_agent_router = APIRouter()
qa_chain = build_rag_chain()

# --- Pydantic Model ---

class RagQueryInput(BaseModel):
    query: Optional[str] = Field(
        default=None,
        example="What are the key cybersecurity threats in this log?"
    )
    context: Optional[Dict[str, Any]] = Field(
        default=None,
        example={"ip": "192.168.1.10", "source": "EDR"}
    )

# --- API Endpoint ---

@rag_agent_router.post("/rag_ask/")
async def ask_rag(input_data: RagQueryInput):
    try:
        query = input_data.query or "Explain this log in terms of cyber risk."
        query = query.strip()
        if not query:
            raise HTTPException(status_code=400, detail="Query cannot be empty")

        # Pass context into the chain if your RAG supports it (optional)
        result = qa_chain({
            "query": query,
            "context": input_data.context or {}
        })

        return {
            "status": "success",
            "answer": result["result"],
            "source_documents": [doc.metadata for doc in result["source_documents"]]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
"""