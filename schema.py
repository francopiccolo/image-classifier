from pydantic import BaseModel
from typing import List


class Prediction(BaseModel):
    class_: str
    confidence: str
    
    class Config:
        fields = {'class_': 'class'}

class PredictionsList(BaseModel):
    __root__: List[Prediction]