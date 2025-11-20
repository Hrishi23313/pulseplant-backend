from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class WorkerCreate(BaseModel):
    name: str
    badge_id: Optional[str] = None
    role: Optional[str] = "operator"
    supervisor_id: Optional[int] = None

class WorkerRead(BaseModel):
    id: int
    name: str
    badge_id: Optional[str]
    role: str
    supervisor_id: Optional[int]

    class Config:
        orm_mode = True

class ShiftCreate(BaseModel):
    worker_id: int
    machine_id: Optional[int] = None

class ShiftEnd(BaseModel):
    shift_id: int
    end_time: Optional[datetime] = None

class ShiftRead(BaseModel):
    id: int
    worker_id: int
    machine_id: Optional[int]
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    hours: Optional[float]
    status: str

    class Config:
        orm_mode = True
