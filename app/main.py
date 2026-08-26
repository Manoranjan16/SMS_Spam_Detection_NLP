from fastapi import FastAPI
from .schemas import SpamRequest, SPamResponse
from .config import MODEL_PATH
import pickle

app = FastAPI()

with open(MODEL_PATH, "rb") as file:
    pipeline = pickle.load(file)

@app.get("/")
def home():
    return {"message": "Welcome to FASTAPI for Spam Detection"}


@app.post("/predict", response_model=SPamResponse)
def predict_spam(data: SpamRequest):
    prediction = pipeline.predict([data.message])

    result = "It's Spam " if prediction[0] == 1 else "It's Ham"

    return {
        "message": data.message,
        "prediction": result
    }



