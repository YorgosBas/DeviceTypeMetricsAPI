import requests, os
from fastapi import APIRouter, Depends
from .... import crud, schemas
from ....security import verify_token

router = APIRouter()
DEVICE_REGISTER_URL = os.getenv("DEVICE_REGISTER_URL", "http://127.0.0.1:8000/Device/register")

@router.post("/auth")
def log_auth(device_stat: schemas.DeviceStatCreate, token: str = Depends(verify_token)):
    data = device_stat.dict()
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(url=DEVICE_REGISTER_URL, json=data, headers=headers)
    if response.status_code == 200:
        return {"statusCode": 200, "message": "success"}
    else:
        return {"statusCode": 400, "message": "bad_request"}
    
@router.get("/auth/statistics")
def get_statistics(deviceType: str):
    count = crud.get_device_stats_count(deviceType)
    if count is not None:
        return {"deviceType": deviceType, "count": count}
    else:
        return {"deviceType": deviceType, "count": -1}