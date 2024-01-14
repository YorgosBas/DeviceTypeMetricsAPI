from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DeviceStats(Base):
    __tablename__ = 'device_stats'
    userKey = Column(String, primary_key=True)
    deviceType = Column(String)

class DeviceRegistration(Base):
    __tablename__ = 'device_registration'
    userKey = Column(String, primary_key=True)
    deviceType = Column(String)