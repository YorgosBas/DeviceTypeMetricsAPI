from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .... import crud, schemas, database

router = APIRouter()

@router.post("/Log/auth", response_model=schemas.DeviceStatCreate)
def log_auth(device_stat: schemas.DeviceStatCreate, db: Session = Depends(database.SessionLocal)):
    return crud.create_device_stat(db, userKey=device_stat.userKey, deviceType=device_stat.deviceType)

@router.get("/Log/auth/statistics")
def get_statistics(deviceType: str, db: Session = Depends(database.SessionLocal)):
    count = crud.get_device_stats_count(db, deviceType)
    return {"deviceType": deviceType, "count": count}