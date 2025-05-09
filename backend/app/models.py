from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    warmup_time_secs = Column(Float)
    series_rest_time_secs = Column(Float)
    series = relationship("Series", back_populates="session")

class Series(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("sessions.id"))
    activity = Column(String)
    reps_per_min = Column(Float)
    set_time_secs = Column(Float)
    rest_time_secs = Column(Float)
    sets_count = Column(Integer)
    session = relationship("Session", back_populates="series")
