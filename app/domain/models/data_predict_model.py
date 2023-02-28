from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime




class RequestPredictModel(BaseModel):
    season: str
    month: str
    year: str
    holiday: int
    temp: float
    atemp: float
    hum: float
    windspeed: float
    cnt_1: int
    cnt_7: int


class ConsultResponseModel(BaseModel):
    results: List[Dict]
