from .models import DeviceStats, DeviceRegistration
from .database import db 

def create_device_stat(userKey: str, deviceType: str):
    db_item = DeviceStats(userKey=userKey, deviceType=deviceType)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_device_registration(userKey: str, deviceType: str):
    db_item = DeviceRegistration(userKey=userKey, deviceType=deviceType)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_device_stats_count(deviceType: str):
    return db.query(DeviceStats).filter(DeviceStats.deviceType == deviceType).count()