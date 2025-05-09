from pydantic import BaseModel
from typing import List, Optional

class SeriesBase(BaseModel):
    activity: str
    reps_per_min: float
    set_time_secs: float
    rest_time_secs: float
    sets_count: int

class SeriesCreate(SeriesBase):
    pass

class Series(SeriesBase):
    id: int
    session_id: int

    class Config:
        from_attributes = True

class SessionBase(BaseModel):
    name: str
    warmup_time_secs: float
    series_rest_time_secs: float
    use_sound: bool

class SessionCreate(SessionBase):
    pass

class Session(SessionBase):
    id: int
    series: List[Series]

    class Config:
        from_attributes = True
