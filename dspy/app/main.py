# main.py
from fastapi import FastAPI, HTTPException, Request, APIRouter
from fastapi.responses import JSONResponse, Response
from typing import Optional, List, Dict, Any
import os
from agents.dspy_integration import load_agent, run_agent
from agents.classifier import register_routes as register_classifier_routes
from agents.summarizer import register_routes as register_summarizer_routes
from agents.textrank_summarizer import register_routes as register_textrank_summarizer_routes  # NEW
from agents.echo import register_routes as register_echo_routes              # NEW
from agents.time import register_routes as register_time_routes              # NEW
from agents.joke import register_routes as register_joke_routes              # NEW
from agents.quote import register_routes as register_quote_routes            # NEW
from agents.math import register_routes as register_math_routes              # NEW

app = FastAPI(title="FastAPI Agent System")

# --- Agent Information ---
AGENTS_INFO: List[Dict[str, str]] = [
    {"name": "hello_world", "description": "Returns a simple hello world message."},
    {"name": "goodbye", "description": "Returns a goodbye message."},
    {"name": "echo", "description": "Returns a simple echo message."},
    {"name": "time", "description": "Returns the current time in ISO 8601 format."},
    {"name": "joke", "description": "Returns a random programming joke."},
    {"name": "quote", "description": "Returns an inspirational quote."},
    {"name": "math", "description": "Evaluates a math expression after verifying a token."},
    {"name": "classifier", "description": "Classifies input text using rule-based logic."},
    {"name": "summarizer", "description": "Summarizes a block of text (truncation)."},
    {"name": "textrank_summarizer", "description": "Summarizes text using TextRank algorithm."},
]

@app.get("/agents", tags=["All Agents"])
async def list_all_agents() -> Dict[str, List[Dict[str, str]]]:
    return {"agents": AGENTS_INFO}

# --- Agent Router ---
agent_router = APIRouter(prefix="/agent")
register_classifier_routes(agent_router)
register_summarizer_routes(agent_router)
register_textrank_summarizer_routes(agent_router)  # NEW: Register the TextRank routes
register_echo_routes(agent_router)                 # NEW: Register Echo Agent routes
register_time_routes(agent_router)                 # NEW: Register Time Agent routes
register_joke_routes(agent_router)                 # NEW: Register Joke Agent routes
register_quote_routes(agent_router)                # NEW: Register Quote Agent routes
register_math_routes(agent_router)                 # NEW: Register Math Agent routes
app.include_router(agent_router)


# --- Other Routes (hello_world, goodbye, generic) ---
# Keep hello_world and goodbye as before.  The generic route is also important.

@app.get("/agent/hello_world", tags=["Simple Agents"])
async def hello_world_agent():
    agent_file = os.path.join("agents", "hello_world.py")
    agent_module = load_agent(agent_file)
    output = run_agent(agent_module)
    return {"agent": "hello_world", "result": output}

@app.get("/agent/goodbye")
async def goodbye_agent():
    agent_file = os.path.join("agents", "goodbye.py")
    agent_module = load_agent(agent_file)
    output = run_agent(agent_module)
    return {"agent": "goodbye", "result": output}


@app.get("/agent/{agent_name}", tags=["Dynamic Agents"]) 
async def execute_agent(agent_name: str, request: Request):
    agent_file = os.path.join("agents", f"{agent_name}.py")
    if not os.path.exists(agent_file):
        raise HTTPException(status_code=404, detail="Agent not found.")

    try:
        agent_module = load_agent(agent_file)

        if hasattr(agent_module, 'TOKEN') and 'token' in request.query_params:
            agent_module.TOKEN = request.query_params['token']
        if hasattr(agent_module, 'EXPRESSION') and 'expression' in request.query_params:
            agent_module.EXPRESSION = request.query_params['expression']
        if hasattr(agent_module, 'INPUT_TEXT') and 'INPUT_TEXT' in request.query_params:
            agent_module.INPUT_TEXT = request.query_params['INPUT_TEXT']
        if hasattr(agent_module, 'TEXT_TO_SUMMARIZE') and 'TEXT_TO_SUMMARIZE' in request.query_params:
            agent_module.TEXT_TO_SUMMARIZE = request.query_params['TEXT_TO_SUMMARIZE']

        output = run_agent(agent_module)
        return {"agent": agent_name, "result": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error executing agent: {str(e)}")



@app.get("/favicon.ico")
async def get_favicon():
    svg = '''<?xml version="1.0" encoding="UTF-8"?>
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
        <rect width="16" height="16" fill="#4a90e2"/>
        <text x="2" y="12" font-size="10" fill="white">A</text>
    </svg>'''
    return Response(content=svg.encode('utf-8'), media_type="image/svg+xml")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Agent System!"}

@app.get("/health")
async def health_check():
    return JSONResponse({"status": "ok", "message": "Healthy"})