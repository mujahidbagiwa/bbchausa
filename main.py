from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import List
from fastapi import Depends
from .src import model, utils
from pickle import load


class PredictResponse(BaseModel):
    data: List[str]


app = FastAPI()


@app.get('/predict/', response_model=PredictResponse)
def predict(top_n: int = 3, word_length: int = 200, model=model.get_model(), input_data=utils.get_data()):
    prediction = model.predict(input_data, word_length)
    return PredictResponse(data=prediction)
