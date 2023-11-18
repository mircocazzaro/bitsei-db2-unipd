from fastapi import APIRouter
from endpoints import (
    crime
)

api_router = APIRouter()
api_router.include_router(crime.router, prefix="/crime", tags=["crime"])
