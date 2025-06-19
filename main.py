from fastapi import FastAPI
from app.route import router

app = FastAPI(title="LangGraph AI Agent")
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Agent Chatbot API. Use /chat for chatbot functionality."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)