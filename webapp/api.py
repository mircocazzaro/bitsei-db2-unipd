from fastapi import APIRouter
from endpoints import (
    crime, business, covid
)

api_router = APIRouter()
api_router.include_router(covid.router, prefix="/covid", tags=["covid"])
api_router.include_router(crime.router, prefix="/crime", tags=["crime"])
api_router.include_router(business.router, prefix="/business", tags=["business"])
