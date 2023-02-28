from fastapi import FastAPI
from app.infrastructure.routers import predict


def create_app():
    app = FastAPI(
        title="Consult data base",
        description="Service for querying the mongo database",
        version="1.0.0",
        openapi_url="/openapi.json",
    )
    app.include_router(
        predict.router,
        prefix="/ConsultDB",
        tags=["Database"]
    )

    return app