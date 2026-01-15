from fastapi import FastAPI
from pydantic import BaseModel
from src.agent import run_diagnostic

app = FastAPI(title="DevOps AI Agent Service")

class Query(BaseModel):
    prompt: str

@app.post("/ask")
async def ask_agent(query: Query):
    result = run_diagnostic(query.prompt)
    return {"answer": result["messages"][-1].content}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)