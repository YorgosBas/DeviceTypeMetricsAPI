from fastapi import FastAPI, HTTPException, Query
import databases
import sqlalchemy

# Database configuration
DATABASE_URL = "postgresql://postgres:admin@pg-minikube-postgresql:5432/jsafraapi"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Define table structure
device_registration = sqlalchemy.Table(
    "device_registration",
    metadata,
    sqlalchemy.Column("userKey", sqlalchemy.String,primary_key=True),
    sqlalchemy.Column("deviceType", sqlalchemy.String),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/Device/register")
async def register_device(userKey: str = Query(...), deviceType: str = Query(...)):
    query = device_registration.insert().values(userKey=userKey, deviceType=deviceType)
    await database.execute(query)
    return {"statusCode": 200}