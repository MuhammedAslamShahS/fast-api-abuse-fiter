from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .filter import is_clean

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

@app.post("/filter")
def filter_message(message: Message):
    allowed, msg = is_clean(message.text)
    return {"allowed": allowed, "message": msg}

@app.get("/")
def root():
    return {"status": "API is running"}
