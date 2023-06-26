import os
import sys
from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipeline
from pydantic import BaseModel

app = FastAPI()

text:str = "What is text summarisation?"

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs/")

@app.get("/check")
async def check():
    return Response("API is up and running!")

@app.get("/train")
async def train():
    try:
        os.system("python main.py")
        return Response("Training completed successfully!")
    
    except Exception as e:
        return Response(e)
    
class PredictionInputModal(BaseModel):
    text:str

@app.post("/predict")
async def predict(text:PredictionInputModal):
    try:
        prediction = PredictionPipeline()
        summary = prediction.predict(text.text)
        return summary
    
    except Exception as e:
        return Response(e)
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)