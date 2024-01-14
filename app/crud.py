from sqlalchemy.orm import Session
from .models import DeviceStats, DeviceRegistration

def create_device_stat(db: Session, userKey: str, deviceType: str):
    db_item = DeviceStats(userKey=userKey, deviceType=deviceType)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_device_registration(db: Session, userKey: str, deviceType: str):
    db_item = DeviceRegistration(userKey=userKey, deviceType=deviceType)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_device_stats_count(db: Session, deviceType: str):
    return db.query(DeviceStats).filter(DeviceStats.deviceType == deviceType).count()