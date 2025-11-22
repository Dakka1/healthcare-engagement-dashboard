from fastapi import FastAPI, Request
from sqlalchemy.orm import Session
from backend.database import Base, engine, SessionLocal
from backend.models.physician import Physician
from backend.models.message import Message
import pandas as pd
import time
import os
from backend.api.physicians import router as physicians_router
from backend.api.messages import router as messages_router
from backend.api.classify import router as classify_router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app.include_router(physicians_router)
app.include_router(messages_router)
app.include_router(classify_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables on startup
Base.metadata.create_all(bind=engine)


# Dependency to get DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Middleware for request latency logging
@app.middleware("http")
async def log_request_latency(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    print(f"Request {request.url.path} took {duration:.4f} sec")
    return response


# Load CSV data into SQLite if empty
@app.on_event("startup")
def load_data():
    db = SessionLocal()

    physicians_count = db.query(Physician).count()
    messages_count = db.query(Message).count()

    if physicians_count == 0:
        print("Loading physicians into database")
        df = pd.read_csv("backend/data/physicians.csv")
        records = df.to_dict(orient="records")
        for row in records:
            p = Physician(**row)
            db.add(p)
        db.commit()

    if messages_count == 0:
        print("Loading messages into database")
        df = pd.read_csv("backend/data/messages.csv")
        records = df.to_dict(orient="records")
        for row in records:
            m = Message(**row)
            db.add(m)
        db.commit()

    db.close()

@app.get("/")
def root():
    return {"message": "Healthcare Engagement Dashboard Backend Running"}