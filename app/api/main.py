from fastapi import FastAPI
from pydantic import BaseModel
from app.agents.orchestrator import QueryOrchestrator

app=FastAPI(title="QueryPilot AI API")

class QueryRequest(BaseModel):
    question:str
    history:str=""

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/query")
def query(request:QueryRequest):
    return QueryOrchestrator().run(request.question,request.history)
