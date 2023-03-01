from fastapi import FastAPI
from app.infrastructure.routers import predict


def create_app():
    app = FastAPI(
        title="Bike Model",
        description="Service for predict bike numbers",
        version="1.0.0",
        openapi_url="/openapi.json",
    )
    app.include_router(
        predict.router,
        prefix="/bike",
        tags=["Model"]
    )

    app.include_router(
        predict.router,
        prefix="/bike",
        tags=["Model"]
    )

    return app