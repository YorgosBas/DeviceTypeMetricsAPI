from pydantic import BaseModel

class DeviceStatCreate(BaseModel):
    userKey: str
    deviceType: str

class DeviceRegistrationCreate(BaseModel):
    userKey: str
    deviceType: str