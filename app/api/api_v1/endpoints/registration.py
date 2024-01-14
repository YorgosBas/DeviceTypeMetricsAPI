from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .... import crud, schemas, database

router = APIRouter()

@router.post("/register")
def register_device(device_stat: schemas.DeviceRegistrationCreate):
    try:
        crud.create_device_stat(userKey=device_stat.userKey, deviceType=device_stat.deviceType)
        return {"statusCode": 200}
    except Exception:
        raise HTTPException(status_code=400, detail="bad_request")