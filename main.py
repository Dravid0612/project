from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/api/v1/hackrx/run")
async def run_webhook(data: Query):
    response = {
        "answer": f"You asked: '{data.question}'. This is a placeholder answer.",
        "source": "dummy.pdf"
    }
    return response
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

