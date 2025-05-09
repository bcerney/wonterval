from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/sessions/", response_model=schemas.Session)
def create_session(session: schemas.SessionCreate, db: Session = Depends(get_db)):
    db_session = models.Session(**session.dict())
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session

@app.get("/sessions/", response_model=List[schemas.Session])
def list_sessions(db: Session = Depends(get_db)):
    return db.query(models.Session).all()

@app.post("/sessions/{session_id}/series/", response_model=schemas.Series)
def create_series(
    session_id: int,
    series: schemas.SeriesCreate,
    db: Session = Depends(get_db)
):
    db_series = models.Series(**series.dict(), session_id=session_id)
    db.add(db_series)
    db.commit()
    db.refresh(db_series)
    return db_series
