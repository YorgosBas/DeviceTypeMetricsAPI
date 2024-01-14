from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .... import crud, schemas, database
import requests

router = APIRouter()

@router.post("/auth")
def log_auth(device_stat: schemas.DeviceStatCreate):
    try:
        data = device_stat.dict()
        response = requests.post(url="http://127.0.0.1:8000/Device/register", json=data)
        if response.status_code == 200:
            return {"statusCode": 200, "message": "success"}
        else:
            return {"statusCode": 400, "message": "bad_request"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/auth/statistics")
def get_statistics(deviceType: str, db: Session = Depends(database.SessionLocal)):
    count = crud.get_device_stats_count(db, deviceType)
    return {"deviceType": deviceType, "count": count}