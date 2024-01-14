from fastapi import APIRouter
from .endpoints import auth, registration

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(registration.router, prefix="/registration", tags=["registration"])