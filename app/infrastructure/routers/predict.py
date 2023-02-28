from fastapi import APIRouter, status, Response
from app.domain.models.data_models.Request.get_request import RequestDataBaseModel, ConsultResponseModel
from app.domain.usecases.consult_data_base.request_data_base import ConsultDataBaseUseCase

router = APIRouter()


@router.get('/predict',
            status_code=status.HTTP_200_OK,
            summary='Get prediction',
            response_model=ConsultResponseModel
            )
async def execute_consult(collection: str= None, field: str = None, value: str = None):
    query = {field: value}
    request_data = RequestDataBaseModel(collection = collection, query = query)
    return ConsultDataBaseUseCase(request_data).consults_data_base()