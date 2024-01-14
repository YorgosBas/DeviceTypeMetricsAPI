from fastapi import FastAPI, Query
import databases
import sqlalchemy

# Database configuration (testing)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@pg-minikube-postgresql:5432/jsafraapi"
database = databases.Database(SQLALCHEMY_DATABASE_URL)
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URL)
metadata = sqlalchemy.MetaData()
metadata.create_all(engine)

SessionLocal = sqlalchemy.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = sqlalchemy.declarative_base()

# Table structure
device_stats = sqlalchemy.Table(
    "device_stats",
    metadata,
    sqlalchemy.Column("userKey", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("deviceType", sqlalchemy.String),
)

async def startup():
    await database.connect()
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)

async def shutdown():
    await database.disconnect()
    
app = FastAPI()
app.add_event_handler("startup", startup)
app.add_event_handler("shutdown", shutdown)

@app.post("/Log/auth")
async def log_auth(userKey: str = Query(...), deviceType: str = Query(...)):
    query = device_stats.insert().values(userKey=userKey, deviceType=deviceType)
    await database.execute(query)
    return {"statusCode": 200, "message": "success"}

@app.get("/Log/auth/statistics")
async def get_statistics(deviceType: str = Query(...)):
    query = sqlalchemy.select([sqlalchemy.func.count()]).select_from(device_stats).where(device_stats.c.deviceType == deviceType)
    count = await database.fetch_val(query)
    return {"deviceType": deviceType, "count": count}