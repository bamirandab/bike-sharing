from fastapi import APIRouter, status, Response
from app.domain.models.data_predict_model import ResponsePredictModel, RequestPredictModel
from app.domain.usecases.predict_model.predict import BikeModel

router = APIRouter()


@router.post('/train',
            status_code=status.HTTP_200_OK,
            summary='Train model'
            )
async def execute_consult(Credentials) -> object:
    pass
    return None