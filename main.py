from email.base64mime import header_length
#main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
    return {"message": "Service is online"}