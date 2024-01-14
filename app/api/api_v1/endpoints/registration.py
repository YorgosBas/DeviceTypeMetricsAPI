from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .... import crud, schemas, database

router = APIRouter()

@router.post("/Device/register", response_model=schemas.DeviceRegistrationCreate)
def register_device(device_registration: schemas.DeviceRegistrationCreate, db: Session = Depends(database.SessionLocal)):
    return crud.create_device_registration(db, userKey=device_registration.userKey, deviceType=device_registration.deviceType)