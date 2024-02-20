from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
from text_preprocessor import is_spam

app = FastAPI()


class ScoringItem(BaseModel):
    Comment: str


with open('spam_detector.pkl', 'rb') as f:
    model = pickle.load(f)


@app.post('/')
async def scoring_endpoint(item: ScoringItem):
    words = pd.read_csv("words_list.csv").squeeze()
    prediction = is_spam(item.Comment, model, words)
    return {"prediction": int(prediction)}
