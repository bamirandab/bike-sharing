from fastapi import APIRouter, status, Response
from app.domain.models.data_predict_model import ResponsePredictModel, RequestPredictModel
from app.domain.usecases.predict_model.predict import BikeModel

router = APIRouter()


@router.get('/predict',
            status_code=status.HTTP_200_OK,
            summary='Get prediction',
            response_model=ResponsePredictModel
            )
async def execute_consult(season: str, mnth: str, yr: int , holiday: int, weekday: str, workingday: int, weathersit: str,
                          temp: float, atemp: float, hum: float, windspeed: float) -> object:
    request_data = RequestPredictModel(season=season, mnth=mnth, yr=yr, holiday=holiday, weekday=weekday,
                                       workingday=workingday, weathersit=weathersit, temp=temp, atemp=atemp,
                                       hum=hum, windspeed=windspeed)
    bike_model = BikeModel(request_data)
    return bike_model.predict()

