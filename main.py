from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
import asyncio

from agent import customer_support_bot

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

async def stream_text(text):
    for word in text.split():
        yield word + " "
        await asyncio.sleep(0.03)

@app.post("/chat")
async def chat(req: ChatRequest):

    response = customer_support_bot(req.message)

    return StreamingResponse(
        stream_text(response),
        media_type="text/plain"
    )