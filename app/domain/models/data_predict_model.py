from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime




class RequestPredictModel(BaseModel):
    season: str
    mnth: str
    yr: int
    holiday: int
    weekday: str
    workingday: int
    weathersit: str
    temp: float
    atemp: float
    hum: float
    windspeed: float


class ResponsePredictModel(BaseModel):
    bike_number: int
